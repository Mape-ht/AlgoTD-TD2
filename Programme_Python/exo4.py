# programme puissance
"""
===============================Sujet===============================
Ecrire un programme qui saisit un réel x et un entier n et affiche x à la puissance n.
Version 1 : utiliser la fonction pow  du fichier d’en-tête <math.h>  ex : pow(x,n)
Version 2 : en utilisant un boucle
===================================================================
"""
#demander à l'utilistateur de saisir un nombre réel x et un entier n)
x = float(input("Saisir un nombre réel")) 
n = int(input("Saisir un nombre entier"))
p = pow(x,n) 
print ('la puissance est égale à', p)
if (n==0) :
    print ('la puissance est égale à', 1)
else:
    print ('la puissance est égale à', p)



