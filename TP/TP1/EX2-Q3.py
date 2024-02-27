S = 0
SC = 0
for i in range(1,6):
    #Demande
    N = float(input("entrer la note de la matier " + str(i) + " : " ))
    C = int(input("Son Coefficeint ? : "))
    #Calcule la somme des notes et des coefficients
    S = S + (N * C)
    SC = SC + C

M = S / SC
print("Le Moyenne est:", M)
