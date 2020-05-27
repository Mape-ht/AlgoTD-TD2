# programme dureeDeVol
'''
=======================Sujet============================
Ecrire un algorithme qui donne la durée de vol en heure minute connaissant l'heure de départ et l'heure d'arrivée. 
a. On considère que le départ et l'arrivé ont lieu le même jour 
b. On suppose que la durée de vol est inférieure à 24 heures mais peut avoir lieu le lendemain

========================================================
'''
#Demander à l'utilisateur de saisir les différents horaires d'arrivée et de départ 
#l\' pour que ' ne soit pas considéré comme fin de string
hd = int(input("donner l\'heure de départ: "))
mnd = int(input("donner les minutes de départ: "))
print ("heure départ: ", (hd,mnd) )
ha = int(input("donner l\'heure arrivée: "))
mna=int(input("donner les minutes arrivée: " ))
print ("heure arrivée: ", (ha,mna) )
#convertir les heures en minutes et procéder à la différence arrivées et départ
mnDD = (hd*60) + mnd
mnAA = (ha*60) + mna
print ("heure départ en seconde : ", mnDD )
print ("heure arrivée en seconde : ", mnAA )

#convertir la différence minute en heure prendre le quotien comme heure et les restes comme mn 
duréeH = (mnAA - mnDD)//60
duréeM = (mnAA - mnDD)%60
print ( duréeH, duréeM )

#chercher la durée du trajet pour jour+1 (cad arrivée le jour d'après)

if mna > mnd :
    mnMN = (mna - mnd)
    hH = (ha - hd + 24) 
    print ("La duree du trajet : ", hH, mnMN )
else:
    mnMN = ((mna + 60) - mnd) 
    hH = (((ha - 1) - hd) + 24)
    print ("La duree du trajet : ", hH, mnMN )


