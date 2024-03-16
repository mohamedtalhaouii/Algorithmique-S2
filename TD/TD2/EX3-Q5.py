
def somme(N):
    S = 0
    for i in range(N+1):
        S = S + i
    return S


N = int(input("Entrer un nombre : "))
print("La Somme des nombres jusqu'a ", N ,"est : ", somme(N))