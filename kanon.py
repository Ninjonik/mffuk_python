from collections import deque

"""
radek1 = [".", ".", ".", ".", ".", ".", ".", "."]
radek2 = [".", ".", ".", "X", "X", ".", ".", "."]
radek3 = [".", ".", "Z", "X", ".", ".", ".", "."]
radek4 = [".", ".", ".", "X", "B", ".", ".", "."]
radek5 = [".", ".", ".", "X", ".", ".", ".", "."]
radek6 = [".", ".", ".", "X", "X", ".", ".", "."]
radek7 = [".", ".", ".", ".", ".", ".", ".", "."]
radek8 = [".", ".", ".", ".", "X", "X", ".", "."]

mapa = [radek1, radek2, radek3, radek4, radek5, radek6, radek7, radek8]

"""

mapa = []
for i in range(8):
    mapa.append(list(input()))

stlpce = 8
riadky = 8

original_mapa = list(mapa)

# n?jdi ?tart
start = None
for y in range(stlpce):
    for x in range(riadky):
        if mapa[y][x] == "Z":
            start = [x, y]


def generuj_tahy(start, adding=True, vertical=True):
    def_tah = [0, 0]
    tah = [0, 0]
    i = 0
    to_return = []
    while True:
        if adding:
            i += 1
        else:
            i -= 1

        if vertical:
            novy_tah = [def_tah[0], def_tah[1] + i]
        else:
            novy_tah = [def_tah[0] + i, def_tah[1]]

        x, y = start[0] + novy_tah[0], start[1] + novy_tah[1]
        # print(x,y)

        # print(x, y, novy_tah, tah)

        # je mimo boundaries
        # print(x, y, novy_tah)
        if x > stlpce - 1 or x < 0 or y > riadky - 1 or y < 0:
            # print("mimo")
            break

        # je tam prek?ka
        if mapa[y][x] == "X":
            # print("prekazka")
            break

        # u? sme tam boli (je tam kanon)
        if mapa[y][x] == "K":
            # print("kanon")
            break

        # m?me tu cyklus
        if tah == novy_tah:
            # print("cyklus")
            break

        tah = novy_tah
        to_return_value = [start[0] + tah[0], start[1] + tah[1]]
        to_return.append(to_return_value)

    # if tah[0] == 0 and tah[1] == 0:
    # return None

    return to_return


diagonalne_mozne_tahy = [[-1, -1], [-1, 1], [1, 1], [1, -1]]


def validuj(start):
    global mapa
    validne_tahy = []

    vertikalne_nadol = generuj_tahy(start, True, True)
    vertikalne_nahor = generuj_tahy(start, False, True)
    horizontalne_doprava = generuj_tahy(start, True, False)
    horizontalne_dolava = generuj_tahy(start, False, False)

    validne_tahy = validne_tahy + vertikalne_nadol + vertikalne_nahor + horizontalne_dolava + horizontalne_doprava

    for tah in diagonalne_mozne_tahy:
        # nov? poz?cia x a y
        x, y = start[0] + tah[0], start[1] + tah[1]

        # je mimo boundaries
        if x > stlpce - 1 or x < 0 or y > riadky - 1 or y < 0:
            continue

        # je tam prek?ka
        if mapa[y][x] == "X":
            continue

        # u? sme tam boli
        if mapa[y][x] == "K":
            continue

        # m?me boji?te
        if mapa[y][x] == "B":
            return [[x, y]]

        validne_tahy.append([x, y])

    return validne_tahy


fronta = deque()
info = (start, 0)
fronta.append(info)
vysledok = -1

while len(fronta) > 0:
    data = fronta.popleft()
    start = data[0]
    length = data[1]

    # sme tam, kde treba, very good
    if mapa[start[1]][start[0]] == "B":
        if vysledok == -1 or length < vysledok:
            vysledok = length
            break

    # nastav aktualnu poziciu, ze sme tam uz boli
    mapa[start[1]][start[0]] = "K"

    validne_tahy = validuj(start)

    # ziadne validne tahy a nie sme ani tam, kde treba (konec)
    if len(validne_tahy) < 1:
        mapa[start[1]][start[0]] = "."
        vysledok = -1
        continue

    minimum = None
    for tah in validne_tahy:
        fronta.append((tah, length + 1))

print(vysledok)