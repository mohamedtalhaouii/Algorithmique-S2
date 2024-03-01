# Question: Ecrire un programme qui lit l'heure et les minutes et affiche l'heure qu'il sera une minute plus tard.

# Lire l'heure et les minutes
heure = int(input("Donner l'heure: "))
minutes = int(input("Donner les minutes: "))
if heure < 0 or heure > 23 or minutes < 0 or minutes > 59:
	print("L'heure doit être entre 0 et 23 et les minutes devons être entre 0 et 59")
else:
	if minutes == 59:
		if heure == 23:
			heure = 0
		else:
			heure = heure + 1
		minutes = 0
	else:
		minutes = minutes + 1

	print("Dans une minute, il sera", heure, "heure(s)", minutes, "minute(s)");
