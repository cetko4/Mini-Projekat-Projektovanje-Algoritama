from read_from_file import citanje_iz_fajla
from sortiranje import sort


lista, broj_gradova = citanje_iz_fajla()
print(lista)
print("Broj gradova:", broj_gradova)

sort(lista)
print(lista)

duzina = len(lista) - 1
print("Grad sa najvise stanovnika je ", lista[duzina][0], " iz drzave ", lista[duzina][1], " sa ", lista[duzina][2], " stanovnika")
print("Drugi grad sa najvise stanovnika je ", lista[duzina-1][0], " iz drzave ", lista[duzina-1][1], " sa ", lista[duzina-1][2], " stanovnika")
print("Treci grad sa najvise stanovnika je ", lista[duzina-2][0], " iz drzave ", lista[duzina-2][1], " sa ", lista[duzina-2][2], " stanovnika")
print("2024. grad sa najvise stanovnika je ", lista[2023][0], " iz drzave ", lista[2023][1], " sa ", lista[2023][2], " stanovnika")

for i in range(len(lista)-1):
    if lista[i][0] == 'Novi Sad':
        print("Broj stanovnika Novog Sada je ", lista[i][2])
    if lista[i][0] == 'Sremska Mitrovica':
        print("Broj stanovnika Sremske Mitrovice je ", lista[i][2])

