"""Importe les combat logs d'OPTCG Sim dans parties/logs/ et crée une fiche par partie.

    python scripts/sync_logs.py              # importe les parties terminées pas encore copiées
    python scripts/sync_logs.py --watch      # tourne en fond, importe chaque partie dès qu'elle se termine
    python scripts/sync_logs.py --source "D:/OPTCGSim/Builds_Windows/CombatLogs"

Le sim ne garde qu'une centaine de logs et ses mises à jour vident le dossier : on copie tout.
Le dossier du sim n'est JAMAIS modifié (lecture + copie seulement).
Une partie en cours s'écrit dans un fichier *.partial.log : on l'ignore et on attend le *.log final.
Source : --source, sinon la variable OPTCG_COMBATLOGS, sinon recherche automatique.
"""
import argparse
import glob
import os
import shutil
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.join(RACINE, "parties", "logs")
HOME = os.path.expanduser("~")
CANDIDATS = [
    os.path.join(HOME, "Downloads", "*", "Builds_Windows", "CombatLogs"),
    os.path.join(HOME, "Downloads", "*", "CombatLogs"),
    os.path.join(HOME, "Desktop", "*", "Builds_Windows", "CombatLogs"),
    r"C:\Program Files\*\Builds_Windows\CombatLogs",
    r"C:\Program Files\*\CombatLogs",
    r"C:\Program Files (x86)\*\Builds_Windows\CombatLogs",
    os.path.join(HOME, "Games", "*", "Builds_Windows", "CombatLogs"),
    os.path.join(HOME, "Library", "Application Support", "*", "CombatLogs"),   # Mac
]


def trouver_sources(force=None):
    if force:
        return [force]
    if os.environ.get("OPTCG_COMBATLOGS"):
        return [os.environ["OPTCG_COMBATLOGS"]]
    vus = []
    for motif in CANDIDATS:
        for d in glob.glob(motif):
            d = os.path.normpath(d)
            if os.path.isdir(d) and d not in vus:
                vus.append(d)
    return vus


def logs_termines(source, delai_partiel=600):
    """Parties terminées. Le sim finalise un *.partial.log en *.log au plus tard au lancement de la
    partie suivante : un partiel sans écriture depuis `delai_partiel` secondes et qui contient au moins
    un tour joué est pris aussi (dernière partie d'une session). Sa fiche sera remplacée si le .log arrive."""
    tous = glob.glob(os.path.join(source, "**", "*.log"), recursive=True)
    finaux = {f[:-len(".log")] for f in tous if not f.endswith(".partial.log")}
    for f in tous:
        if not f.endswith(".partial.log"):
            yield f
        elif f[:-len(".partial.log")] not in finaux and time.time() - os.path.getmtime(f) > delai_partiel:
            with open(f, encoding="utf-8", errors="replace") as h:
                if "End Turn" in h.read():
                    yield f


def importer(sources, fiches=True, bavard=True):
    os.makedirs(DEST, exist_ok=True)
    nouveaux = []
    for src in sources:
        for f in logs_termines(src):
            cible = os.path.join(DEST, os.path.basename(f))
            if os.path.exists(cible) and os.path.getsize(cible) == os.path.getsize(f):
                continue
            shutil.copy2(f, cible)
            nouveaux.append(cible)
            # version finale arrivée : la copie du partiel ne sert plus
            partiel = cible[:-len(".log")] + ".partial.log"
            if not cible.endswith(".partial.log") and os.path.exists(partiel):
                os.remove(partiel)
    if fiches and nouveaux:
        import fiche_partie
        for c in sorted(nouveaux):
            try:
                r = fiche_partie.traiter(c, force=True)
            except Exception as e:   # une fiche ratée ne bloque pas l'import
                r = None
                print(f"  fiche impossible pour {os.path.basename(c)} : {e}", file=sys.stderr)
            if bavard:
                print(f"+ {os.path.basename(c)} -> {os.path.relpath(r, RACINE) if r else 'pas de fiche (partie incomplète)'}")
    elif bavard:
        for c in nouveaux:
            print(f"+ {os.path.basename(c)}")
    return nouveaux


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--watch", action="store_true", help="surveille le dossier et importe en continu")
    ap.add_argument("--source", help="dossier CombatLogs du sim")
    ap.add_argument("--intervalle", type=float, default=5, help="secondes entre deux vérifications (--watch)")
    ap.add_argument("--sans-fiche", action="store_true", help="copier les logs sans créer de fiche")
    a = ap.parse_args()

    sources = trouver_sources(a.source)
    if not sources:
        sys.exit("Dossier CombatLogs introuvable. Donne-le avec --source ou la variable OPTCG_COMBATLOGS.")
    for s in sources:
        print(f"Source : {s}")
    n = importer(sources, fiches=not a.sans_fiche)
    print(f"{len(n)} partie(s) importée(s) -> {os.path.relpath(DEST, RACINE)}")
    if not a.watch:
        return
    print("Surveillance en cours (Ctrl+C pour arrêter)...")
    try:
        while True:
            time.sleep(a.intervalle)
            # le sim peut avoir été déplacé ou mis à jour : on recherche les dossiers à chaque passage
            importer(trouver_sources(a.source) or sources, fiches=not a.sans_fiche)
    except KeyboardInterrupt:
        print("Arrêt.")


if __name__ == "__main__":
    main()
