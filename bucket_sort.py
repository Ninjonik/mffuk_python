import sys

def to_int_char(str_char):
    if(ord(str_char) >= 48 and ord(str_char) <= 57):
        return ord(str_char) - 48

    return None

def daj_sem_dalsie_cislo():
    char = sys.stdin.read(1)
    cislo = None
    # ked je medzi 0 vr?tane a 9 vr?tane v ASCII tabu?ke
    while(ord(char) >= 48 and ord(char) <= 57):
        if cislo is None: cislo = 0
        cislica = to_int_char(char)
        cislo = (cislo * 10) + cislica
        char = sys.stdin.read(1)

    if not cislo:
        return daj_sem_dalsie_cislo()

    return cislo

pocet_cisel = daj_sem_dalsie_cislo()
cisla = []
for i in range(pocet_cisel):
    cisla.append(daj_sem_dalsie_cislo())

priehradky = [ [] for _ in range(10)]
for i in range(9):
    for cislo in cisla:
        aktualna_cifra_hodnota = (cislo % ((10 ** (i + 1))) // (10 ** i))
        priehradky[aktualna_cifra_hodnota].append(cislo)

    cisla = []
    for priehradka in priehradky:
        for key, cislo in enumerate(priehradka):
            print(cislo, end=" " if key != pocet_cisel - 1 else "")
            cisla.append(cislo)
    if i != 9:
        print("\n", end="")

    priehradky = [[] for _ in range(10)]
