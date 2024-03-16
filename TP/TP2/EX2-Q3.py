#Demand:
N = []
for i in range(3):
     N.append(int(input("Entrer un entier : ")))

#trouver le max:
def max():
    Max = N[0]
    for i in range(3):
        if  Max < N[i]:
            Max = N[i]
    return Max

#Afficher le max:
print("Le Max est : ", max())