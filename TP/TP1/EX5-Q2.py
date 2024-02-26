#Demande
x = int(input("Donner un premier nombre : "))
Operation = str(input("Entrer L'operation : "))
y = int(input("Donner un second nombre : "))


#Les Operations
if Operation == "+":
    resultat = x + y
    print(x, "+", y , "=" ,resultat )

elif Operation == "-":
    resultat = x - y
    print(x, "-", y , "=" ,resultat )

elif Operation == "*":
    resultat = x * y
    print(x, "*", y , "=" ,resultat )

elif Operation == "/":
#La Condition de la Dénominateur null
    if y == 0:
        y = int(input("Essayer d'entrer la second nombre non null : "))
    resultat = x / y
    print(x, "/", y , "=" ,resultat )

else:
    print("Erreur !")
