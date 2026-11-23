def afficher_graphe(L) :
    """
    Affiche la matrice L avec les numéros des sommets et la valeur des arcs.

    Prend en paramètre la matrice L.
    Ne retourne rien (fonction d'affichage).
    """
    n = len(L)

    #création de la ligne avec le numéro des sommets de 0 à n-1
    tableau = [[""]]
    for j in range(n) :
        tableau[0].append(str(j))

    #création des lignes du tableau avec le numéro du sommet puis les valeurs
    for i in range(n) :
        ligne = [str(i)]
        for j in range(n) :
            if L[i][j] == float("inf") :
                ligne.append("∞") #pas d'arc donc on met infini
            else :
                ligne.append(str(L[i][j])) #valeur de l'arc
        tableau.append(ligne)

    #calcul de la largeur de chaque colonne
    largeurs = []
    for j in range(n + 1) :
        maxi = 0
        for i in range(n + 1) :
            if len(tableau[i][j]) > maxi :
                maxi = len(tableau[i][j])
        largeurs.append(maxi + 2) #2 espaces de séparation

    #affichage aligné à droite
    for i in range(n + 1) :
        ligne_affichee = ""
        for j in range(n + 1) :
            ligne_affichee += tableau[i][j].rjust(largeurs[j])
        print(ligne_affichee)