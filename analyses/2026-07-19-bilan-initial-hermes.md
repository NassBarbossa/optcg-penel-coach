# Bilan initial — baseline Hermes (2026-07-19)

Premier bilan du coach, basé sur les stats perso Hermes (5724 W / 5353 L, 51,7 %, ~11 min/partie) et la méthode du guide. Sert de référence : les prochains bilans se mesureront contre celui-ci.

## Constat n°1 — Le volume ne progresse plus (ch. 1 & 5)

~11 000 parties et 51,7 % de winrate avec un deck que le pro qualifie de Tier 1 « insanely good ». Sur un échantillon pareil, la variance est lavée depuis longtemps : c'est le portrait type de la **répétition sans deliberate practice** (ch. 5.1) — beaucoup de reps, même pilotage, mêmes catégories d'erreurs. La marge de progression n'est pas dans « jouer plus », elle est dans « jouer moins, revoir plus ».

## Constat n°2 — LE leak : jouer en 2e (la faiblesse prioritaire)

Écarts 1st → 2nd :

| Matchup | 1st | 2nd | Écart |
|---|---|---|---|
| Mirror Enel | 60,2 % | 39,8 % | **−20,4** |
| UY Nami | 40,2 % | 21,9 % | **−18,3** |
| PY Rosinante | 70,1 % | 62,1 % | −8,0 |
| UG Luffy | 63,4 % | 59,2 % | −4,2 |
| Yamato | 55,3 % | 58,0 % | +2,7 |
| BY Teach | 31,0 % | 31,1 % | +0,1 |

Aller 2e est structurellement un peu plus dur, mais −18 à −20 points n'est pas structurel : c'est un **pattern de pilotage**. Hypothèse de travail : en 2e, tu subis le tempo au lieu de jouer le rôle du defender (économie de counters, gestion de life, patience sur les swings symétriques) — et Enel a justement un kit défensif (≤6 DON!!, Reiju, Mamaragan counter). Yamato (+2,7 en 2e) prouve que tu SAIS le faire quand le plan « counter les petites, encaisser les grosses » est explicite.

## Constat n°3 — Le mirror est un coin flip chez toi

60/40 selon le dé = winrate moyen ~50 % contre les autres Enel : **aucun edge dans le mirror** alors qu'Enel est un des decks les plus joués du format. Chaque point d'edge mirror vaut cher en winrate global. Non couvert par la bible → à demander au pro (il propose les DM).

## Constat n°4 — Où sont les points à prendre

- **UY Nami** : pire matchup fréquent (Tier S, en hausse ↑ sur la tierlist JP), 40/22, et PAS couvert par la bible. C'est la demande n°1 à faire au pro.
- **BY Teach** : 31 % symétrique — conforme au « Hard » du guide, et deck encore peu joué. Priorité moindre que Nami malgré le chiffre plus laid : moins fréquent, et le plan de la bible est déjà là.
- **Rosinante** : 70/62, déjà bon. Tester la ligne de DON!! denial du guide en 2e : si elle est bien exécutée, le 62,1 % doit monter — c'est le test de l'hypothèse « Preferred Start: Second ».
- **Yamato 55-58 % sur un matchup « Easy »** : sous-performance discrète. À revoir après quelques parties loggées.

## Constat n°5 — 11 min/partie et le grind

Durée moyenne courte + volume énorme = sessions de queue en chaîne. Deux risques (ch. 3-4) : aucune capture entre les parties (le cerveau réécrit), et le tilt en série invisible. À vérifier dans Hermes si possible : winrate en fonction du rang de la partie dans la session.

## Changement testable (UN seul, ch. 3.5)

> **Sur les 15 prochaines parties jouées en 2e** : avant chaque tour, répondre mentalement à deux questions — « qui est le beatdown LÀ, maintenant ? » et « combien de counter power j'ai en main vs ce qu'il peut représenter ? ». Après chaque partie, logger 1-2 décisions incertaines dans `parties/` AVANT de relancer une queue.

Pas de « joue mieux en 2e » : juste ce protocole, 15 parties, puis on mesure.

## Demandes à faire au pro (il propose les DM)

1. Guide du matchup **UY Nami** (ton pire matchup fréquent).
2. Guide du **mirror Enel**.

## Tags baseline

`role` (subi en 2e), `counter-management` (hypothèse à confirmer par les logs), `life-management` (hypothèse), `mulligan` (à vérifier : keeps différents en 2e ?)
