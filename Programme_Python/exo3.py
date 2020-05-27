# programme resistance

'''
===============================Sujet===============================
Version 1 :
Faire un programme qui saisit 3 résistances : R1, R2 et R3.
Calculer et afficher la résistance en série : R1 + R2 +R3
Calculer et afficher la résistance en parallèle : (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
===================================================================
'''
#int(input) pour sécifier que le type de donnée est un entier
r1 = int(input("Veuiller indiquer la valeur de la résistance 1 "))
r2 = int(input("Veuiller indiquer la valeur de la résistance 2 "))
r3 = int(input("Veuiller indiquer la valeur de la résistance 3 "))
rs = int(r1 + r2 + r3)
rp = int(r1 * r2 * r3) / (r1* r2 + r2*r3 + r1*r3)
#afficher les résultats 
print ("La résistance en série est de ", rs)
print ("La résistance en parallele est de ", rp)

'''
===============================Sujet===============================
Version 2 :
Demander a l’utilisateur d’indiquer son choix.
S’il entre la valeur  1, calculer et afficher la fréquence en série.
S’il entre la valeur 2, calculer et afficher la fréquence en parallèle.
===================================================================
'''
#demander à l'utilisateur de choisir entre les chiffres 1 ou 2
choice = input ("Veuillez saisir la valeur 1 ou 2 ", )

#si l'utilisateur choisi le chiffre 1 alors afficher la résistance en série, sinon afficher la résistence en parallele
if choice == '1' :
    rs = ( 1 + 1 + 1 )
    print ("la résistance en série est de ", rs)
elif choice == '2':
    rp = int(r1 * r2 * r3) / (r1* r2 + r2*r3 + r1*r3)
    print ("la résistance en parallele est de ", rp)
    
         
    


 




   