import sys


def daj_sem_dalsie_cislo():
    cislo = None
    while True:
        char = sys.stdin.read(1)
        if char == '':
            return None

        if '0' <= char <= '9':
            if cislo is None:
                cislo = ""
            cislo = cislo + char
        elif cislo is not None:
            return cislo


cisla = []

while True:
    n = daj_sem_dalsie_cislo()
    if n is None:
        break
    cisla.append(n)

for cislo in cisla:
    print(cislo)
