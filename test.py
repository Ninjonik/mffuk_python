import sys



def daj_sem_dalsie_cislo():
    char = sys.stdin.read(1)
    cislo = None
    while "0" <= char <= "9":
        if cislo is None:
            cislo = 0

        char = ord(char) - 48
        cislo = (cislo * 10) + char
        char = sys.stdin.read(1)

    if cislo is None:
        return daj_sem_dalsie_cislo()

    return cislo