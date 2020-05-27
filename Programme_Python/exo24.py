# programme nombreSecret
'''
=======================Sujet============================
Nombre secret : écrire un programme qui demande à l’utilisateur 1 d’entrer un nombre et à l’utilisateur 2 de le trouver en affichant, à chaque tentative, « trop grand » si le nombre entré est plus grand que le nombre secret, « trop petit » sinon. Le programme s’arrête quand l’utilisateur 2 a trouvé le nombre secret.
========================================================
'''
#saisir un 1 nombres entier 
a = int(input ("Saisir un nombre entier a :" ))
print (a)
tour = 0
b = ()
while (a != b):  #tant que a différent de b refaire le tour
    b = int(input ("Saisir un nombre entier b :" ))
    print (b)
    if a < b :
       print ("trop grand ",)
    elif a > b : 
        print ("trop petit ",) 
        tour =+ tour
    continue  
if a == b :
    print (" trouvé ! :", b)
