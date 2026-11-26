# Analyse 2026-11-26 — session ladder Enel violet, 6 parties (0 W confirmée, 4 L, 2 inconnues)

## Contexte

- **Source** : combat logs d'OPTCG Sim, importés automatiquement (`scripts/sync_logs.py`). Fiches : `parties/2026-11-26-*.md`. Aucune partie racontée par le joueur.
- **Parties** :

| Heure | Adversaire | Qui commence | Résultat |
|---|---|---|---|
| 08:07 | Gunko | moi | L (abandon T9) |
| 08:19 | Karoo (Alabasta) | lui | L |
| 08:33 | RP Luffy (ST10) | moi | ? : le log s'arrête pendant mon attaque létale (adversaire à 0 vie) |
| 08:43 | Gunko | lui | L |
| 08:58 | Spandam | moi | ? : le log s'arrête pendant ma 4e attaque (adversaire à 0 vie) |
| 09:06 | Franky (Water Seven) | lui | L (abandon T10) |

- **Faiblesse travaillée** (demandée par le joueur) : les décisions **face ou clear** à chaque tour.
- **Méthode du compte**, à chaque tour où j'attaque :
  - **létal** : vies adverses + 1 coups qui touchent, comparés au nombre de mes attaquants ;
  - **défense adverse** : ses cartes en main (counters possibles) et ses Blockers actifs ;
  - **cibles d'un clear** : ses persos **couchés**, les seuls qu'une attaque peut viser.
- **Limites des données** :
  - la valeur des counters adverses est inconnue au moment T (seul le nombre de cartes l'est) ;
  - le statut couché est reconstitué (attaques, effets Rest, Lightning Dragon) ;
  - le DON!! est approximatif : le log n'écrit pas le DON!! payé pour jouer une carte.
- **Liste jouée** : la liste réelle du joueur (Law ×3, Killingham ×2), intégrée dans `decks/enel.md` le jour même.

## Décisions clés (évaluées au moment T)

Légende : ✅ bonne avec l'info disponible · ⚠️ défendable, à discuter · ❌ mauvaise avec l'info disponible.

### 08:07 — Gunko (moi premier, L)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T3 | 4 vies → 5 coups ; 3 attaquants (Leader, Pudding, Shura Rush) ; 6 cartes ; 0 Blocker ; 0 perso couché | El Thor sur Saint Gunko (le chercheur), puis 3 attaques face, 1 touche | ✅ Le létal est impossible et aucun perso n'est attaquable : le clear ne peut passer que par un effet. Tuer le chercheur tout de suite, c'est la règle du pro contre Gunko. Les 3 attaques face lui coûtent 2 counters pour 1 carte reçue. |
| T5 | 3 vies → 4 coups ; 3 attaquants ; 6 cartes ; Blocker Sleeptids ; 0 couché | Leader face à 5000 (Cerberus 2000 dépensé), Pudding face (Sleeptids bloque et meurt) | ✅ Lui faire dépenser Cerberus en counter retire une pièce de son combo. Shura n'attaque pas (2000 contre 5000) : correct. |
| T7 | 3 vies → 4 coups ; 2 attaquants ; 7 cartes, puis 5 après Law (Killingham + Shamrock défaussés) ; 0 Blocker ; couché : Killingham 6000 | El Thor sur Saint Gunko, puis Leader et Enel face, 2 coups qui touchent (3 → 1) | ✅ Killingham revient du cimetière quand il est K.O. : contre Gunko, le clear sur ses persos récursifs ne retire rien. La course est le bon plan. |
| T9 | 1 vie → 2 coups ; **3 attaquants** (Leader, Enel 6c, Pudding) ; 7 cartes ; 0 Blocker ; couchés : Killingham, Sommers | El Thor sur Saint Gunko, Leader face à 9000 contré (+5000)… puis **abandon** | ❌ **Deux attaquants n'ont jamais attaqué**, dont Enel à 10 000. Il lui restait 5 cartes après ses 2 counters : le létal était improbable mais pas impossible, et une attaque ne coûtait rien. On n'abandonne pas tant qu'il reste une attaque à déclarer. |

### 08:19 — Karoo (lui premier, L)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T2 | 4 vies ; Leader seul (0 DON!! après Satori) ; 5 cartes ; 0 couché | Aucune attaque | ⚠️ Leader 5000 contre Leader 5000 : l'attaque touche sans counter. Elle forçait une carte ou donnait une carte. Même schéma au 2e Gunko : voir la question au joueur plus bas. |
| T4 | 4 vies → 5 coups ; Leader, Satori, Shura ; 5 cartes ; Blocker Vivi OP18-011 (+6000 pendant mon tour) ; 0 couché | Satori face (touche), Leader face (bloqué par Vivi et 2 counters), puis Lightning Dragon sur Vivi | ✅ Lightning Dragon sur le Blocker qui vient de bloquer : elle reste couchée deux tours. Bon réflexe. |
| T6 | 3 vies → 4 coups ; Leader, Shura ; 5 cartes ; 0 Blocker actif ; couchés : Igaram 2000, Vivi, Pell 6000 | Shura sur Pell (contré), Leader sur Igaram (K.O.), Lightning Dragon sur Pell | ✅ Contre un deck aggro Rush, létal hors de portée : on tape ses attaquants couchés. Bon tour. |
| T8 | 3 vies → 4 coups ; **2 attaquants** (Leader, Enel 6c) ; 5 cartes ; Blockers Vivi ×2 (EB03 retirée par Kiten + El Thor) ; **couchés : 2 Pell 6000 (Rush), Vivi 2000** | Leader et Enel **face**, 2 coups qui touchent (3 → 1) | ❌ **Le tournant de la partie.** 4 coups étaient nécessaires pour 2 attaquants : pas de létal ce tour, et à 1 vie il en faut encore 2 au tour suivant à travers 2 Blockers. Ces 2 attaques face lui ont donné 2 cartes (main de 5 → 8). Ses 2 Pell couchés sont restés en vie et ont attaqué au tour suivant : ils m'ont coûté 2 vies et 4 cartes défensives. Enel 14 000 sur un Pell (8000 de counters pour le sauver) et Leader 7000 sur l'autre (2000 pour le sauver) retiraient deux attaquants. |
| T10 | 1 vie → 2 coups ; 4 attaquants ; 5 cartes après Law ; Blockers Vivi ×2 ; couchés : 2 Pell, Karoo 7000 ; moi : 2 vies, 2 cartes en main | 3 attaques face (Shura contré, Leader bloqué, Enel bloqué : K.O. de Vivi), puis Enel sur Karoo 7000 | ✅ Bon séquençage. Une fois les 2 Blockers et un counter dépensés, le létal ne pouvait plus arriver avec une seule attaque. La dernière attaque est passée en défense sur son plus gros attaquant. La partie s'était perdue au T8. |

### 08:33 — RP Luffy (moi premier, ?)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T3 | 3 vies → 4 coups ; Leader, Satori ; 6 cartes ; 0 couché | Satori face (contré par Yamato), Leader face à 6000 (touche) | ✅ Pas de cible et pas de létal ; Leader Luffy à 6000, donc attaquer à 6 force un counter ou un coup. |
| T5 | 2 vies → 3 coups ; DON!! limité ; Blocker Yamato | El Thor sur Yamato (Blocker), Satori face à 8000 (contré) | ✅ |
| T7 | 2 vies → 3 coups ; 6 attaquants, mais seulement 6 DON!! ; 5 cartes ; Zoro 9000 actif (+2000 au Leader) | Gamma Knife et Mamaragan couchent Zoro, Leader le tue ; Enel face (touche, 2 → 1) ; Satori face ×2 | ✅ « Gamma Knife pour Zoro » (règle du pro). Clear de la menace, puis pression avec le reste. |
| T9 | 1 vie → 2 coups ; 5 cartes ; 0 Blocker ; Roger 10 000 actif ; **adversaire à 10 DON!!** | Gamma Knife + Mamaragan + Leader sur Roger, El Thor sur Nami, Enel face (touche, 1 → 0) ; Satori face contré | ⚠️ Le clear de Roger est solide : 10 000 power, plus 2000 sur son Leader. Mais l'information clé était là : **10 DON!! en face**, c'est-à-dire la sortie Luffy OP05-119 (tour supplémentaire), « la seule défaite du pro ». La question à se poser avant ce tour : « mettre à 0 ou tenter les 2 coups maintenant ? » Elle a coûté 3 vies au tour suivant (2 → 1 avec Reiju perdue). Pas clairement fautif : les cartes de clear ont aussi enlevé ses attaquants. |
| T12 | 0 vie → 1 coup ; Enel avec 6 DON!! | Enel face ; contré par Gum Gum Giant + Mamaragan… le log s'arrête | ✅ Ligne correcte. Résultat non écrit dans le log. |

### 08:43 — Gunko (lui premier, L)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T2 | 4 vies ; Leader + Shura ; 0 DON!! après Shura + Ohm ; 5 cartes | Aucune attaque | ⚠️ Même schéma qu'au T2 contre Karoo (Leader 5000 contre 5000 non utilisé). |
| T4 | 4 vies → 5 coups ; Leader, Shura, Ohm ; 6 cartes ; 0 couché | Shura et Leader face, contrés (Sleeptids 2000, Sommers 2000) | ⚠️ Pas d'alternative de clear. Mais contre Gunko, ses counters partent au **cimetière, d'où il rejoue Sleeptids et Sommers** (Killingham, I'll Summon Them). Le faire contrer nourrit son moteur. À garder en tête, sans trancher. |
| T6 | 4 vies → 5 coups ; 6 cartes ; Blocker Sleeptids | El Thor sur Sleeptids, Satori face (contré), Leader face (touche, 4 → 3) | ✅ |
| T8 | 3 vies → 4 coups ; Leader, Shura, Ohm, Enel ; 6 cartes, puis 4 après Law (I'll Summon Them + Shamrock) ; couché : Killingham | Enel face (touche), Ohm sur Killingham (K.O. : il paie 2 cartes pour le rejouer), Leader face (contré +4000) | ✅ Bon tour : Law vide sa main, et le K.O. de Killingham le force à défausser 2 cartes. |
| T10 | 2 vies → 3 coups ; 3 attaquants ; 4 cartes ; couchés : Sommers, Killingham, Shamrock 9000 ; moi : 2 vies | Leader face (contré), Shura face (touche, 2 → 1), Enel sur Shamrock (K.O.) | ✅ 3 coups pour 3 attaquants : il suffit d'un counter pour arrêter le létal. Mettre Enel sur Shamrock (le Rush imblocable avec Cerberus) est la seule ligne défensive (« ne pas aller à 0 face à Shamrock + Cerberus »). Shamrock revient du cimetière, mais ça lui coûte une carte. |

### 08:58 — Spandam (moi premier, ?)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T3 | 4 vies → 5 coups ; Leader, Shura ; 6 cartes ; 0 couché | Shura face (contré), Leader face (touche, **Trigger** Charlotte Pudding) | ⚠️ Au T2, les Lilith montraient déjà un deck de Triggers. Taper tôt dans un deck de Triggers, c'est payer en Triggers. Ici il n'y avait pas de cible : acceptable. |
| T5 | 3 vies → 4 coups ; Leader, Pudding ; **8 cartes** ; couché : Lilith 2000 | Pudding et Leader face, tous deux contrés (2 cartes dépensées) | ⚠️ Avec 8 cartes en face, les attaques face sont contrées à coup sûr. Le Leader sur la Lilith couchée retirait un attaquant qui tue mes 1-drops. Les deux lignes se défendent (2 counters dépensés, ce n'est pas rien). |
| T7 | 4 vies (il a rajouté une vie) → 5 coups ; Leader, Enel ; 7 cartes ; couchés : Lilith, Pudding 4000 | Lightning Dragon sur Pudding, Leader et Enel face (4 → 2) | ✅ Spandam remet une vie chaque tour : la partie longue est à lui, donc je suis le beatdown. Ses persos sont petits et ne menacent pas Enel. |
| T9 | 3 vies → 4 coups ; **4 attaquants** (Leader, Enel ×2, Shura Rush) ; 6 cartes après Law ; Blocker Fukurou | 4 attaques face : 3 touchent (3 Triggers), la 4e prend 4 counters… le log s'arrête | ✅ 4 coups pour 4 attaquants avec un Blocker en face : le létal dépendait de sa défense. Mais le mettre à 0 en vidant sa main était la bonne pression. |

### 09:06 — Franky (lui premier, L)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T2 | 4 vies ; Leader, Shura ; 0 DON!! ; Shark Submerge (+1000 au Leader en défense) | Aucune attaque | ✅ 5000 contre 6000 avec Shark Submerge : l'attaque ne pouvait pas toucher. |
| T4 | 4 vies → 5 coups ; Leader, Shura | Leader à 5000 d'abord (Shark se couche pour le contrer), puis Shura à 8000 (touche) | ✅ Excellent séquençage : l'attaque du Leader sert d'appât pour coucher Shark Submerge. |
| T6 | 3 vies → 4 coups ; Leader, Pudding ; 7 cartes | Pudding à 6000 (touche), Leader à 6000 (Mini-Merry 3000) | ✅ « Attaquer à 6 contre Franky » : chaque attaque force un 3k ou touche. |
| T8 | 2 vies → 3 coups ; 2 attaquants ; 6 cartes ; Blocker Franky Family ; 0 couché | Leader face (Mini-Merry), Enel 14 000 face (touche, 2 → 1) | ✅ Aucune cible attaquable et pas de létal. Enel à 14 000 est un coup quasi gratuit, et il prépare le létal à 2 coups. Le pro conseille de retirer le Franky Family : c'était possible par effet (El Thor ou Gamma Knife en main), à considérer. |
| T10 | 1 vie → 2 coups ; Leader + Enel (le 2e Enel bloqué par l'effet de Luffy) ; 6 cartes ; Franky Family couché par Mamaragan | Kiten, Mamaragan, El Thor ×3, Enel face (touche, 1 → 0), Leader à 10 000 (2 Mini-Merry) → abandon | ✅ Toutes les attaques utilisées et le Blocker neutralisé avant d'attaquer. Avec 6 cartes en face, l'abandon après la dernière attaque est logique. |

## Lignes alternatives

1. **Karoo T8** (le coût le plus élevé de la session). Au lieu de Leader + Enel face :
   - Kiten + El Thor sur Vivi EB03, comme joué ;
   - **Enel 14 000 sur Pell n°1** : il faut 8000 de counters pour le sauver ;
   - **Leader 7000 sur Pell n°2** : il faut 2000 pour le sauver.

   Résultat attendu : au tour suivant, il attaque avec son Leader, Karoo (s'il le joue) et peut-être Vivi, au lieu de Leader + 2 Pell + Karoo. Il reste à 3 vies avec 5 cartes au lieu de 8. Mon Enel et mes Blockers tiennent la partie longue, qui est celle du deck contrôle.
2. **Gunko n°1, T9**. Faire toutes les attaques avant de décider d'abandonner. Ordre pour le létal à 2 coups : d'abord la plus petite attaque qui demande un counter (Pudding avec DON!!), puis le Leader, et Enel à 10 000 en dernier. Il doit garder le plus gros counter pour la fin.
3. **RP Luffy T9**. Avant d'attaquer, vérifier le DON!! adverse. À 10 DON!!, le Luffy OP05-119 est en jeu. Comparer explicitement :
   - (a) mettre à 0 et clear (joué) ;
   - (b) tenter les 2 coups ce tour.

   Le joueur doit pouvoir dire pourquoi il a choisi (a).

## Part de variance

- **Gunko ×2** : le pire matchup selon le pro, et la récursion rend les clears peu rentables. Les deux défaites viennent surtout de leur combo (Shamrock + Cerberus + Luffy tour supplémentaire). Une seule décision clairement fautive : l'abandon prématuré du T9.
- **Karoo** : défaite majoritairement **décisionnelle** (T8), pas de la variance.
- **Franky** : défaite surtout due à la bombe du T9 adverse (Luffy Rush + Tom + Nami + White Hobby Horse, 5 attaques). Les décisions face ou clear étaient bonnes. Classée « expected variance » pour ce qui est du face ou clear.
- **RP Luffy, Spandam** : résultat inconnu (log coupé avec l'adversaire à 0 vie). Les décisions étaient bonnes ou défendables.

## Tags : `role` `attack-economy` `lethal`

- `role` + `attack-economy` : Karoo T8 (face au lieu de clear contre un aggro, sans létal possible).
- `lethal` : Gunko T9 (abandon avec 2 attaques non déclarées).
- À surveiller, `attack-economy` : Leader non utilisé au T2 en second joueur (Karoo, Gunko n°2).

**Bilan face ou clear sur la session** : 28 tours d'attaque évalués, 20 ✅, 6 ⚠️, 2 ❌.

Le joueur choisit bien le clear **quand il a un effet de removal en main** (El Thor sur les chercheurs et les Blockers, Gamma Knife sur Zoro et Roger). Il oublie le clear **par attaque** sur les persos couchés quand le létal est hors de portée.

## Faiblesse prioritaire → changement testable

**Faiblesse** : quand le létal est impossible ce tour, attaquer la face par défaut au lieu de vérifier s'il y a des attaquants adverses couchés à tuer.

**Changement testable, sur les 10 prochaines parties** : avant chaque phase d'attaque, dire à voix haute ou écrire le compte :

1. « Il lui faut **X** coups (vies + 1), j'ai **Y** attaquants, il a **Z** cartes et **B** Blockers. »
2. Si Y < X (pas de létal) et qu'il a au moins un perso **couché qui m'attaquera au prochain tour** : **au moins une attaque va sur ce perso avant toute attaque face**. Exception : un perso qui revient du cimetière (Gunko).
3. On n'abandonne **jamais** tant qu'il reste une attaque à déclarer.

**Mesure** : la prochaine analyse compte, dans les fiches générées, les tours « pas de létal + perso couché disponible ». Elle vérifie qu'au moins une attaque y est allée. Objectif : 100 % sur 10 parties.

**Drill (ch. 5.1)** : en solo contre soi-même sur le sim, recréer la position Karoo T8 (2 Pell couchés, 2 Vivi, 3 vies en face, mes 2 attaquants). La jouer 5 fois avec des mains adverses différentes, en comparant face et clear sur les deux tours suivants.

**Question au joueur (ch. 9.3)** : au T2 en second joueur (Karoo, Gunko n°2), le Leader n'a pas attaqué alors que 5000 contre 5000 touche sans counter. C'était voulu (ne pas donner de carte) ou un oubli ? Déroule ton raisonnement avant que je donne le mien.
