def construire_chemin(P, L, depart, arrivee) :
    """
    Construit un plus court chemin de départ à arrivée à partir de la matrice P.

    Prend en paramètre les matrices P, L, les sommets de départ et d'arrivée.
    Retourne la liste des sommets du chemin ou None s'il n'existe pas de chemin.
    """
    if L[depart][arrivee] == float("inf") :
        return None #pas de chemin

    chemin = [arrivee] #on stocke le sommet d'arrivée dans une liste
    sommet = arrivee #on part de la fin et on remonte les prédécesseurs
    while sommet != depart :
        sommet = P[depart][sommet] #on remonte au prédécesseur
        chemin.append(sommet)
    chemin.reverse() #on a construit le chemin de l'arrivée vers le départ donc on inverse la liste
    return chemin

def afficher_chemin(P, L, depart, arrivee) :
    """
    Affiche le chemin minimal de départ à arrivée ou un message s'il n'y en a pas.

    Prend en paramètre P, L, depart et arrivee.
    Ne retourne rien (fonction d'affichage).
    """
    chemin = construire_chemin(P, L, depart, arrivee)
    if chemin == None :
        print("Il n'existe pas de chemin de", depart, "à", arrivee)
    else :
        print(f"Chemin minimal de {depart} à {arrivee} : {' -> '.join(str(s) for s in chemin)} (valeur {L[depart][arrivee]})")

def interroger_chemins(P, L) :
    """
    Boucle d'interface où on demande un départ et une arrivée à l'utilisateur puis affiche le chemin minimal.

    Prend en paramètre les matrices P et L.
    Ne retourne rien (fonction d'affichage).
    """
    n = len(L)
    reponse = ""
    while reponse != "3" :
        print("1 - Afficher un chemin")
        print("2 - Afficher tous les chemins")
        print("3 - Arrêter")
        reponse = input("Saisie : ")
        print("------------------------------------")

        if reponse == "1" :
            depart = int(input("Sommet de départ : "))
            arrivee = int(input("Sommet d'arrivée : "))
            if depart < 0 or depart >= n or arrivee < 0 or arrivee >= n :
                print("Sommet invalide (entre 0 et", n - 1, ").")
                print("------------------------------------")
            else :
                afficher_chemin(P, L, depart, arrivee)
                print("------------------------------------")
        elif reponse == "2" :
            #on affiche le chemin minimal de chaque sommet vers chaque autre sommet
            for depart in range(n) :
                for arrivee in range(n) :
                    afficher_chemin(P, L, depart, arrivee)
            print("------------------------------------")
        elif reponse != "3" :
            print("Choix invalide.")