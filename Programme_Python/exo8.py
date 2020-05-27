# programme equation
'''
=======================Sujet============================
Ecrire un algorithme permettant de résoudre une équation du second degré. 
Ax2 + bx + c = 0
========================================================
'''
a=float(input("Saisir la valeur de a", ))
b=float(input("Saisir la valeur de b", ))
c=float(input("Saisir la valeur de c", ))
print(a, b, c)  
if a==0 : 
    if b==0:
        print ("Pas de solution")
    else:
        s1 = float(-c/b)
print ("la solution est :", s1)
if a < 0 :
    print ("Pas de solution", )
    if a == 0 :
        s2 = (float(-b/a) * a )
else:
    d = float(pow(b,b)-(4 * a * c )
    if d < 0
        print ("Pas de solution", )
        if d = 0
        print float("La solution est ",-b/(2*a) )    
        if d > 0
        print ("Deux solutions existent", (-b-(sqrt(d)))/(2*a )), (-b+(sqrt(d)))/(2*a ))
         

