# programme moyenneEntier 
'''
Faire un programme qui calcule le PGCD de deux nombres saisis au clavier en utilisant l'astuce suivante: soustrait le plus petit des deux entiers du plus grand jusqu'à ce qu'ils soient égaux.
''' 
import math
def PGCD (a, b) : #fonction PGCD from import math 

	r = int() #affecter la valeur 0 à reste r
	i = 0
	a = int(input(print("saisir un nombre entier")))
	print(a) 
	b = int(input(print("saisir un nombre entier")))
print(b) 

	if b == 0 :
		return a
	else :
		r = a % b
		return PGCD (b, r)	
print ("le PGCD", a, "et" , b, "est", PGCD (b, r))


 