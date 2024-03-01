# Methode 1: utilisant une boucle
n=int(input("Donner la valeur de n: "))
somme=0
for i in range(0,n+1):
	somme += 2**i
print(somme)
# Methode 2: utilisant la formule de la somme des puissances de 2
n=int(input("Donner la valeur de n: "))
somme = 2**(n+1) - 1
print(somme)