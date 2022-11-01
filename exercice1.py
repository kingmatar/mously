"""EXERCICE 1:
Ecire un programme qui permet de remplir une liste de valeurs entieres.
Le programme demande de saisir ensuite une valeur 
entiere V, puis supprime la premiere occurence de la valeur V de la liste.
Le programme doit afficher la liste avant et apres suppresion.
Faire l'exercice en utilisant le fonction remove() des listes.
ATTENTION : le programme ne doit pas avoir d'erreurs quelque soit les valeurs saisies.
"""
def removeDuplicate():
    for x in l:
        if x not in listNombres:
            listNombres.append()
    return listNombres   
n=int(input("veuillez saisir le nombre d'entier a saisir:"))
listNombres = []
for i in range(0,n):
    nbr= int(input("Tapez la valeur d'un entier : "))
    listNombres.append(nbr)
print("Voici la liste des nombres saisis : " , listNombres)
print(removeDuplicate(l))
