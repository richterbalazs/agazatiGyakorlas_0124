def elso():
    print("I/A:")

    nev = input("\tMúzeum neve: ")
    latogato = input("\tLátogató neve: ")
    ertekeles = int(input("\tÉrtékelés(1-20): "))

    szamokJok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    if ertekeles < 0 or ertekeles == 0:
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles > 20:
        print("20 pont feletti értékelés nem elfogadható!", end="")
    else:
        print("I/B")
        print("\tKöszönjük az értékelést!", end="")
