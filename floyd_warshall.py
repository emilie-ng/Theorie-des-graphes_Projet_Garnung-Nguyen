from afficher_graphe import *

def floyd_warshall(L) :
    """
    Exécute l'algorithme de Floyd-Warshall sur la matrice L.
    Affiche les matrices L et P initiales puis après chaque itération.

    Prend en paramètre la matrice L des valeurs des arcs.
    Retourne les matrices L, P et un booléen : True si le graphe contient un circuit absorbant, False sinon.
    """
    n = len(L)

    #initialisation de P : P[i][j] = i
    P = [] #matrice des prédécesseurs
    for i in range(n) :
        ligne = []
        for j in range(n) :
            ligne.append(i)
        P.append(ligne)

    print("L initiale")
    afficher_graphe(L)
    print("")
    print("P initiale")
    afficher_graphe(P)
    print("")

    #calcul des plus courts chemins
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if L[i][k] + L[k][j] < L[i][j] : #passer par le sommet k est plus court
                    L[i][j] = L[i][k] + L[k][j] #on met à jour avec le chemin qui passe par k
                    P[i][j] = P[k][j] #le prédécesseur de j est celui du chemin de k à j

        print("L après l'itération k =", k+1)
        afficher_graphe(L)
        print("")
        print("P après l'itération k =", k+1)
        afficher_graphe(P)
        print("")

        #un terme négatif sur la diagonale = circuit absorbant : on arrête
        for i in range(n) :
            if L[i][i] < 0 :
                return L, P, True

    return L, P, False #aucun circuit absorbant