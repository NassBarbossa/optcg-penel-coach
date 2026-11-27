# Analyse 2026-11-27 : session 4 (26/11 18:32 → 27/11 07:06), Enel, face ou clear

## Contexte

- Suite du rapport de session 3 (`2026-11-26-enel-session-3-face-ou-clear.md`).
- Faiblesse travaillée : **face ou clear**, avec les deux réflexes à installer depuis la session 3 :
  - en fin de tour, vérifier qu'aucun perso n'a gardé son attaque alors qu'une cible couchée et faible est là ;
  - contre les counters qui couchent un perso, faire attaquer les petits persos d'abord.
- Trois blocs : 18:32 → 18:53 (4 parties), 22:27 → 23:38 (6 parties), puis 07:06 le 27/11 (1 partie).
- Bilan : **5 W, 5 L, 1 inconnu**.

| Heure | Adversaire | Commence | Résultat |
|---|---|---|---|
| 18:32 | Gunko | lui | W (il abandonne au T7) |
| 18:36 | Luffy [OP18-022] | moi | L (T10) |
| 18:44 | Luffy [OP18-022] | moi | inconnu (le log s'arrête pendant ma dernière attaque, adversaire à 0 vie) |
| 18:53 | Luffy [OP18-022] | lui | L (j'abandonne au T10, après toutes mes attaques) |
| 22:27 | Gunko | moi | W |
| 22:42 | RP Luffy [ST10-002] | moi | W (l'adversaire se déconnecte au T9) |
| 22:52 | Luffy [OP13-001] | moi | W |
| 23:13 | Spandam | moi | L (j'abandonne au T13) |
| 23:27 | Karoo | moi | L (j'abandonne au T10) |
| 23:38 | Sabo | moi | W |
| 07:06 (27/11) | Gunko | moi | L (j'abandonne au T11) |

- Les résultats de 22:27, 22:42, 22:52 et 23:38 viennent des fichiers de résultats du simulateur.
- **Textes des cartes adverses** cités plus bas : lus dans la base de cartes du projet (`data/cache/cartes.json`, celle de `scripts/cartes.py`). Ils ne sont pas encore dans `knowledge/` : voir « Repères ajoutés ».
- **Limites** : DON!! approximatif, statut couché reconstitué, counters inconnus avant d'être joués. Deux limites de plus vues cette session :
  1. la fiche compte comme attaquants des persos qui ne peuvent pas attaquer (Killingham adverse, effet « ne peut pas être couché » de Zoro & Sogeking et du Luffy OP18-118). Je les ai retirés du compte ;
  2. la power des persos couchés est la power imprimée. Avec Vivi en jeu, les Karoo étaient plus gros que ce que dit la fiche.

## Les deux réflexes de la session 3

### Réflexe 1 : aucune attaque gardée face à une cible couchée et faible

14 tours sans létal possible avec une cible couchée attaquable (hors Gunko, hors cible déjà gelée) :

| | Appliqué ✅ | À moitié ⚠️ | Pas appliqué ❌ |
|---|---|---|---|
| Bloc 18:32 → 18:53 | 1 | 1 | 0 |
| Bloc 22:27 → 23:38 | 5 | 3 | 4 |
| **Total** | **6** | **4** | **4** |

Les 4 ❌ ont un point commun : la cible est un petit perso à 2000 qui tue un de mes 1-drops chaque tour (Nami EB02-017, Usopp OP17-080), ou le plus petit attaquant de Karoo. La cible est pourtant écrite dans le compte. Le problème vient du moment de la vérification : elle est prévue **en fin de tour**, et à ce moment les attaques sont déjà parties face.

**Verdict : pas encore installé (6 sur 14).**

### Réflexe 2 : les petits persos d'abord contre les counters qui couchent

- Aucun Slow-Slow Beam Sword joué en counter cette session (une copie défaussée par Gunko à 07:06, T4).
- Contre Gunko, l'ordre est bon à chaque fois, petit perso puis Leader : 22:27 T3 et T9 ; 07:06 T3, T5 et T7. **5 sur 5.**
- Contre Spandam, la logique n'a pas été étendue aux **Triggers** qui retirent un perso (Kalifa, Fukurou, Rob Lucci, Jabra). Deux fois, le Leader a attaqué avant un perso qui n'avait pas encore attaqué, et le Trigger a retiré ce perso (T7 Law, T13 Killingham). C'est la règle de la session 2 : « les triggers visent les persos ».

**Verdict : installé contre les counters de Gunko, pas encore étendu aux Triggers.**

## Ce qui a changé depuis la session 3

**Les tours de létal sont bien ordonnés.**

| Partie | Tour | Ordre |
|---|---|---|
| Gunko 22:27 | T9 | Shura et Leader absorbent ses deux counters, les deux Enel touchent |
| RP Luffy | T7 | Pudding, qui ne pouvait pas toucher un Leader à 6000, tue Bonney ; les autres vont face (2 → 0) |
| Luffy OP13-001 | T11 | Satori et le Leader vident ses DON!! de défense, Senor Pink puis Enel touchent (2 → 0) |
| Sabo | T9 | Blocker Jinbe couché, Reiju d'abord (3 counters), Leader, Enel en dernier |

**Les moteurs adverses sont ciblés**, comme le demande le pro :
- Saint Gunko (22:27 T5, 07:06 T5) ;
- Zoro & Sogeking avec Gamma Knife + El Thor (18:44 T9, 18:53 T8) ;
- Sanji (22:52 T9), Ripley (22:27 T7, 23:38 T7), Vivi (23:27).

**Law** prend les bonnes cartes : Sanji + Zoro & Sogeking (18:36 T5), deux Shamrock (22:27 T9), Sleeptids + Shamrock (07:06 T5).

## Décisions clés (évaluées au moment T)

| Partie | Tour | Compte | Décision | Verdict |
|---|---|---|---|---|
| Luffy 18:36 | T9 | 2 vies → 3 coups ; Leader, Enel, Pudding, Shura ×2, Ohm ; 4 cartes ; 0 Blocker ; moi à 1 vie ; il sera à 10 DON!! au tour suivant | Gamma Knife + El Thor ×2 sur Nico Robin ; Pudding 7000 (touche), Leader 6000 (contré), Enel 13 000 (touche) : 2 → 0 ; Shura ×2 et Ohm n'attaquent pas | ⚠️ À 1 vie contre un Leader qui attaque deux fois par tour, avec 10 DON!! à venir, ce tour devait être le létal. Robin OP18-031 n'est pas un Blocker : elle protège ses persos de mes effets et redresse son Leader à la fin de **son** tour. La tuer n'aidait ni le létal ni ma défense (Luffy était déjà redressé). Les 3 cartes et les DON!! dépensés pour elle pouvaient donner une ou deux attaques de plus à 5000, chacune demandant un counter. Dépend du DON!! (approximatif). |
| Luffy 18:53 | T8 | 3 vies → 4 coups ; Leader, Law (Enel ne peut pas être couché) ; 4 cartes ; couchée : Nami EB02-017 2000 ; moi à 3 vies | Gamma Knife + El Thor sur Zoro & Sogeking ; Leader face (contré) ; **Law n'attaque pas** | ⚠️ Garder Law en Blocker à 3 vies contre un Leader à Double Attack se défend. Mais au T9, Law n'a pas bloqué la Double Attack (2 dégâts) : voir les questions. |
| Gunko 22:27 | T3 | 4 vies → 5 coups ; Leader, Shura ; 6 cartes ; Saint Gunko [OP18-084] debout | Shura et Leader face, tous deux contrés | ⚠️ « Tuer le chercheur dès qu'il arrive » (pro). Debout, il ne se retire que par effet : Mamaragan pouvait le coucher pour que Shura le tue. Dépend du DON!! (approximatif). Tué au T5 par le Leader, dès qu'il était couché. |
| Luffy OP13-001 | T5 | 3 vies → 4 coups ; Leader, Ohm, Ohm ; 6 cartes ; Blocker Nami OP14-031 ; couchée : Nami EB02-017 2000 | Ohm face (−1000 sur le Blocker, absorbé par ses DON!!), Leader face (absorbé) ; **le 2e Ohm n'attaque pas** | ❌ Pas de létal. Nami EB02-017 venait de tuer Shura. Ohm à 2000 contre 2000 la tue ; si le Blocker (mis à 1000 par le premier Ohm) s'interpose, c'est lui qui meurt. C'est le cas exact du réflexe 1. |
| Luffy OP13-001 | T7 | 3 vies → 4 coups ; Leader, Ohm, Reiju ; 6 cartes ; couchées : Nami EB02-017 2000, Nami OP14-031 2000 | El Thor tue une Nami OP14-031, Lightning Dragon gèle l'autre ; Reiju et Leader face (absorbés par ses DON!!) ; Ohm sur la Nami OP14-031 **déjà gelée** (sauvée par Sanji) | ⚠️ Une attaque est bien allée sur un perso, mais sur la cible déjà neutralisée. Nami EB02-017, celle qui tue les 1-drops, restait libre. |
| Luffy OP13-001 | T9 | 3 vies → 4 coups ; Leader, Reiju, Enel ; 4 cartes ; couchées : 2 Nami à 2000 | Gamma Knife + El Thor sur Sanji ; 3 attaques face, 1 touche | ❌ 3 attaquants pour 4 coups : pas de létal. Tuer Sanji suit la règle du pro. Mais aucune attaque sur les deux Nami couchées. Son Leader peut aussi protéger une Nami avec ses DON!!, donc le K.O. n'était pas garanti ; il lui demandait pourtant la même dépense que l'attaque face. |
| Spandam | T7 | 3 vies → 4 coups ; Leader, Ohm, Law ; 5 cartes | Ohm face (Trigger Fukurou : Reiju détruite) ; El Thor (+1000 sur Law, K.O. d'Ahiru) ; Leader face (Trigger Rob Lucci : **Law renvoyée sous le deck avant d'attaquer**) | ❌ **Ordre.** Fukurou venait de détruire Reiju dans ce même tour, et Kalifa avait couché Law au T5. Les Triggers de Spandam visent les persos. Law, buffée par El Thor, devait attaquer avant le Leader. |
| Spandam | T13 | 4 vies → 5 coups ; Leader, Killingham n°1 ; 6 cartes ; moi à 4 vies avec 6 cartes en main | Killingham n°2 gèle ses deux Sweet 3 Generals ; Leader face (Trigger Jabra : Killingham n°1 sous le deck) ; **abandon** | ❌ Abandon à 4 vies contre 4, avec 2 Mamaragan, El Thor, Gamma Knife et Reiju en main, et deux de ses attaquants gelés. Même ordre fautif qu'au T7, sur un Killingham qui pouvait encore attaquer. Si tu as arrêté pour une autre raison (heure, fatigue), ignore la partie « abandon ». |
| Karoo | T3 | 4 vies → 5 coups ; Leader, Shura ; 5 cartes ; Blocker Vivi | Kiten −1000 et Mamaragan sur Vivi, Shura l'attaque (contré), Lightning Dragon la gèle ; **le Leader n'attaque pas** | ⚠️ Le Leader à 5000 pouvait finir Vivi (5000 après Kiten) ou aller face à égalité. Une attaque gratuite non déclarée, alors qu'une cible couchée était là. |
| Karoo | T5 | 4 vies → 5 coups ; Leader, Satori, Shura ; 4 cartes ; couchés : Vivi (gelée), Karoo OP18-004 | Satori et Leader sur Vivi (2 counters dépensés), Lightning Dragon la regèle | ✅ Vivi est son moteur : +1000 à ses Karoo, Blocker et +6000 pendant mon tour. Le Karoo OP18-004, affiché à 4000, était en fait à 6000 (il attaquait à 7000 avec 1 DON!! au T4, avec Banish). Il finit à 2 cartes en main. |
| Karoo | T9 | 4 vies → 5 coups ; Leader, Shura, Senor Pink ; 1 carte ; couchés : Karoo OP18-004 (5000 réels après la mort de Vivi), 2 Karoo EB02-001 ; **moi à 1 vie** | Gamma Knife + El Thor sur la nouvelle Vivi ; Kiten −1000 sur un EB02 ; Shura 6000 puis Leader 7000 sur ce même EB02 (échouent) ; **Senor Pink face** (4 → 3) | ❌ **Le plus coûteux de la session.** À 1 vie contre un deck aggro, sans létal possible (3 attaquants pour 5 coups). Senor Pink à 6000 tuait le Karoo OP18-004 sauf counter de 2000, avec la seule carte qu'il avait. L'attaque face lui a donné une carte et n'a rien retiré à son tour suivant. Shura à 6000 contre un EB02 à 7000 ne pouvait pas réussir non plus. |
| Sabo | T5 | 3 vies → 4 coups ; Leader, Ohm ; **9 cartes** ; couché : Usopp OP17-080 2000 | Ohm face (−1000 sur Usopp, contré), Leader face (contré) | ❌ Le cas exact de Ms. All Sunday T7 en session 3. Contre 9 cartes, pas de létal et des attaques face contrées à coup sûr. Usopp venait de tuer Satori ; Ohm sur lui le tuait, son propre effet le mettait même à 1000. |
| Sabo | T7 | 3 vies → 4 coups ; Leader, Enel ; 5 cartes ; Blocker Jinbe ; couchés : 2 Usopp à 2000 | Mamaragan, Gamma Knife et El Thor sur Ripley ; Lightning Dragon gèle un Usopp ; Leader et Enel face (3 → 1) | ⚠️ Ripley ramène un perso du cimetière : bonne cible. Mais le 2e Usopp restait libre, avec moi à 2 vies. Leader sur cet Usopp, Enel face. |
| Gunko 07:06 | T9 | 1 vie → 2 coups ; Leader seul (les 2 Law gelées par Killingham) ; 5 cartes ; couché : Sommers 6000 | Gamma Knife, Mamaragan et Lightning Dragon sur Shamrock ; El Thor sur Saint Gunko ; Leader face (2 counters) | ✅ Un seul attaquant, pas de létal. Sommers revient du cimetière : le coup face qui lui coûte 2 cartes vaut autant. Trois cartes pour geler Shamrock un tour, c'est cher. |
| Gunko 07:06 | T11 | 1 vie → 2 coups ; Leader seul (Law ×2 gelées, Senor Pink posé ce tour) ; 4 cartes ; **Blocker Saint Gunko OP18-065 à 11 000** | Senor Pink ; El Thor en Main (+1000, aucune cible à 3000 ou moins) ; Leader 9000 bloqué ; **abandon** | ⚠️ Un attaquant contre un Blocker à 11 000 : le létal était impossible, c'était un tour de défense. El Thor valait +2000 en counter à son tour. À 2 vies, avec 2 Law qui peuvent bloquer (Killingham empêche d'attaquer, pas de bloquer) et Kiten + El Thor en main, survivre n'était pas exclu, et il était à 1 vie. |

## Lignes alternatives

1. **Karoo T9** (la plus chère). Après Gamma Knife + El Thor sur Vivi et Kiten sur un EB02 :
   - Shura 6000 sur le Karoo OP18-004 (5000) : il lui faut un counter de 2000 ;
   - Leader 7000 sur l'EB02 passé à 7000 par Kiten : il lui faut 1000 ;
   - Senor Pink sur la cible encore en vie.

   Avec une seule carte en main, il sauve au mieux un des deux. Il arrive à son tour avec un ou deux attaquants de moins, au lieu d'une carte de plus.
2. **Sabo T5** : Ohm d'abord sur Usopp (son effet le met à 1000), puis le Leader face. L'attaque face reste possible, elle passe juste en second.
3. **Spandam T7** : Ohm, puis Law à 6000 (avec El Thor), puis le Leader en dernier. Si le Trigger retire un perso, il retire un perso qui a déjà attaqué.

## Part de variance

- **Luffy 18:36** : à 1 vie contre un Luffy qui attaque deux fois à 15 000. La partie se joue au T9 (⚠️), sans erreur nette.
- **Luffy 18:53** : au T10, 4 attaques contre 1 carte. Chaque vie prise lui donne une carte et Gum-Gum Giant Axe arrête Law. Surtout de la variance, sauf la question du blocage au T9.
- **Spandam** : trois Triggers ont retiré trois de mes persos, et il remet une vie presque chaque tour. Grosse part de variance, aggravée par l'ordre du T7.
- **Karoo** : Banish dès le T4, puis deux EB02 qui touchent au T8. La partie était mal partie avant le T9, mais le T9 a retiré la dernière chance.
- **Gunko 07:06** : le pire matchup selon le pro. Killingham a gelé les deux Law deux tours de suite.
- **Luffy OP13-001, W** malgré deux ❌ : la victoire ne valide pas les T5 et T9.

## Tilt (ch. 4)

- **Bloc 18:32 → 18:53** : 4 parties en une trentaine de minutes, enchaînées. Après la défaite de 18:36, la partie de 18:44 est propre (5 tours ✅). **Aucun signe de tilt.**
- **Bloc 22:27 → 23:38** : les **6 ❌ de la session sont toutes ici**, dans les 4 dernières parties (22:52 → 23:38). Elles commencent après deux victoires : ce n'est pas une réaction à une défaite. L'heure (de 22:27 à environ 23:50) et la fatigue l'expliquent mieux.
- **Un signal net du ch. 4** : à 23:13, abandon à 4 vies contre 4 juste après le Trigger Jabra. La partie de 23:27 est lancée dans la foulée, et elle contient l'erreur la plus coûteuse de la session (Senor Pink face au T9). Défaite frustrante, partie enchaînée, décision rapide.
- **07:06** : abandon à 2 vies contre 1. Les abandons discutables reviennent à chaque session : Gecko Moria T6 et Karoo T9 en session 2 ; Spandam T13 et Gunko T11 ici.

**Règle pré-engagée proposée** :
1. avant de cliquer « Concede », dire ses vies, mes vies et mes counters. Si j'ai 2 vies ou plus, ou s'il est à 1 vie, je joue son tour ;
2. après un abandon, 5 minutes de pause avant de relancer ;
3. après 23:00, une dernière partie, puis stop.

## Tags : `attack-economy` `role` `sequencing` `lethal`

- `attack-economy` + `role` : réflexe 1 (Luffy OP13-001 T5 et T9, Karoo T9, Sabo T5).
- `sequencing` : Triggers de Spandam (T7, T13).
- `lethal` : abandons (Spandam T13, Gunko 07:06 T11) et ressources hors létal (Luffy 18:36 T9).

## Bilan face ou clear

- **49 tours relus : 36 ✅, 7 ⚠️, 6 ❌.**

| Bloc | Tours | ✅ | ⚠️ | ❌ |
|---|---|---|---|---|
| 18:32 → 18:53 | 15 | 13 | 2 | 0 |
| 22:27 → 23:38 | 29 | 19 | 4 | 6 |
| 07:06 | 5 | 4 | 1 | 0 |

- Pour comparer : session 1, 28 tours (6 ⚠️, 2 ❌) ; session 2, 17 tours (4 ⚠️, 3 ❌) ; session 3, 1 ❌ et 2 ⚠️ sur les tours relus.
- **Progrès** : les tours de létal (ordre, Blocker retiré avant d'attaquer) et le ciblage des moteurs. Le bloc de 18:32 et la partie de 07:06 n'ont aucune ❌.
- **Ce qui coûte encore** : le clear par attaque sur les petits persos couchés, surtout tard le soir.

## Faiblesse prioritaire → changement testable

**Faiblesse** (la plus fréquente, et présente depuis la session 1) : quand le létal est impossible, des attaques partent face alors qu'un petit perso adverse couché, souvent celui qui tue mes 1-drops, peut être tué.

**Ce qui change** : la vérification « en fin de tour » arrive trop tard. On la place **avant la première attaque**.

**Changement testable, sur les 10 prochaines parties** : à chaque tour où Y < X (pas de létal) et où un perso adverse couché a une power inférieure ou égale à celle d'un de mes attaquants, **la première attaque du tour va sur ce perso**, avec mon plus petit attaquant capable de le tuer. Le reste peut aller face ensuite.
- Exceptions : Gunko (récursion) ; cible déjà gelée par Lightning Dragon ou Killingham (passer alors à la cible suivante).

**Mesure** : la prochaine analyse compte ces tours dans les fiches. Cette session : 6 sur 14. Objectif : 100 %.

**Drill (ch. 5.1)** : rejouer en solo Sabo T5 (Usopp couché à 2000, 9 cartes en face, Leader + Ohm) et Luffy OP13-001 T5 (Nami EB02-017 couchée, Blocker Nami OP14-031, Leader + 2 Ohm). 5 fois chacune, en comparant face et clear sur les deux tours suivants.

**Rappel, sans en faire une 2e priorité** : contre Spandam et dans tout tour de létal, les persos d'abord et le Leader en dernier.

## Questions pour toi (ch. 9.3)

1. **Luffy 18:53, T9** : Law était debout et pouvait bloquer la Double Attack de Luffy (2 dégâts). Pourquoi pas ? Si une carte l'en empêchait, dis laquelle : la fiche ne montre rien.
2. **T2 en second** : ton Leader n'attaque toujours pas (Gunko 18:32, Luffy 18:53). C'est la troisième fois que je pose la question. Déroule ton raisonnement avant que je donne le mien.

## Repères ajoutés

Textes lus dans `data/cache/cartes.json`. À ajouter à `knowledge/` si tu valides (rien n'est fait).

- **Luffy [OP18-022]** (Leader 5000) :
  - [DON!! x3] When Attacking, une fois par tour, il se redresse et ne se redressera pas au Refresh suivant : il attaque deux fois par tour dès 3 DON!! ;
  - Nico Robin [OP18-031] le redresse à la fin de son tour et protège ses persos de mes effets (elle se couche à leur place) ;
  - Zoro & Sogeking [OP18-027] fixe sa base à 7000 pendant mon tour (Leader debout avec 3 DON!! ou plus) ;
  - Zoro & Sogeking et Luffy [OP18-118] empêchent un de mes persos d'être couché : il ne peut ni attaquer ni bloquer.

  C'est probablement le « Water Seven Luffy » de la veille du pro (ses cartes citent le type {Water Seven}), à confirmer. Ton bilan contre lui : 2 L, 1 inconnu.
- **Luffy [OP13-001]** (Leader 5000) : pendant mon attaque, s'il a 5 DON!! actifs ou moins, il couche des DON!! pour +2000 chacun, sur son Leader ou un perso {Straw Hat Crew}. Mes attaques face lui coûtent des DON!!, pas des cartes.
- **RP Luffy [ST10-002]** (Leader 6000) : seuils de la fiche respectés (attaques à 6 et 7).
- **Karoo** : Vivi [OP18-011] donne +1000 à ses persos {Animal} {Alabasta}, et gagne Blocker et +6000 pendant mon tour. Karoo [OP18-004] (4000 imprimé) gagne Rush à 5000, Banish à 6000 et Unblockable à 7000. Ajouter ces bonus à la power « couchée » de la fiche.
- **Spandam** (Leader CP) : les Triggers Kalifa, Fukurou, Rob Lucci et Jabra visent un perso (couché, K.O. ou renvoyé sous le deck).
- **El Thor [OP15-075]** : en Main, +1000 puis K.O. d'un perso à 3000 ou moins ; en Counter, +2000 sur un Enel. **Lightning Dragon [OP15-077]** ne gèle qu'un perso **couché** à 6000 ou moins.
- **Fiche** : la ligne « mes attaquants » inclut les persos gelés ou qui ne peuvent pas être couchés. Correction possible dans `scripts/fiche_partie.py` (non faite).
