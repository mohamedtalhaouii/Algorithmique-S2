# Question: Ecrire un programme qui demande à l’utilisateur de saisir deux entiers naturels n et p et qui affiche la valeur de C(n,p).
# Methode 1: (sans utiliser la fonction factoriel)
p = int(input("Donner la valeur de p: "))
n = int(input("Donner la valeur de n: "))
if n < 0 or p < 0 or n < p:
	print("p et n doit être des entiers naturel et n doit être superieur ou égale p")
else:
	n_factoriel = 1
	if n != 0 and n != 1:
		for i in range(1,n+1):
			n_factoriel = n_factoriel * i
	p_factoriel = 1
	if p != 0 and p != 1:
		for i in range(1,p+1):
			p_factoriel = p_factoriel * i
	n_moins_p_factoriel = 1
	if n-p != 0 and n-p != 1:
		for i in range(1,n-p+1):
			n_moins_p_factoriel = n_moins_p_factoriel * i
	resultat = n_factoriel / (p_factoriel * n_moins_p_factoriel)
	print(resultat)
# Methode 2: (en utilisant la fonction factoriel)
	def factoriel(n):
		for i in range(2,n):
			n = n * i
		return n
	p = int(input("Donner la valeur de p: "))
	n = int(input("Donner la valeur de n: "))
	if n < 0 or p < 0 or n < p:
		print("p et n doit être des entiers naturel et n doit être superieur ou égale p")
	else:
		resultat = factoriel(n) / (factoriel(p) * factoriel(n-p))
		print(resultat)