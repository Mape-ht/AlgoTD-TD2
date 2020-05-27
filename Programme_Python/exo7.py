# programme monnaie
'''
============================Sujet=====================
Décomposition d’un montant en euros Écrire un algorithme permettant de décomposer un montant entré au clavier en billets de 20, 10, 5 euros et pièces de 2, 1 euros, de façon à minimiser le nombre de billets et de pièces
======================================================
'''
#demander à l'utilisateur de saisir un montant en euro 
montant = int(input("Saisir un montant en euro", ))
print (montant) 

#calculer le nombre de billet de 20 euro dans le montant saisi en divisant le nombre /20
billet20 = int(montant//20)
print ("le nombre de billet de 20 euro est de :", billet20 )
#calculer le nombre de billet de 10 euro dans le montant saisi en divisant le reste de la division montant /20 par 10
billet10 = int(montant % 20)//10
print ("le nombre de billet de 10 euro est de :", billet10 )
#calculer le nombre de billet de 5 euro dans le montant saisi en divisant le reste de la division billet de 10 par 5 (ex: 1379/20=68 avec reste=15, billet de 10= 15/10 pour avoir le nb de billet de 20 faire reste 15/10 à /5 et ainsi de suite)
billet5 = int((montant % 20) % 10)//5
print ("le nombre de billet de 5 euro est de :", billet5 )
piece2 = int(((montant % 20) % 10)% 5)//2
print ("le nombre de piece de 2 euro est de :", piece2 )
piece1 = int((((montant % 20) % 10)% 5)% 2)//1
print ("le nombre de piece de 1 euro est de :", piece1 )






