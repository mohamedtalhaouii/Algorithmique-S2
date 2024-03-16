
def SommePremiers(N):
    S = 0
    if N > 0:
        for i in range(N+1):
            if (i % 3 != 0 and i % 2 == 0):
                S = S + i
    return S

N = int(input("Entrer un Nombre Positive : "))
print("La Somme des Nombres est : ", SommePremiers(N))