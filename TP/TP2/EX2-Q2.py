
def absolue(N):
    if N < 0:
        return -N
    else:
        return N

N = float(input("Entrer un nombre : "))
print("|",N,"| = ", absolue(N))