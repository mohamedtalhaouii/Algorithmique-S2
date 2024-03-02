import random

#La fonction qui simule le jeu de dè: 
def Dice():
    N = [1, 2, 3, 4, 5, 6]
    random.shuffle(N)
    return N[1]

Fois = 0
while 1 == 1:
    Play = str(input("Entrer 'R' Pour Jouer et 'S' Pour Arreter : "))
    #Affiche la face:
    if Play == "R" :
        Fois = Fois + 1
        print(Dice())
    #Le Nbr de fois lorsqu'on arreter:
    if Play == "S":
        print("Le nombre de fois est :", Fois )
        break
