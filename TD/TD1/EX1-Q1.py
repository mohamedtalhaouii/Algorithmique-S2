# Question: Écrire un programme qui permute circulairement les valeurs de trois variables a, b et c.

# Lire les variables a, b et c
a = int(input("Donner la valeur de a: "))
b = int(input("Donner la valeur de b: "))
c = int(input("Donner la valeur de c: "))

# Effectuer la permutation circulaire:
temp = a
a = c
c = b
b = temp

# Écrire la resultat:
print("a = ", a, " , b = ", b, " et c = ", c)
