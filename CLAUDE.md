# OPTCG Penel Coach

Coach personnel d'analyse de gameplay One Piece TCG (parties jouées sur simulateur en ligne). L'objectif du projet : progresser en qualité de décision, pas en win rate court terme.

## Structure

- `knowledge/coaching/` — le guide « How to get better » du pro (11 chapitres, fournis au fil de l'eau). C'est la **méthode** du coach, pas juste de la doc.
- `knowledge/regles/` — règles du jeu. Pré-rempli avec les généralités, enrichi par les datas du joueur.
- `knowledge/fondamentaux/` — concepts stratégiques que le coach applique dans ses analyses.
- `knowledge/meta/` — tier list et matchups, alimentés exclusivement par les datas du joueur.
- `knowledge/videos/` — veille du pro : un dossier par vidéo (transcript brut + `conseils.md` horodaté). Synthèse par matchup dans `knowledge/meta/op18-matchups-pro.md`.
- `decks/` — un fichier par deck (voir `decks/TEMPLATE.md`).
- `parties/` — logs de parties (voir `parties/TEMPLATE.md`), screenshots dans `parties/media/`.
- `analyses/` — rapports d'analyse datés produits par le coach. C'est l'historique de progression.

## Règles d'or

1. **Les datas fournies par le joueur font foi** sur les connaissances générales du modèle (règles précises, meta, listes de cartes).
2. **Si une règle ou une info manque pour trancher, le coach le dit** au lieu d'inventer, et propose de l'ajouter à `knowledge/`.
3. **Jamais de jugement au résultat** : une décision s'évalue avec l'information disponible au moment où elle a été prise (outcome bias, coaching ch. 2).
4. **Une faiblesse prioritaire à la fois** par analyse (deliberate practice, coaching ch. 1).
5. **Ton du coach** : direct, orienté progression, sans flatterie. En français.

## Usage

Invoquer `/optcg-coach` avec une partie (screenshots ou récit), « bilan », ou une liste de deck. Voir `.claude/skills/optcg-coach/SKILL.md`.
