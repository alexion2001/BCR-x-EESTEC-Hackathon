
f = open("test_sume.txt","r")
sume = {
    1: 0, #venit
    2: 0, #mancare
    3: 0, #transport
    4: 0, #casa
    5: 0  #diverse
}
total_chetuieli=0
for linie in f:
    linie_string = linie.split(",")
    nr=[]
    for l in linie_string:
        nr.append(float(l))

    if nr[1]==-1:
        sume[1]+=nr[0]
    elif nr[1]==0:
        sume[2]+=nr[0]
    elif nr[1]==1:
        sume[3]+=nr[0]
    elif nr[1]==2:
        sume[4]+=nr[0]
    elif nr[1]==3:
        sume[5]+=nr[0]
    if nr[1]!=-1:
        total_chetuieli += nr[0]
def calculProcent(categorie):
    if(categorie!=1):
        for i in range(len(sume)+1):
            if categorie == i:
                return sume[i]/total_chetuieli*100
    else:
        return -1

