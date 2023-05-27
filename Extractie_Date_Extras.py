import pandas as pd
extras = pd.read_csv("extras/extras1.csv")
detalii_tranzactii=[]
detalii_tranzactii.append(extras["Transaction's details"]) #[0]
detalii_tranzactii.append(extras["Debit (amount)"]) #[1]
detalii_tranzactii.append(extras["Credit (amount)"]) #[2]
venituri=0.0
cheltuieli=[]
sum_chelt=0.0
# eliminarea virgulei din sumele cu mi(1,432.45)
# trasformarea in float
detalii_tranzactii[1] = detalii_tranzactii[1].str.replace(',', '').astype(float)
detalii_tranzactii[2] = detalii_tranzactii[2].str.replace(',', '').astype(float)
# for i in range(len(detalii_tranzactii[1])):
#     detalii_tranzactii[1][i] = float(detalii_tranzactii[1][i].replace(',',''))
#
# for i in range(len(detalii_tranzactii[2])):
#     detalii_tranzactii[2][i] = float(detalii_tranzactii[2][i].replace(',',''))

# for detaliu in detalii_tranzactii[0]:
for index, detaliu in enumerate(detalii_tranzactii[0]):
    # extragerea locatiei in care s-a facut plata
    tranz_index = detaliu.find('Locatie: ')
    last = detaliu.find('.', tranz_index)
    tranz_index += 21
    detaliu = detaliu[tranz_index:]
    tranz = ""
    i = 0
    while i < last - tranz_index:
        tranz += detaliu[i]
        i += 1
    if detalii_tranzactii[1][index] == 0:
        venituri+=detalii_tranzactii[2][index]
    else:
        if tranz:
            tranz_data=(tranz,detalii_tranzactii[1][index])
            cheltuieli.append(tranz_data)
            sum_chelt += detalii_tranzactii[1][index]
    # break
for i in cheltuieli:
    print(i)