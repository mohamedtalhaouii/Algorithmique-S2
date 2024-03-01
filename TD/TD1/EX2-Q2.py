# Methode 1: en utilisant une boucle
x=float(input("Donner la valeur de x: "))
n=int(input("Donner la valeur de n: "))
resultat=1
for i in range(n):
	resultat*=x
print(resultat)
# Methode 2: en utilisant la fonction pow
x=float(input("Donner la valeur de x: "))
n=int(input("Donner la valeur de n: "))
x=pow(x,n)
print(x)