# Methode 1: utilisant une boucle
n=int(input("Donner la valeur de n: "))
somme=0
for i in range(1,n+1):
	somme+=i
print(somme)
# Methode 2: utilisant la formule des nombres triangulaire
n=int(input("Donner la valeur de n: "))
somme=n*(n+1)/2
print(somme)