# programme calendrier 
'''
Faire un programme qui saisit une date (jour, mois et année) et qui indique si la date est valide
''' 
jr = input(print("Saisir un jour :"))
print(jr)
mo = input(print("Saisir un mois :"))
print(mo)
an = input(print("Saisir une année :"))
print(an)    
if an > "1589" and mo > "1" and mo <= "12" : 
        if (jr <= "31") and ( (mo == "1") or (mo == "3") or (mo == "5") or (mo == "7") or (mo == "8") or (mo == "12")):
            jr31 = True
        if (jr <= "30") and ( (mo == "4") or (mo == "6") or (mo == "9") or (mo == "11")) :
            jr30 = True
        if (jr <= "29") and (mo == "2") : 
            jr29 = True    
        print ("la date est valide :" )
else : 
        print ("la date n'est pas valide :" )   


