#Methode 1 :
from math import sqrt

a = int(input("Donner un nombre positif : "))
r = int(sqrt(a))

print("la racine carre de", a ,"est :", r )

#Methode 2 :
def sqrt():
    #Demander
    N = int(input("Donner un nombre positif :"))
    R = N **(1/2)
    #affichier
    return print("Le Racine Rarre de ", N ,"est : ",R)
#L'appel de la fonction sqrt()
sqrt()
