# programme sommeNombre
'''
============================Sujet=====================
Ecrire un programme qui saisit 5 variables de type entier au clavier et qui affiche leur somme. Utiliser une boucle (for ou while ou do..while).
======================================================
'''
#déclarer i incrémentation à 1 allant de 1 à 5
#déclarer à 0 entier naturel à saisir par l'utilisateur
#déclarer snbi à 0 comme sac contenant la somme des nbi à chaque saisie  
i=1
nbi=0
snbi=0
#tant que le nombre de saisie de nombre entier est inférieur ou égal à 5 alors mettre les nombres saisis dans le sac snbi snbi = snbi+nbi saisi, et refaire un autre tour i+1  
#jusqu'à i atteint 5, afficher la somme des nbi dans le snbi
while i<=5:
    nbi=int(input("saisir un nombre entier", ))
    snbi=snbi+nbi
    i=i+1
else:
    print ("la somme des nombres entiers est ", snbi)
