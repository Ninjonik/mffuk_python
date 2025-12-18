"""
V této úloze budete pro zadanou šachovnici a zadanou pozici jezdce na šachovnici rozhodovat,
zda může jezdec postupně projít celou šachovnici tak, aby každé její pole navštívil právě jednou.

Ze standardního vstupu přečtěte 4 kladná celá čísla oddělena mezerami:
m n sx sy

Čísla splňují podmínky:
m < 20
n < 20
sx <= m
sy <= n.

Startovní pole jezdce je dáno souřadnicemi [sx, sy], indexování od 1. Rozměry šachovnice jsou m sloupců krát n řádků.
Úkolem je odpovědět na otázku, zda existuje posloupnost m*n-1 tahů jezdcem takových,
že na žádné pole šachovnice jezdec nevstoupí dvakrát. Požadovaný výstup (na stdout) je řetězec ANO nebo NE.

Příklad vstupu:
3 3 2 1

Správný výstup:
NE

Příklad vstupu:
5 5 2 1

Správný výstup:
NE

Příklad vstupu:
10 3 1 1

Správný výstup:
ANO

Rada: Použijte rekurzi.
"""
import copy

stlpce, riadky, sx, sy = map(int, input().split(" "))
sx, sy = sx - 1, sy - 1

matica = [[False for stlpec in range(stlpce)] for riadok in range(riadky)]

mozne_tahy = [[-1, 2], [1, 2], [-1, -2], [1, -2], [-2, 1], [2, 1], [-2, -1], [2, -1]]
def validuj(start, matica):
    validne_tahy = []

    for tah in mozne_tahy:
        x, y = start[0] + tah[0], start[1] + tah[1]
        if x > stlpce - 1 or x < 0 or y > riadky - 1 or y < 0:
            continue

        if matica[y][x]:
            continue

        validne_tahy.append([x, y])

    return validne_tahy


def rekurzuj(start, matica):
    matica[start[1]][start[0]] = True

    validne_tahy = validuj(start, matica)

    if len(validne_tahy) < 1:
        # pozri, či bola celá matica zaplnená -> True, inak False
        for radek in matica:
            for sloupec in radek:
                if not sloupec:
                    matica[start[1]][start[0]] = False
                    return False

        return True

    for tah in validne_tahy:
        vysledok = rekurzuj(tah, matica)
        if vysledok:
            return True

    # žiadny ťah nebol úspešný - backtrack
    matica[start[1]][start[0]] = False
    return False

res = rekurzuj([sx, sy], matica)
print("ANO" if res else "NE")
