# Scripts : combat logs OPTCG Sim → fiches de partie

Python 3.8+, bibliothèque standard uniquement.

| Commande | Effet |
|---|---|
| `python scripts/sync_logs.py` | Copie les parties terminées pas encore importées vers `parties/logs/` et crée leur fiche dans `parties/` |
| `python scripts/sync_logs.py --watch` | Idem, puis surveille le dossier du sim (toutes les 5 s) et importe chaque partie dès qu'elle se termine. Ctrl+C pour arrêter |
| `python scripts/fiche_partie.py --tout --force` | Régénère toutes les fiches (après une amélioration du script) |
| `python scripts/cartes.py` | Met à jour la base de cartes (puissance, counter, Blocker, Rush) |

## Où sont les logs du sim

`<dossier du sim>/Builds_Windows/CombatLogs/AutoSaved/`. Le script cherche tout seul dans `Téléchargements`, `Bureau`, `Program Files` et `Games`. Si le sim est ailleurs : `--source "D:/chemin/CombatLogs"` ou la variable d'environnement `OPTCG_COMBATLOGS`.

Le dossier du sim n'est jamais modifié. Le sim n'y garde qu'une centaine de parties et ses mises à jour le vident : c'est pour ça qu'on copie tout.

## Format du log (relevé le 2026-11-26, version 1.45b)

- Un fichier par partie : `AAAA-MM-JJTHH.MM.SS.xxxxxxx-<id>.log`, heure UTC du début de partie. Pendant la partie, le fichier s'appelle `*.partial.log` : il est ignoré jusqu'à ce que la partie se termine.
- Lignes `RZ1|...` : encodage machine non documenté, ignoré.
- Lignes `CHAT|<base64>` : messages du chat, ignorés (ils peuvent contenir des pseudos).
- Lignes lisibles : `[Pseudo] action`, avec les cartes en `Nom [OP15-058]`. Leaders, qui commence, mains avant et après mulligan (les miennes), pioches, `Deploy`, effets, `Attach N Don`, attaques (`A attacking B`, counters, `Blocks`, `Activate Trigger`, `A [p] vs B [p]`, `hit for 1 damage` / `Attack Fails` / `Destroyed`), `End Turn`, et un état complet à chaque fin de tour (`Hand`, `Board`, `Trash`, `Life` des deux joueurs).
- Fin : `Concedes!`, `Quits!`, ou rien du tout (le dernier coup sur un Leader à 0 vie, ou un log coupé par un départ).

## Ce que la fiche garde et ne garde pas

- Pseudos remplacés par « Moi » et « Adversaire ». Les logs bruts ne sont jamais commités (`.gitignore`).
- La main adverse et ses pioches sont **en clair** dans le log : la fiche n'en garde que le nombre de cartes, pour évaluer chaque décision avec l'information réellement disponible.
- Approximations : DON!! sur le terrain (le paiement des coûts n'est pas écrit), statut couché des persos (reconstitué à partir des attaques et des effets), Rush sous condition.

Base de cartes : [buhbbl/punk-records](https://github.com/buhbbl/punk-records), téléchargée dans `data/cache/` (non commitée).
