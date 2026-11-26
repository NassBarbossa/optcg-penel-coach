"""Base de cartes (anglais) pour les fiches de partie : puissance, counter, Blocker, Rush, texte.

Source : https://github.com/buhbbl/punk-records (dossier english/data, un JSON par extension).
Téléchargée une fois dans data/cache/cartes.json (non commité, voir .gitignore).

    python scripts/cartes.py            # télécharge ou met à jour le cache
"""
import json
import os
import sys
import urllib.request

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(RACINE, "data", "cache", "cartes.json")
BASE = "https://raw.githubusercontent.com/buhbbl/punk-records/main/english/"


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "optcg-penel-coach"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def telecharger():
    packs = _get(BASE + "packs.json")
    cartes = {}
    for pid in packs:
        try:
            liste = _get(f"{BASE}data/{pid}.json")
        except Exception as e:  # une extension manquante ne bloque pas le reste
            print(f"  extension {pid} ignorée : {e}", file=sys.stderr)
            continue
        for c in liste:
            cid = c["id"].split("_")[0]          # OP15-058_p1 -> OP15-058
            if cid in cartes and "_" in c["id"]:
                continue                          # garder la version de base
            effet = c.get("effect") or ""
            cartes[cid] = {
                "nom": c.get("name"),
                "type": c.get("category"),
                "cout": c.get("cost"),
                "puissance": c.get("power"),
                "counter": c.get("counter"),
                "blocker": "[Blocker]" in effet,
                "rush": "[Rush]" in effet,
                "trigger": c.get("trigger"),
                "effet": effet,
            }
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "w", encoding="utf-8") as f:
        json.dump(cartes, f, ensure_ascii=False)
    return cartes


_CARTES = None


def charger(auto=True):
    """Renvoie {id: infos}. Télécharge le cache s'il n'existe pas (auto=True)."""
    global _CARTES
    if _CARTES is None:
        if os.path.exists(CACHE):
            with open(CACHE, encoding="utf-8") as f:
                _CARTES = json.load(f)
        elif auto:
            try:
                _CARTES = telecharger()
            except Exception as e:
                print(f"Base de cartes indisponible ({e}) : fiches sans Blocker/counter.", file=sys.stderr)
                _CARTES = {}
        else:
            _CARTES = {}
    return _CARTES


if __name__ == "__main__":
    n = len(telecharger())
    print(f"{n} cartes dans {CACHE}")
