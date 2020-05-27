# programme cercle
'''
=========================Sujet=================================
Ecrire un programme qui demande à l’utilisateur de donner le rayon d’un cercle et lui retourne sa surface et son périmètre
===============================================================
'''

import math #importer des formules de math
from math import pi #spécifier dans math l'utilisation de la constante pi

rayon = int(input("saisir le rayon du cercle"))
perimetre = (rayon * rayon)
surface = (perimetre * pi)
print ("le périmètre du cercle est de : ", perimetre)
print ("la surface du cercle est de : ", surface)





   