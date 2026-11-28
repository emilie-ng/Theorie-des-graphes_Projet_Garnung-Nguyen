# Floyd-Warshall : recherche des chemins les plus courts

Projet de théorie des graphes, année 2026-2027.  
Équipe : Justine GARNUNG, Emilie NGUYEN.

Ce programme Python calcule, avec l'algorithme de Floyd-Warshall, les chemins de valeurs minimales entre tous les couples de sommets d'un graphe orienté et valué.

## Fonctionnalités

- Choix d'un graphe par son numéro, et test de plusieurs graphes sans relancer le programme
- Chargement du graphe depuis un fichier texte, lu une seule fois à chaque analyse
- Affichage des matrices avec colonnes alignées et sommets identifiés
- Affichage des matrices `L` et `P` initiales, puis après chaque itération
- Détection des circuits absorbants
- Affichage d'un chemin minimal au choix, ou de tous les chemins

## Prérequis

Python 3.6 ou plus récent. Aucune bibliothèque externe.

## Installation et lancement

```bash
git clone https://github.com/emilie-ng/Theorie-des-graphes_Projet_Garnung-Nguyen.git
cd Theorie-des-graphes_Projet_Garnung-Nguyen
python main.py
```

Lancez la commande depuis le dossier du projet, où se trouvent les fichiers de graphes. Selon votre installation, utilisez `python3` à la place de `python`.

## Utilisation

1. Saisir le numéro d'un graphe existant (par exemple `3` pour `graphe3.txt`).
2. Lire la matrice des valeurs (`L initiale`), puis les itérations de l'algorithme.
3. En l'absence de circuit absorbant, choisir dans le menu :
   - `1` : afficher un chemin (sommets de départ et d'arrivée)
   - `2` : afficher tous les chemins
   - `3` : revenir au choix du graphe
4. Taper `stop` pour quitter.

## Format des fichiers de graphes

Les fichiers sont nommés `graphe<numéro>.txt`.

```text
Nombre de sommets
Nombre d'arcs
Sommet_de_départ Sommet_d_arrivée Valeur_de_l_arc    (une ligne par arc)
```

Exemple (`graphe2.txt`) :

```text
4
5
0 1 1
0 2 5
1 2 -3
1 3 5
2 3 2
```

- Les sommets sont numérotés de `0` à `n - 1`.
- Les valeurs sont des entiers (négatifs et nuls compris).
- Il y a au plus un arc d'un sommet vers un autre.
- Pour ajouter ou supprimer un arc, modifiez sa ligne et mettez à jour le nombre d'arcs.

## Algorithme

- `L[i][j]` : valeur du meilleur chemin connu de `i` vers `j`
- `P[i][j]` : prédécesseur de `j` sur ce chemin

**Initialisation :** `L[i][j]` vaut la valeur de l'arc, ou `∞` s'il n'existe pas. La diagonale vaut `0`, sauf en cas de boucle négative (une boucle positive ou nulle n'apparaît donc pas). `P[i][j]` vaut `i`.

**Itérations :** chaque sommet est testé à son tour comme intermédiaire.

```text
si L[i][k] + L[k][j] < L[i][j]
    L[i][j] ← L[i][k] + L[k][j]
    P[i][j] ← P[k][j]
```

À l'écran, « itération k = 1 » correspond au sommet intermédiaire `0`, et ainsi de suite.

**Circuit absorbant :** après chaque itération, une valeur négative sur la diagonale de `L` signale un circuit absorbant. Le calcul s'arrête alors.

**Reconstruction d'un chemin :** on remonte les prédécesseurs dans `P` depuis le sommet d'arrivée.

**Complexité :** `O(n³)` opérations pour le calcul (hors affichage) et `O(n²)` en mémoire.

## Graphes de test

| Graphe | Sommets | Arcs | Circuit absorbant |
|---:|---:|---:|:---:|
| 1 | 4 | 5 | non |
| 2 | 4 | 5 | non |
| 3 | 4 | 6 | non |
| 4 | 4 | 6 | **oui** |
| 5 | 4 | 7 | non |
| 6 | 4 | 9 | **oui** |
| 7 | 7 | 12 | non |
| 8 | 5 | 7 | non |
| 9 | 5 | 7 | non |
| 10 | 5 | 7 | **oui** |
| 11 | 5 | 8 | non |
| 12 | 5 | 9 | non |
| 13 | 8 | 12 | **oui** |

Les traces d'exécution sont dans `traces_graphes/` (une par graphe) et dans `trace_graphes_complet.txt`.

## Organisation du dépôt

| Fichier | Rôle |
|---|---|
| `main.py` | Boucle principale |
| `lire_graphe.py` | Lecture d'un fichier et construction de la matrice des valeurs |
| `afficher_graphe.py` | Affichage aligné d'une matrice |
| `floyd_warshall.py` | Algorithme et détection des circuits absorbants |
| `chemin_minimal.py` | Reconstruction et affichage des chemins |
| `graphe1.txt` à `graphe13.txt` | Graphes de test |
| `traces_graphes/`, `trace_graphes_complet.txt` | Traces d'exécution |
