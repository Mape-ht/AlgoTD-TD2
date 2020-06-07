# programme operationCalculatrice
'''
=======================Sujet============================
Ecrire un algorithme calculatrice permettant la saisie du premier entier (a) de l'opération ( + ou – ou * ou / : sont des caractères) et du deuxième entier (b) et qui affiche le résultat
========================================================
'''
#demander à saisir deux nombre entier a et b
a = (int(input("saisir un nombre entier a:", )))
print(a)
op = (str(input("saisir une opération :", )))
print(op)
b = (int(input("saisir un nombre entier b:", )))
print (b)
#utiliser selon que pour effectuer les opérations arithmétiques et afficher les résultats
if op == (" + ") :  
    print (("la somme est : ", a + b))
    if op == (" - ") :  
        print (("la difference est : ", a - b))
        if op == (" * ") :  
            print (("le produit est : ", a * b))
            if op == (" / ") :  
                if a == (0) :
                print ("l'opération est invalide : ", )
Else :
    print (("le quotient est : ", a // b))