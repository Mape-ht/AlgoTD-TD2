# programme moyenneEntier 
'''
Faire un programme qui calcule et affiche la division de a par b par soustractions successives
''' 
r = () #affecter la valeur 0 à reste r
i = 0
a = int(input(print("saisir un nombre entier")))
print(a) 
b = int(input(print("saisir un nombre entier")))
print(b) 

while r != 0 :
	r = a - b
	print (" ", a, "-", b, "=", r)
	a = r	
	i +=1
else:
	print ("le quotient de a-b est : ", i)


 