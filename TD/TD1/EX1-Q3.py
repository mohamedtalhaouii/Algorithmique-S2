# Question: Ecrire un programme qui demande à l’utilisateur de donner un nombre compris entre 10 et 20.

convienne = False
while not convienne:
	nombre = int(input("Donner un nombre compris entre 10 et 20: "))
	if nombre > 20:
		print(" Plus petit ! ")
	else:
		if nombre < 10:
			print(" Plus grand ! ")
		else:
			convienne = True
