import sys
from collections import deque


def daj_sem_dalsie_cislo():
    char = sys.stdin.read(1)
    cislo = None
    while 48 <= ord(char) <= 57:
        if cislo is None:
            cislo = 0

        char = ord(char) - 48
        cislo = (cislo * 10) + char
        char = sys.stdin.read(1)

    if cislo is None:
        return daj_sem_dalsie_cislo()

    return cislo


a, b, c, x, y, z = daj_sem_dalsie_cislo(), daj_sem_dalsie_cislo(), daj_sem_dalsie_cislo(), daj_sem_dalsie_cislo(), daj_sem_dalsie_cislo(), daj_sem_dalsie_cislo()

kapacity = (a, b, c)
initial_state = (x, y, z)

fronta = deque([(initial_state, 0)])
visited = {initial_state}

# objem -> min_krokov
results = {}

while len(fronta) > 0:
    stav, krokov = fronta.popleft()

    for objem in stav:
        if objem not in results or results[objem] > krokov:
            results[objem] = krokov

    for i in range(3):
        for j in range(3):
            if i == j:
                continue

            mozem_preliat = min(stav[i], kapacity[j] - stav[j])
            if mozem_preliat > 0:
                novy_stav = list(stav)
                novy_stav[i] -= mozem_preliat
                novy_stav[j] += mozem_preliat
                novy_stav = tuple(novy_stav)

                if novy_stav not in visited:
                    visited.add(novy_stav)
                    fronta.append((novy_stav, krokov + 1))

for objem in sorted(results.keys()):
    print(f"{objem}:{results[objem]}", end=" ")