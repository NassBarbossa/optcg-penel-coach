# Analyse 2026-11-27 — Enel vs Nico Robin [EB05-010] (L), partie de 12:04

## Contexte

- Fiche : `parties/2026-11-27-1204-enel-vs-nico-robin.md`. Je commence. J'abandonne au T7, à 2 vies contre 2.
- Partie hors classement : le sim n'a pas écrit de fichier de résultat (il le fait seulement pour les parties OP Bounty).
- Mulligan : Satori, Enel 6c, El Thor ×2, Kiten. Un seul 1-drop, Enel en main, des counters. Keep ✅.
- Matchup absent de la base jusqu'ici : ajouté dans `knowledge/meta/matchups.md`. Son deck : Lilith [OP13-113], Robin [EB05-016], Gloriosa [EB05-052], Nami [EB05-055], et l'événement You'll Frighten Me... [OP14-118] en trigger.
- Textes (base locale `data/cache/cartes.json`) :
  - **Robin [EB05-010]**, Leader 5000. [Once Per Turn] Quand un de ses persos <Wisdom> sans [Blocker] est mis K.O., il ajoute la carte du dessus du deck à ses vies. [Activate: Main] [Once Per Turn] Il remet debout un de ses persos <Wisdom> à 6000 ou moins.
  - **Robin [EB05-016]**, 6000. On Play : pose un perso <Wisdom> de coût 5 ou moins depuis sa main. Trigger : met à terre un de mes persos de coût 6 ou moins.
  - **Nami [EB05-055]**, 6000. Trigger : se pose si son joueur a 2 vies ou moins. On Play pendant son tour : +1 vie.
  - **Gloriosa [EB05-052]**, 6000. Quand il devrait prendre un dégât, il peut la défausser à la place.
  - **You'll Frighten Me... [OP14-118]**. Trigger : pose un perso à 6000 ou moins avec [Trigger] depuis sa main.

## Décisions clés (évaluées au moment T)

| Tour | Compte | Décision | Verdict |
|---|---|---|---|
| T3 | 4 vies → 5 coups ; Leader, Satori ; 6 cartes ; 0 Blocker ; 0 perso couché | Satori à 6000 face, Leader à 7000 face : 4 → 2 | ✅ Pas de cible couchée, donc la face est la seule attaque utile. Le trigger You'll Frighten Me... qui pose un Robin à 6000 fait partie du risque normal. |
| T5 | 2 vies → 3 coups ; Leader, Pudding (Enel 6c vient d'arriver) ; 6 cartes ; 0 Blocker ; couchés : Lilith 2000, Robin EB05-016 6000 | Lightning Dragon gèle Robin, El Thor tue Lilith (son Leader regagne une vie) ; Pudding face (trigger Nami : un perso à 6000 de plus), Leader face : 3 → 1 | ❌ Pas de létal possible : 3 coups avec 2 attaquants, contre 6 cartes. Le KO de Lilith avait déjà utilisé son « une fois par tour » : un deuxième KO ce tour-ci ne lui rendait aucune vie. Pudding à 6000 tuait donc le Robin couché (6000 contre 6000) gratuitement. C'était le perso qui m'avait touché deux fois au T4. À la place, les deux attaques face lui ont donné 2 cartes. Le coup qui l'a fait passer à 2 vies a aussi activé le trigger de Nami, qui se pose à 2 vies ou moins. **Limites** : DON!! approximatifs, valeur de ses counters inconnue. |
| T4, T6 | Défense : 4 attaques à 6000 contre mon Leader à 5000 | 3 Kiten et 1 El Thor en counter | ✅ Chaque counter arrête une attaque. Mais il a fallu 4 cartes pour survivre à deux tours. |
| T7 | 2 vies → 3 coups ; Leader, Enel 6c à 10 000 ; 5 cartes ; en face 5 persos à 6000 ; moi à 2 vies, main : Enel 6c, El Thor, Senor Pink, Mamaragan | Law posé (mis à terre par le trigger Robin), Enel face : 2 → 1, puis abandon | ✅ L'abandon se défend. Pas de létal (3 coups pour 2 attaquants). Au tour suivant, il avait 6 attaques et il lui fallait 3 coups. Je n'avais qu'environ 2 counters (El Thor +2000, Mamaragan +1000) et pas de Blocker debout. Mamaragan ne pouvait mettre à terre aucun de ses persos (tous à 6000, au-delà de sa limite de 5000). |

## Lignes alternatives

- **T5** : El Thor sur Lilith (le KO qui lui rend sa vie du tour), puis Pudding sur le Robin couché, puis le Leader face. Il perd un attaquant à 6000 pour de bon, il ne regagne qu'une vie, et il pioche une carte au lieu de deux. Le trigger Nami reste possible sur la seule attaque face.

## Part de variance

- **2 triggers sur 4 coups au Leader** : You'll Frighten Me... (Robin à 6000) et Nami (un perso à 6000, puis une vie). La part de variance est forte : chaque trigger lui a donné un attaquant gratuit.
- Son board a grandi de 2 à 5 persos à 6000 en 5 tours, et ses deux 2000 ont tué mes 1-drops. Le résultat dépend surtout de ça.

## Tags : `attack-economy` `sequencing`

## Faiblesse prioritaire → changement testable

C'est la même que dans les rapports de session : **face ou clear**. Le changement testable reste celui de la session en cours.

Repères ajoutés pour ce matchup (dans `knowledge/meta/matchups.md`) :
- son Leader ne regagne une vie qu'**une fois par tour**. Le premier KO du tour la lui rend, les suivants sont gratuits : quand on clear, on clear plusieurs persos le même tour ;
- quand il est à 3 vies, le coup qui le fait passer à 2 active Nami (trigger à 2 vies ou moins) ;
- Gloriosa peut se défausser pour encaisser un dégât à la place de sa vie.
