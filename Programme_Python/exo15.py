# programme moyenneEntier 
'''
Ecrire un algorithme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu'à ce nombre. Par exemple si l'on tape 4 , l’algorithme doit calculer: 1 + 2 + 3+ 4 = 10 Réécrire l'algorithme qui calcule cette fois la moyenne !
''' 
s = () #affecter la valeur 0 à s
i = 0
m = ()
nb = int(input(print("saisir un nombre entier")))
print(nb) #saisir un nombre entier
for s in range (1, nb): 
    s = nb + i
    i +=1
    print ("la valeur de i est : ", i)
    print ("la somme est : ", s)
m = s/(nb-1)
print ("la moyenne est : ", m)