# programme anneeBissextile 
'''
Faire un programme qui saisit une date (jour, mois et année) et qui indique si l’année est bissextile
''' 
#saisir l'année, si elles est multiple de 400 alors bissextile
an = int(input("Saisir une année"))
print (an)   
if (an > 1582) :
    if (an % 4 == 0) : #si elle est divisible par 4 alors bissextile  
        an = True
        print ("l'année est bissextile ")
    if (an % 400 == 0) : #si l'année est multiple de 400 alors bissextile
        an = True
        print ("l'année est bissextile " )
    if (an % 100 == 0) : #si l'année multiple de 100 alors n'est pas bissextile
        an = False
        print ("l'année n'est pas bissextille" )

