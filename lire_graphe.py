def lire_graphe(num) :
    """
    Lit le graphe à partir du fichier texte et initialise une matrice L avec la valeur des arcs.

    Prend en paramètre le numéro du graphe.
    Retourne la matrice L remplie de la valeur des arcs.
    """
    with open(f"graphe{num}.txt", "r", encoding="utf-8") as f :
        n = int(f.readline()) #on lit la ligne 1, n = nombre de sommets
        m = int(f.readline()) #on lit la ligne 2, m = nombre d'arcs
        L = [] #matrice (liste de listes) de la valeur des arcs

        #on initialise la diagonale par des 0 et le reste par des infinis
        for i in range(n) :
            ligne = []
            for j in range(n) :
                if i == j :
                    ligne.append(0) #diagonale par 0
                else :
                    ligne.append(float("inf")) #pas d'arc = infini
            L.append(ligne)

        #on remplace les infinis par la valeur de l'arc
        for k in range(m) :
            depart, arrivee, valeur = f.readline().split() #on lit le sommet de départ, le sommet d'arrivée et la valeur de l'arc
            depart = int(depart)
            arrivee = int(arrivee)
            valeur = int(valeur)
            if depart == arrivee :
                L[depart][depart] = min(0, valeur) #la diagonale reste à 0 sauf si la boucle est négative (cas du circuit absorbant)
            else :
                L[depart][arrivee] = valeur #sinon on stocke la valeur de l'arc dans la matrice
    return L