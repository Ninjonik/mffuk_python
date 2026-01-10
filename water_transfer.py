"""
Máme tři nádoby o celočíselných objemech a, b, c (čísla a, b, c nejsou větší než 10) ve kterých je na začátku objem x, y, z vody, v tomto pořadí.

Vodu můžeme přelévat z nádoby do nádoby, a to vždy tak, že nádobu kam lijeme, zcela zaplníme, nebo tak,
že nádobu odkud lijeme, zcela vyprázdníme. Objem přelité vody je určen tím, která z těchto variant nastane dříve.

Vodu nesmíme vylévat nikam jinam ani doplňovat z nějakého jiného zdroje.

Vstupem programu jsou po řadě čísla a, b, c, x, y, z udávající objemy a počáteční obsahy nádob.

Program vytiskne seznam všech objemů (včetně nuly, lze-li), kterých lze přeléváním dosáhnout
(celý objem vody v kterékoliv z nádob) a u každého z nich uvede za dvojtečkou minimální počet potřebných přelití.
Objemy v tomto seznamu budou vytištěny v rostoucím pořadí.


Příklad:

Vstup:
      4 1 1  1 1 1

Odpovídající výstup:
      0:1 1:0 2:1 3:2
"""

from collections import deque


def bfs(kapacita, voda):
    stavy_kroky = {}
    queue = deque()

    queue.append((voda, 0))  # (stav, počet krokov)
    stavy_kroky[voda] = 0

    while queue:
        aktualna_voda, kroky = queue.popleft()

        # prelievame z nádoby i do nádoby j
        for i in range(3):  # z ktorej nádoby
            for j in range(3):  # do ktorej nádoby
                if i == j:  # nemôžeme prelievať do sebe samej
                    continue

                # nový stav po preliatí
                novy_stav = list(aktualna_voda)

                # Môžeme preliať minimum z: voda v i, koľko sa zmestí do nádoby j
                preliatie = min(novy_stav[i], kapacita[j] - novy_stav[j])

                novy_stav[i] -= preliatie
                novy_stav[j] += preliatie
                novy_stav = tuple(novy_stav)

                # ak je stav nový, pridáme do fronty (na poradí nádob nezáleží)
                if novy_stav not in stavy_kroky:
                    stavy_kroky[novy_stav] = kroky + 1
                    queue.append((novy_stav, kroky + 1))

    stavy = {}  # stav -> min počet krokov

    for stav, kroky in stavy_kroky.items():
        for objem in stav:
            if objem not in stavy or kroky < stavy[objem]:
                stavy[objem] = kroky

    # Zatriedime lexikograficky
    vysledok = []
    for objem in sorted(stavy.keys()):
        vysledok.append(f"{objem}:{stavy[objem]}")

    print(" ".join(vysledok))


vstup = input().split()
a, b, c, x, y, z = map(int, vstup)

kapacita = (a, b, c)
voda = (x, y, z)

bfs(kapacita, voda)
