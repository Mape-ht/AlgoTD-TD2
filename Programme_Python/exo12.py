# programme nombreParfait
'''
=======================Sujet============================
Un nombre est parfait s’il est égal à la somme de ses diviseurs stricts (différents de lui-même). Ainsi par exemple, l’entier 6 est parfait car 6 = 1 + 2 + 3. Écrire un algorithme permettant de déterminer si un entier naturel est un nombre parfait
========================================================
'''
nb = int(input("Saisir un nombre entier: ", ))
monSac = int()
i = 1
for i in range (1,nb-1): 
	if nb % i == 0 :
		monSac = monSac + i
		i += 1
if nb == monSac :
	print ("le nombre est parfait" )
else:
	print ("le nombre n'est pas parfait")
