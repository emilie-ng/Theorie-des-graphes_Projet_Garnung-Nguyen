from lire_graphe import *
from afficher_graphe import *
from floyd_warshall import *
from chemin_minimal import *

num = ""
print("------------------------------------")
print("Pour arrêter le test, tapez 'stop'.")

while num != "stop" : #boucle pour tester les graphes sans relancer le programme
    print("Quel graphe voulez-vous tester ?")
    num = input("Saisie : ")
    if num == "stop" :
        break
    print("------------------------------------")

    #algorithme de Floyd-Warshall avec le graphe demandé par l'utilisateur
    g = lire_graphe(num)
    L, P, absorbant = floyd_warshall(g)

    #programme indique si le graphe contient au moins un circuit absorbant + affichage des chemins de valeurs minimales
    if absorbant :
        print("Le graphe contient au moins un circuit absorbant.")
    else :
        print("Le graphe ne contient pas de circuit absorbant.")
        print("------------------------------------")
        interroger_chemins(P, L)