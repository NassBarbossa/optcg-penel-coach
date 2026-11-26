"""Combat log OPTCG Sim -> fiche de partie (parties/AAAA-MM-JJ-HHMM-<mon-leader>-vs-<son-leader>.md).

    python scripts/fiche_partie.py parties/logs/<fichier>.log [--force]
    python scripts/fiche_partie.py --tout [--force]       # toutes les parties de parties/logs/

Ne lit que les lignes lisibles du log (pas les lignes RZ1|..., encodage machine non documenté).
Le log contient la main adverse en clair : la fiche n'en garde que le NOMBRE de cartes, pour que
l'analyse se fasse avec l'information réellement disponible au moment de la décision.
Les pseudos adverses sont remplacés par « Adversaire », le mien par « Moi ».
"""
import argparse
import datetime as dt
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cartes as base_cartes  # noqa: E402

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS = os.path.join(RACINE, "parties", "logs")
PARTIES = os.path.join(RACINE, "parties")
PSEUDO = os.environ.get("OPTCG_PSEUDO", "Barbossa")

ID = r"[A-Z0-9]+-\d{3}"
RE_LINK = re.compile(r'<mark><link="([^"]+)">[^<]*</link></mark>')
RE_TAG = re.compile(r"</?[a-z]+[^>]*>")
RE_JOUEUR = re.compile(r"^\[([^\]]*#\d+|You|Opponent)\] (.*)$")
RE_CARTE = re.compile(rf"(.+?) \[({ID})\]")
SNAP = ("Hand:", "Board:", "Trash:", "Life:")


# ---------------------------------------------------------------- lecture

def nettoyer(ligne):
    ligne = ligne.replace("​", "").rstrip("\r\n")
    ligne = RE_LINK.sub(r"\1", ligne)
    return RE_TAG.sub("", ligne)


def liste_ids(txt):
    txt = txt.strip()[1:-1]
    return [x for x in txt.split(",") if x]


def heure_depuis_nom(nom):
    """2026-11-26T01.06.32.5192590-<id>.log (UTC) -> datetime locale."""
    m = re.match(r"(\d{4}-\d\d-\d\dT\d\d\.\d\d\.\d\d)", os.path.basename(nom))
    if not m:
        return None
    t = dt.datetime.strptime(m.group(1), "%Y-%m-%dT%H.%M.%S").replace(tzinfo=dt.timezone.utc)
    return t.astimezone()


class Tour:
    def __init__(self, num, joueur):
        self.num, self.joueur = num, joueur
        self.lignes = []          # (auteur ou None, texte)
        self.etat = {}            # joueur -> {Hand, Board, Trash, Life}
        self.attaques = []
        self.ferme = False
        self.bonus = False


def parser(chemin):
    with open(chemin, encoding="utf-8", errors="replace") as f:
        brutes = [nettoyer(l) for l in f if not l.startswith("RZ1|")]
    # CHAT|<base64> : messages du chat (peuvent contenir des pseudos) -> jamais repris
    brutes = [l for l in brutes if l.strip() and not l.startswith("CHAT|")]

    p = {"fichier": os.path.basename(chemin), "heure": heure_depuis_nom(chemin), "leaders": {},
         "ordre": [], "premier": None, "moi": None, "main_avant": None, "main_apres": None,
         "mulligan": {}, "tours": [], "fin": None, "version": None, "pre": []}

    # joueur local = celui dont la main avant mulligan est affichée
    for l in brutes:
        m = RE_JOUEUR.match(l)
        if m and m.group(2).startswith("Hand before Mulligan"):
            p["moi"] = m.group(1)
    for l in brutes:
        m = RE_JOUEUR.match(l)
        if m and m.group(2).startswith("Leader is"):
            c = RE_CARTE.search(m.group(2)[len("Leader is "):])
            p["leaders"][m.group(1)] = (c.group(1), c.group(2)) if c else (m.group(2), None)
            if m.group(1) not in p["ordre"]:
                p["ordre"].append(m.group(1))
    if not p["moi"]:
        p["moi"] = next((j for j in p["ordre"] if j.split("#")[0].lower() == PSEUDO.lower()), None)
    adv = [j for j in p["ordre"] if j != p["moi"]]
    p["adv"] = adv[0] if adv else None
    leader_de = {lid: j for j, (_, lid) in p["leaders"].items() if lid}

    tour = None
    commence = False
    dernier_auteur = None
    tour_bonus = False
    for l in brutes:
        m = RE_JOUEUR.match(l)
        auteur, txt = (m.group(1), m.group(2)) if m else (None, l)
        if auteur in ("You", "Opponent"):
            auteur = p["moi"] if auteur == "You" else p["adv"]
        if txt.startswith("Version is"):
            p["version"] = txt.split()[-1]
        if "Chose to go" in txt:
            p["premier"] = auteur if txt.endswith("First") else next((j for j in p["ordre"] if j != auteur), None)
        if auteur and txt.startswith("Hand before Mulligan"):
            p["main_avant"] = liste_ids(txt.split(":", 1)[1])
        if auteur and txt.startswith("Hand after Mulligan"):
            p["main_apres"] = liste_ids(txt.split(":", 1)[1])
        if auteur and txt == "Mulligan":
            p["mulligan"][auteur] = True
        if txt.endswith(("Concedes!", "Quits!")) and not p["fin"]:
            # le premier qui part décide de la partie ; l'autre quitte ensuite l'écran
            p["fin"] = (auteur, txt.split()[-1].rstrip("!"))

        if not commence:
            if auteur and re.match(r"Draw \d+ Don", txt):
                commence = True
            else:
                p["pre"].append((auteur, txt))
                continue

        est_snap = auteur and txt.startswith(SNAP)
        if est_snap:
            cible = tour if tour else None
            if cible:
                cle, val = txt.split(":", 1)
                cible.etat.setdefault(auteur, {})[cle] = int(val) if cle == "Life" else liste_ids(val)
            continue
        if txt == "Taking another Turn!" and tour is not None:
            tour.ferme, tour_bonus = True, True      # tour supplémentaire (ex. Luffy OP05-119)
        if tour is None or tour.ferme:
            if tour is None:
                joueur = p["premier"]
            elif tour_bonus:
                joueur = tour.joueur
            else:
                joueur = p["adv"] if tour.joueur == p["moi"] else p["moi"]
            tour = Tour(len(p["tours"]) + 1, joueur)
            tour.bonus, tour_bonus = tour_bonus, False
            p["tours"].append(tour)
        # propriétaire des lignes sans [joueur] : leader -> son joueur, sinon dernier auteur
        if auteur is None:
            c = RE_CARTE.match(txt)
            if c and c.group(2) in leader_de and txt.startswith(c.group(0) + ":"):
                proprio = leader_de[c.group(2)]
            else:
                proprio = dernier_auteur
        else:
            proprio = auteur
            dernier_auteur = auteur
        # information cachée : les pioches adverses ne sont gardées qu'en nombre
        if proprio == p["adv"] and txt.startswith("Drew card from deck"):
            txt = "pioche 1 carte"
        tour.lignes.append((proprio, txt, auteur is not None))
        if auteur and txt == "End Turn":
            tour.ferme = True
    return p


# ---------------------------------------------------------------- analyse d'un tour

def nom_carte(cid):
    c = base_cartes.charger().get(cid)
    return c["nom"] if c else cid


def decouper_attaques(tour):
    """Regroupe chaque attaque avec ses counters / blocks / triggers / résultat."""
    attaques, cour = [], None
    for i, (proprio, txt, _) in enumerate(tour.lignes):
        m = re.match(rf"(.+?) \[({ID})\] attacking (.+?) \[({ID})\]$", txt)
        if m:
            cour = {"att": (m.group(1), m.group(2)), "cible": (m.group(3), m.group(4)),
                    "joueur": proprio, "counters": [], "block": None, "trigger": [],
                    "vs": None, "issue": None, "autres": [], "debut": i, "lignes": {i}}
            attaques.append(cour)
            continue
        if not cour:
            continue
        if txt == "End Turn" or (cour["issue"] and proprio == cour["joueur"] and not txt.endswith("Destroyed")):
            cour = None
            continue
        cour["lignes"].add(i)
        if re.match(rf".+ \[{ID}\]\[\d+\] vs .+ \[{ID}\]\[\d+\]$", txt):
            pw = re.findall(r"\]\[(\d+)\]", txt)
            cour["vs"] = (int(pw[0]), int(pw[1]))
        elif m2 := re.match(rf"Discard (.+?) \[({ID})\] for Counter (\d+)", txt):
            cour["counters"].append(f"{m2.group(1)} +{m2.group(3)}")
        elif m2 := re.match(rf"(.+?) \[({ID})\]: Activate Counter", txt):
            cour["counters"].append(f"{m2.group(1)} (event)")
        elif m2 := re.match(rf"(.+?) \[({ID})\] Blocks", txt):
            cour["block"] = m2.group(1)
        elif m2 := re.match(rf"(.+?) \[({ID})\]: Activate Trigger", txt):
            cour["trigger"].append(m2.group(1))
        elif "hit for" in txt:
            cour["issue"] = "touche (" + txt.split("hit for ")[1] + ")"
        elif txt == "Attack Fails":
            cour["issue"] = "échoue"
        elif txt.endswith("Destroyed") and cour["issue"] is None:
            mort = RE_CARTE.match(txt)
            cour["issue"] = f"K.O. de {mort.group(1)}" if mort else "K.O."
        elif txt.endswith("Destroyed"):
            cour["autres"].append(txt)
        else:
            cour["autres"].append(("attaquant" if proprio == cour["joueur"] else "défense") + " : " + txt)
    return attaques


def compter_don(p):
    """DON!! sur le terrain de chaque joueur à la fin de chaque tour (pioches - retours).
    Le log écrit « Draw 2 Don » même quand le deck DON!! est presque vide : on plafonne à la taille
    du deck DON!! (6 pour un Leader dont le texte le précise, comme Enel OP15-058, sinon 10)."""
    db = base_cartes.charger()
    taille = {}
    for j in (p["moi"], p["adv"]):
        lid = p["leaders"].get(j, (None, None))[1]
        m = re.search(r"DON!! deck consists of (\d+)", (db.get(lid) or {}).get("effet", ""))
        taille[j] = int(m.group(1)) if m else 10
    p["taille_don"] = taille
    total = {p["moi"]: 0, p["adv"]: 0}
    for t in p["tours"]:
        for proprio, txt, _ in t.lignes:
            if proprio not in total:
                continue
            txt2 = txt.split(": ", 1)[-1] if re.match(rf".+ \[{ID}\]: ", txt) else txt
            if m := re.match(r"Draw (\d+) (?:Rested )?Don$", txt2):
                total[proprio] = min(taille[proprio], total[proprio] + int(m.group(1)))
            elif m := re.match(r"Minus (\d+) Don$", txt2):
                total[proprio] = max(0, total[proprio] - int(m.group(1)))
        t.don = dict(total)


def etat_avant(p, tour):
    """État du board au début du tour = snapshot de fin du tour précédent."""
    i = p["tours"].index(tour)
    return p["tours"][i - 1].etat if i > 0 else {}


def resultat(p):
    # résultat donné par le joueur quand le log ne l'écrit pas (parties/resultats.json : {"<début du nom du log>": "W"|"L"})
    chemin = os.path.join(PARTIES, "resultats.json")
    if os.path.exists(chemin):
        import json
        with open(chemin, encoding="utf-8") as f:
            for cle, val in json.load(f).items():
                if p["fichier"].startswith(cle):
                    return val, "donné par le joueur"
    if p["fin"]:
        qui, quoi = p["fin"]
        moi = qui == p["moi"]
        raison = ("j'abandonne" if moi else "il abandonne") if quoi == "Concedes" else \
                 ("je quitte la partie" if moi else "il quitte la partie")
        return ("L" if moi else "W"), raison
    # sinon : un coup qui touche le Leader d'un joueur déjà à 0 vie, au dernier tour
    if not p["tours"]:
        return "?", "fin non détectée"
    dern = p["tours"][-1]
    avant = etat_avant(p, dern)
    leader_de = {lid: j for j, (_, lid) in p["leaders"].items() if lid}
    vies = {j: avant.get(j, {}).get("Life") for j in leader_de.values()}
    # un tour supplémentaire n'a pas d'état de fin : repartir du dernier état connu, moins les coups reçus depuis
    i = len(p["tours"]) - 1
    for j in vies:
        if vies[j] is None:
            k = i - 1
            while k >= 0 and "Life" not in p["tours"][k].etat.get(j, {}):
                k -= 1
            if k >= 0:
                v = p["tours"][k].etat[j]["Life"]
                for t in p["tours"][k + 1:i]:
                    v -= sum(1 for a in decouper_attaques(t)
                             if leader_de.get(a["cible"][1]) == j and (a["issue"] or "").startswith("touche"))
                vies[j] = v
    attaques = decouper_attaques(dern)
    for a in attaques:
        j = leader_de.get(a["cible"][1])
        if j is None or not (a["issue"] or "").startswith("touche") or vies.get(j) is None:
            continue
        if vies[j] == 0:
            return ("L" if j == p["moi"] else "W"), "dégâts à 0 vie"
        vies[j] -= 1
    if attaques and attaques[-1]["issue"] is None:
        return "?", "le log s'arrête au milieu d'une attaque (déconnexion ou départ, non écrit dans le log)"
    return "?", "fin non détectée"


def rested_au_debut(p, tour, joueur):
    """Persos de `joueur` couchés au début de `tour` (ils ont attaqué ou été couchés au tour précédent).
    Compte par id de carte (deux exemplaires = ambigus)."""
    i = p["tours"].index(tour)
    if i == 0:
        return {}
    prec = p["tours"][i - 1]
    couches = {}
    # Lightning Dragon & co. joués deux tours plus tôt : la cible ne s'est pas relevée à son Refresh
    if i >= 2:
        for _, txt, _ in p["tours"][i - 2].lignes:
            if m := re.match(rf".+ \[{ID}\]: (.+?) \[({ID})\] will not Activate during next Refresh", txt):
                couches[m.group(2)] = couches.get(m.group(2), 0) + 1
    for a in decouper_attaques(prec):
        if a["joueur"] == joueur and a["att"][1] != p["leaders"][joueur][1]:
            couches[a["att"][1]] = couches.get(a["att"][1], 0) + 1
    for proprio, txt, _ in prec.lignes:
        if m := re.match(rf".+ \[{ID}\]: Rest (.+?) \[({ID})\]$", txt):
            couches[m.group(2)] = couches.get(m.group(2), 0) + 1
        if m := re.match(rf".+ \[{ID}\]: Set (.+?) \[({ID})\] to Active", txt):
            couches[m.group(2)] = max(0, couches.get(m.group(2), 0) - 1)
    return couches


def compte_face_clear(p, tour):
    """Données du compte « face ou clear » pour un de MES tours."""
    moi, adv = p["moi"], p["adv"]
    db = base_cartes.charger()
    avant = etat_avant(p, tour)
    vies_adv = avant.get(adv, {}).get("Life")
    main_adv = len(avant.get(adv, {}).get("Hand", []))
    board_adv = avant.get(adv, {}).get("Board", [])
    mon_board = avant.get(moi, {}).get("Board", [])
    couches = rested_au_debut(p, tour, adv)
    blockers, cibles = [], []
    for cid in board_adv:
        c = db.get(cid, {})
        nom = f"{c.get('nom', cid)} [{cid}]"
        if couches.get(cid, 0) > 0:          # couché : attaquable, ne peut pas bloquer
            couches[cid] -= 1
            cibles.append(f"{nom} {c.get('puissance') or '?'}")
        elif c.get("blocker"):
            blockers.append(nom)
    # mes attaquants : leader + persos présents au début du tour + persos Rush posés ce tour
    deployes = [m.group(2) for _, txt, _ in tour.lignes
                if (m := re.match(rf"Deploy (.+?) \[({ID})\]", txt))]
    rush = [cid for cid in deployes if db.get(cid, {}).get("rush")]
    attaquants = [f"Leader {p['leaders'][moi][0]}"] + [f"{nom_carte(c)} [{c}]" for c in mon_board] \
        + [f"{nom_carte(c)} [{c}] (Rush" + (", sous condition" if "gains [Rush]" in db[c]["effet"] else "") + ")"
           for c in rush]
    att = [a for a in decouper_attaques(tour) if a["joueur"] == moi]
    leader_adv = p["leaders"][adv][1]
    cartes_adv = set(board_adv) | {cid for t in p["tours"] for cid in t.etat.get(adv, {}).get("Board", [])}
    kos, neutres = [], []
    for proprio, txt, _ in tour.lignes:
        if proprio != moi:
            continue
        m = re.search(rf": (Destroy|K\.?O\.?|Return|Bottom Deck|Trash) (.+?) \[({ID})\]", txt)
        if m:
            if m.group(3) in cartes_adv:
                kos.append(txt)
            continue
        m = re.search(rf": (?:Rest (.+?) \[({ID})\]|Buff (.+?) \[({ID})\] -\d+)", txt)
        if m and (m.group(2) or m.group(4)) in cartes_adv:
            neutres.append(txt)
    i = p["tours"].index(tour)
    don_prec = p["tours"][i - 1].don.get(moi, 0) if i > 0 else 0
    pioche = 0
    for pr, txt, _ in tour.lignes:
        m = re.match(r"Draw (\d+) Don$", txt)
        if pr == moi and m:
            pioche = int(m.group(1))
            break
    don_debut = min(don_prec + pioche, p.get("taille_don", {}).get(moi, 10))
    return {"vies_adv": vies_adv, "coups_letal": (vies_adv + 1) if vies_adv is not None else None,
            "main_adv": main_adv, "board_adv": board_adv, "blockers": blockers,
            "attaquants": attaquants, "don": tour.don.get(moi),
            "face": [a for a in att if a["cible"][1] == leader_adv],
            "clear": [a for a in att if a["cible"][1] != leader_adv], "retraits": kos, "neutres": neutres,
            "cibles": cibles,
            "don_debut": don_debut}


# ---------------------------------------------------------------- fiche

def nom_l(nom_id, p):
    leaders = {lid for _, lid in p["leaders"].values()}
    return f"{nom_id[0]} (Leader)" if nom_id[1] in leaders else f"{nom_id[0]} [{nom_id[1]}]"


def fmt_attaque(a, p):
    qui = "Moi" if a["joueur"] == p["moi"] else "Adversaire"
    s = f"⚔ {qui} : {nom_l(a['att'], p)} → {nom_l(a['cible'], p)}"
    if a["vs"]:
        s += f" ({a['vs'][0]} vs {a['vs'][1]})"
    det = []
    if a["counters"]:
        det.append("counters " + ", ".join(a["counters"]))
    if a["block"]:
        det.append("bloqué par " + a["block"])
    if a["trigger"]:
        det.append("trigger " + ", ".join(a["trigger"]))
    autres = [x for x in a["autres"] if not x.endswith("Destroyed")]
    if autres:
        det.append("effets : " + " / ".join(autres))
    if det:
        s += " ; " + " ; ".join(det)
    return s + f" → {a['issue'] or '?'}"


def anonymiser(txt, p):
    if p["adv"]:
        txt = txt.replace(p["adv"], "Adversaire").replace(p["adv"].split("#")[0], "Adversaire")
    if p["moi"]:
        txt = txt.replace(p["moi"], "Moi")
    return txt


def ids_noms(ids):
    return ", ".join(f"{nom_carte(c)} [{c}]" for c in ids) or "—"


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "inconnu"


def nom_fiche(p):
    h = p["heure"].strftime("%Y-%m-%d-%H%M") if p["heure"] else "sans-date"
    moi_l = p["leaders"].get(p["moi"], ("?",))[0]
    adv_l = p["leaders"].get(p["adv"], ("?",))[0]
    return f"{h}-{slug(moi_l)}-vs-{slug(adv_l)}.md"


def ecrire_fiche(p):
    moi, adv = p["moi"], p["adv"]
    compter_don(p)
    res, comment = resultat(p)
    moi_l, adv_l = p["leaders"].get(moi, ("?", "?")), p["leaders"].get(adv, ("?", "?"))
    date = p["heure"].strftime("%Y-%m-%d") if p["heure"] else "?"
    o = []
    o.append(f"# Partie {date} — {moi_l[0]} vs {adv_l[0]}\n")
    o.append("> Fiche générée depuis le combat log d'OPTCG Sim (`scripts/fiche_partie.py`). Faits uniquement ; "
             "la main adverse n'apparaît qu'en nombre de cartes (information disponible en partie).\n")
    o.append("## Contexte\n")
    o.append(f"- **Date / heure** : {p['heure'].strftime('%Y-%m-%d %H:%M') if p['heure'] else '?'} (heure locale)")
    o.append(f"- **Mode** : sim en ligne (version {p['version'] or '?'})")
    o.append(f"- **Mon deck** : {moi_l[0]} [{moi_l[1]}] — `decks/{slug(moi_l[0])}.md`")
    o.append(f"- **Deck adverse** : {adv_l[0]} [{adv_l[1]}]")
    o.append(f"- **Qui commence** : {'moi' if p['premier'] == moi else 'lui'}")
    o.append(f"- **Résultat** : {res} ({comment}, {len(p['tours'])} tours)")
    o.append(f"- **Log source** : `parties/logs/{p['fichier']}` (local, non commité)\n")

    o.append("## Mulligan\n")
    o.append(f"- **Main de départ** : {ids_noms(p['main_avant'] or [])}")
    if p["mulligan"].get(moi):
        o.append(f"- **Décision** : mulligan → {ids_noms(p['main_apres'] or [])}")
    else:
        o.append("- **Décision** : keep")
    o.append(f"- **Adversaire** : {'mulligan' if p['mulligan'].get(adv) else 'keep'}\n")

    o.append("## Déroulé tour par tour\n")
    for t in p["tours"]:
        qui = "Moi" if t.joueur == moi else "Adversaire"
        o.append(f"### Tour {t.num} — {qui}" + (" (tour supplémentaire)" if t.bonus else "") + "\n")
        if t.joueur == moi:
            c = compte_face_clear(p, t)
            o.append("- **Compte face ou clear (début de tour)** :")
            if c["vies_adv"] is None:
                o.append("  - vies adverses : pas encore d'état connu (premier tour)")
            else:
                o.append(f"  - vies adverses : {c['vies_adv']} → {c['coups_letal']} coups qui touchent pour le létal")
            o.append(f"  - mes attaquants : {', '.join(c['attaquants'])} ; DON!! sur le terrain : {c['don_debut']}")
            o.append(f"  - sa main : {c['main_adv']} cartes (counters possibles) ; ses Blockers : "
                     f"{', '.join(c['blockers']) or 'aucun'}")
            o.append(f"  - son board : {ids_noms(c['board_adv'])}")
            o.append(f"  - ses persos couchés (seules cibles possibles pour un clear par attaque) : "
                     f"{', '.join(c['cibles']) or 'aucun'}")
            o.append(f"- **Décision** : {len(c['face'])} attaque(s) sur le Leader, {len(c['clear'])} sur ses persos"
                     + (f", {len(c['retraits'])} retrait(s) par effet" if c["retraits"] else "")
                     + (f", {len(c['neutres'])} neutralisation(s) (rest / malus)" if c["neutres"] else ""))
        att = decouper_attaques(t)
        debuts = {a["debut"]: a for a in att}
        pris = set().union(*[a["lignes"] for a in att]) if att else set()
        actions = []
        for i, (proprio, txt, _) in enumerate(t.lignes):
            if i in debuts:
                actions.append("**" + anonymiser(fmt_attaque(debuts[i], p), p) + "**")
                continue
            if i in pris or txt == "End Turn":
                continue
            if txt.startswith("Drew card from deck") and proprio == adv:
                txt = "pioche 1 carte"
            who = "Moi" if proprio == moi else ("Adversaire" if proprio == adv else "—")
            actions.append(f"{who} · {anonymiser(txt, p)}")
        if actions:
            o.append("- **Déroulé** :")
            o.extend(f"  - {a}" for a in actions)
        e = t.etat
        if e:
            em, ea = e.get(moi, {}), e.get(adv, {})
            o.append(f"- **Fin de tour** : vies {em.get('Life', '?')} (moi) / {ea.get('Life', '?')} (adv) ; "
                     f"DON!! {t.don.get(moi)} / {t.don.get(adv)} ; "
                     f"main {len(em.get('Hand', []))} / {len(ea.get('Hand', []))} cartes")
            o.append(f"  - ma main : {ids_noms(em.get('Hand', []))}")
            o.append(f"  - mon board : {ids_noms(em.get('Board', []))}")
            o.append(f"  - son board : {ids_noms(ea.get('Board', []))}")
        o.append("")

    o.append("## Décisions incertaines\n")
    o.append("*(à compléter par le joueur : 1-2 décisions où j'étais vraiment pas sûr)*\n")
    o.append("## Tags provisoires\n")
    o.append("*(le coach complète à l'analyse)*\n")
    return "\n".join(o)


def traiter(chemin, force=False):
    p = parser(chemin)
    if not p["moi"] or not p["adv"] or not p["tours"]:
        return None
    sortie = os.path.join(PARTIES, nom_fiche(p))
    if os.path.exists(sortie) and not force:
        return sortie
    with open(sortie, "w", encoding="utf-8", newline="\n") as f:
        f.write(ecrire_fiche(p))
    return sortie


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("logs", nargs="*")
    ap.add_argument("--tout", action="store_true")
    ap.add_argument("--force", action="store_true", help="réécrire les fiches existantes")
    a = ap.parse_args()
    fichiers = sorted(glob.glob(os.path.join(LOGS, "*.log"))) if a.tout else a.logs
    for f in fichiers:
        r = traiter(f, a.force)
        print(f"{os.path.basename(f)} -> {os.path.relpath(r, RACINE) if r else 'ignoré (partie incomplète)'}")
