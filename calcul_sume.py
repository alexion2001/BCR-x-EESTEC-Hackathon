
f = open("test_sume.txt","r")
sume = {
    'venituri': 0,
    'mancare': 0,
    'transport': 0,
    'casa': 0,
    'diverse': 0}

for linie in f:
    linie_string = linie.split(",")
    nr=[]
    for l in linie_string:
        nr.append(float(l))

    if nr[1]==-1:
        sume['venituri']+=nr[0]
    elif nr[1]==0:
        sume['mancare']+=nr[0]
    elif nr[1]==1:
        sume['transport']+=nr[0]
    elif nr[1]==2:
        sume['casa']+=nr[0]
    elif nr[1]==3:
        sume['diverse']+=nr[0]
rest = sume['venituri']-sume['mancare']-sume['transport']-sume['casa']-sume['diverse']
print('venituri: ',sume['venituri'])
print('mancare: ',sume['mancare'])
print('transport: ',sume['transport'])
print('casa: ',sume['casa'])
print('diverse: ',sume['diverse'])
print('saracia mai are: ', rest)
