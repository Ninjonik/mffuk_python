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
cisla = [0] * pocet_cisel
for i in range(1, pocet_cisel + 1):
    cislo = daj_sem_dalsie_cislo()
    cisla[cislo - 1] = i

print(" ".join(str(cislo) for cislo in cisla))