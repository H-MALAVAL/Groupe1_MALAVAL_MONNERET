# Groupe1_MALAVAL_MONNERET

# Space Invaders

## Règles du jeu

Space Invaders est un jeu où le joueur doit détruire des vagues d'aliens tout en évitant leurs attaques. Voici les règles :

1. **Déplacement du vaisseau** : Utilisez les touches `A` (gauche) et `Z` (droite) pour contrôler votre vaisseau spatial.
2. **Tir** : Appuyez sur `ESPACE` pour tirer des missiles sur les aliens.
3. **Objectif** :
    - Détruisez les aliens blancs, rouges et bonus pour marquer des points.
    - Survivez aux tirs des aliens rouges et bonus.
    - Protégez votre vaisseau et vos vies.
4. **Conditions de victoire** :
    - Vous gagnez si votre score atteint 1000 points.
5. **Game Over** :
    - Vous perdez si vos vies tombent à 0.

## Spécificités de l'implémentation

Le jeu a été développé en Python en utilisant la librairie Tkinter pour l’interface graphique. Voici les particularités techniques :

- **Aliens** :
  - Les aliens blancs se déplacent en ligne et descendent progressivement vers le joueur.
  - Les aliens rouges se déplacent de manière aléatoire et tirent des missiles.
  - Les aliens bonus sont plus rapides et peuvent résister à plusieurs impacts avant d'être détruits.
- **Murs** :
  - Des murs protecteurs permettent d'absorber certains tirs, mais ils peuvent être dégradés par les impacts.
- **Système de score** :
  - Points attribués selon la couleur de l'alien :
    - Blanc : 10 points
    - Rouge : 25 points
    - Bonus : 150 points
- **Réduction de la zone de jeu** :
  - La taille du canevas diminue lorsque le joueur atteint certains paliers de score, augmentant ainsi la difficulté.
- **Conditions dynamiques** :
  - Les aliens rouges se régénèrent automatiquement s’ils deviennent trop peu nombreux.
  - Des nouvelles lignes d'aliens blancs apparaissent toutes les 10 secondes.

## Répertoire Git

L'adresse du répertoire Git contenant ce projet est :
[https://github.com/H-MALAVAL/Groupe1_MALAVAL_MONNERET.git].

## Localisation des structures de données

Les structures de données suivantes ont été implémentées :

- **Classe `Alien`** (fichier : `classes/Aliens.py`) : Représente les différents types d'aliens et gère leurs déplacements et actions.
- **Classe `Joueur`** (fichier : `classes/Joueur.py`) : Modélise le vaisseau du joueur, ses vies et son score.
- **Classe `Missile`** (fichier : `classes/Missiles.py`) : Décrit les missiles tirés par le joueur et les aliens.
- **Classe `Murs`** (fichier : `classes/Murs.py`) : Gère les murs protecteurs et leur état.

Pour lancer le jeu, exécutez simplement le fichier principal : `main.py`.

---

Merci de jouer à Space Invaders et amusez-vous bien !

