from fractions import Fraction
#Demande
print("pour résoudre cette équation ax + b = 0 ")
a = Fraction(input("Donner La Coefficient a : "))
b = Fraction(input("Donner La Coefficient b : "))
#resoudre l'équation:
x = -b/a
#Affichier la solution:
print("La solution est :", "X =", Fraction(x))