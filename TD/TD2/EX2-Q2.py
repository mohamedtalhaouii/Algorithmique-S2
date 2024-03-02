import random

#fonction qui simule le jeu de dè:
def Dice():
    N = [1, 2, 3, 4, 5, 6]
    random.shuffle(N)
    return N[1]
#Appel d'un fonction
print(Dice())