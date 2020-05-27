# programme distance
'''
============================Sujet=====================
Faire un programme qui saisit  les coordonnées de 2 points A (x1, y1) et b(x2, y2) et qui affiche la distance entre les 2 points.
Formule : distante = racine carrée de ((x1 – x2)2  + (y1 – y2)2)
 Racine carrée : sqrt. Ex : sqrt(7) ; <math.h>
======================================================
'''
#importer le fichier math 
import math
x1=float(input("saisir les coordonnés x1 de A", ))
print (x1)
x2=float(input("saisir les coordonnés x2 de A", ))
print (x2)
y1=float(input("saisir les coordonnés y1 de A", ))
print (y1)
y2=float(input("saisir les coordonnés y2 de A", ))
print (y2)
#pour calculer la distance, calculer d'abord (x1 – x2)2 puis (y1 – y2)2 
dA = float((x1-x2)*(x1-x2))
dB = float((y1-y2)*(y1-y2))
distance_AB = math.sqrt(dA+dB)
print("la distance entre les points A et B est :" , distance_AB)
