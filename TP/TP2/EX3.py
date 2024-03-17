Eleve = int(input("Entrer le nombre des eleves : "))
Notes = int(input("Entrer le nombre des notes : "))

T = [[] for _ in range(Eleve)]  
Moy = []

for i in range(Eleve):
    SN = 0
    for j in range(Notes):
        note = float(input("Enter La Note " + str(j+1) + " d'eleve " + str(i+1) + " : "))
        T[i].append(note)  
        SN = SN + note #La somme des Notes
    M = SN / Notes #La Moyenne des Notes
    Moy.append(M)

SMoy = 0
Nomb = 0
for i in range(Eleve):
    SMoy = SMoy + Moy[i] #La somme des Moyennes des notes
    MoyCls = SMoy / Eleve #La Moyenne de Classe
    
    if Moy[i] > MoyCls:
        Nomb = Nomb + 1 #Le Nombre des Notes Sup à La Moyenne

for i in range(Eleve):
    for j in range(Notes):
        Min = T[0][0]
        if Min > T[i][j]:
            Min = T[i][j]

#############################################################

print("Les Elements du tableau : ", T) #1

print("Le Nombre des Notes Sup à La Moyenne est : ", Nomb) #2

print("Le Minimum des elements du tableau est : ", Min) #3
