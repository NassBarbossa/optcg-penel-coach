# OPTCG Penel Coach — Design

**Date** : 2026-07-19
**Statut** : validé en brainstorming

## Objectif

Un coach personnel d'analyse de gameplay pour One Piece TCG (jeu sur simulateur en ligne). L'utilisateur fournit ses parties (captures d'écran, récits) ; le coach les analyse contre une base de connaissances et produit des rapports orientés progression. Le projet est 100 % Markdown + un skill Claude Code : pas de code, pas de tests, pas d'infra.

## Principe fondateur

Le coach applique la méthode du guide « How to get better — The psychology behind becoming a PRO » (11 chapitres fournis progressivement par l'utilisateur) :

- **Deliberate practice** : chaque analyse cible une faiblesse précise juste au-dessus du niveau actuel, pas une liste exhaustive d'erreurs.
- **Qualité de décision ≠ résultats** : la progression se mesure sur la qualité des lignes de jeu (disparition de catégories d'erreurs), pas sur le win rate court terme. Une bonne décision perdante n'est pas une erreur ; une mauvaise décision gagnante n'est pas un succès à répéter (outcome bias, ch. 2).
- **Stades de progression** (ch. 1) : compétence mécanique → reconnaissance de patterns → raisonnement stratégique conscient → expertise adaptative. Le coach situe le joueur et adapte ses conseils.
- **Contre-mesures structurelles aux biais** (ch. 2) : le log écrit et systématique des parties neutralise confirmation bias, recency bias et self-serving attribution. Le coach distingue explicitement la part contrôlée (décisions) de la part de variance.
- **Anti-tilt** : quand les résultats stagnent mais que les décisions s'améliorent, le coach le dit explicitement (plateau de résultats ≠ plateau de skill).

## Structure du projet

```
optcg-penel-coach/
├── CLAUDE.md                       # contexte projet, ton du coach, règle d'or
├── knowledge/
│   ├── coaching/                   # le guide 11 chapitres du pro (la MÉTHODE)
│   │   ├── 01-learning-curve.md            # fourni
│   │   ├── 02-biases-self-assessment.md    # fourni
│   │   └── ...                             # 03 à 11 au fil de l'eau
│   ├── regles/
│   │   ├── regles-de-base.md       # pré-rempli : tour, DON!!, life, counters, blockers, triggers
│   │   └── mots-cles-et-timings.md # squelette : Rush, Blocker, Banish, On Play…
│   ├── fondamentaux/
│   │   └── strategie.md            # tempo, curve DON!!, card advantage, life comme ressource
│   └── meta/
│       ├── tier-list.md            # squelette vide, datas fournies par l'utilisateur
│       └── matchups.md             # squelette vide
├── decks/
│   └── TEMPLATE.md                 # leader, liste, plan de jeu, matchups
├── parties/
│   ├── TEMPLATE.md                 # log de partie sim (screenshots acceptés en vrac)
│   └── media/                      # captures d'écran
├── analyses/                       # rapports datés générés par le coach
└── .claude/skills/optcg-coach/
    └── SKILL.md                    # le skill unique
```

## Le skill `/optcg-coach`

Skill unique, trois modes selon l'entrée :

1. **Analyse de partie** — l'utilisateur fournit screenshots/récit ; le coach reconstruit la partie, identifie les décisions clés, évalue leur qualité au moment où elles ont été prises (jamais au résultat), propose des lignes alternatives, et cible UNE faiblesse prioritaire à travailler. Rapport sauvegardé dans `analyses/AAAA-MM-JJ-<matchup>.md`.
2. **Bilan** (« /optcg-coach bilan ») — relit les analyses passées, dégage les patterns récurrents, mesure la progression par catégories d'erreurs, situe le stade du joueur, recadre si nécessaire (variance vs skill).
3. **Review de deck** — évalue une liste contre la meta connue et les stats personnelles du joueur.

Règles de fonctionnement du skill :
- S'appuie systématiquement sur `knowledge/` ; si une règle manque pour trancher, il le dit au lieu d'inventer et propose de l'ajouter à la base.
- Les datas fournies par l'utilisateur font foi sur les connaissances générales du modèle.
- Ton direct, orienté progression, sans flatterie.

## Hors périmètre (YAGNI)

- Pas de scripts de stats automatisées, pas d'app, pas de base de données.
- Pas de skills multiples au départ ; découpe seulement si un mode devient lourd.
- Pas de scraping meta : les datas meta viennent de l'utilisateur.
