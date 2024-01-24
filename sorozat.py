import random

def lista_letrehoz():
    lista = []
    for index in range(0, 15, 1):
        vSzam = random.randint(-90, 500)
        lista.append(vSzam)
    return lista

def kiir_lista(lista):
    print("II/A, B, C")
    print("\t", end="")
    # utolsó elemnek a megkülönböztetése
    print(lista[0], end="")
    for index in range(1, len(lista), 1):
        print(f"*{lista[index]}", end="")

def tizzel_oszthatok(lista):
    db = 0
    for index in range(0, len(lista), 1):
        if lista[index] % 10 == 0:
            db += 1
    return db

def konzolra_kiir(db):
    print("\nII/D, E")
    print(f"\t A 10-el oszthatóak száma: {db}")

def fajl_kiir(db):
    kiFajl = open("kimutatas.txt", "w", encoding="utf-8")
    print("II/F: ")
    print(f"Tizzel oszthatóak száma: {db}", file=kiFajl)
    kiFajl.close()

def masodikfeladat():
    szamok = lista_letrehoz()
    kiir_lista(szamok)
    tizzel_oszthatok(szamok)
    db = tizzel_oszthatok(szamok)
    konzolra_kiir(db)
    fajl_kiir(db)