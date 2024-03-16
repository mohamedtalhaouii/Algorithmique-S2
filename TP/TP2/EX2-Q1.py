#L'aire A d'un trapèze dont les bases sont B1 et B2 et dont la hauteur est H est : A=((B1+B2)×H) / 2

def surface():
    return ((B1+B2)*H)/2


B1 = float(input("Entrer la Base 1 : "))
B2 = float(input("Entrer la Base 2 : "))
H = float(input("Entrer l'Hauteur : "))

print("La Surface de trapèze est : ", surface())