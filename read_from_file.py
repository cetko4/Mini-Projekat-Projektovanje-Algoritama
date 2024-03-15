import csv

#indexi
ime_grada = 1
ime_drzave = 7
populacija = 13

def citanje_iz_fajla():
    index = 0
    lista = []
    torka = ()
    nova = ()
    broj_gradova = 0
    with open('citypopulations.csv', 'r', encoding='utf8') as file_obj:
        heading = next(file_obj)
        lines = file_obj.readlines()
        for line in lines:
            if index <= 30000:
                elementi = line.split(';')
                if int(elementi[populacija]) > 0:
                    nova = (elementi[ime_grada], elementi[ime_drzave], int(elementi[populacija]))
                    broj_gradova += 1
                    torka = torka + nova
                    lista.append(torka)
                index += 1
                torka = ()
                nova = ()
    return lista, broj_gradova