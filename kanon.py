from collections import deque

# Setup

"""
"""
mapa = [
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "X", "X", ".", ".", "."],
    [".", ".", "Z", "X", ".", ".", ".", "."],
    [".", ".", ".", "X", "B", ".", ".", "."],
    [".", ".", ".", "X", ".", ".", ".", "."],
    [".", ".", ".", "X", "X", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", "X", "X", ".", "."],
]
start = [2, 2]

"""
mapa = []
for i in range(8):
    mapa.append(list(input()))
"""
stlpce = 8
riadky = 8
original_mapa = list(mapa)

# n?jdi ?tart
start = None
for y in range(stlpce):
    for x in range(riadky):
        if mapa[y][x] == "Z":
            start = [x, y]


def ziskaj_tahy(pos):
    moves = []

    priame_smery = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dist_x, dist_y in priame_smery:
        next_x, next_y = pos[0] + dist_x, pos[1] + dist_y
        while 0 <= next_x < riadky and 0 <= next_y < stlpce:
            if mapa[next_y][next_x] == "X": break
            moves.append((next_x, next_y))
            next_x += dist_x
            next_y += dist_y

    diagonalne_smery = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dist_x, dist_y in diagonalne_smery:
        next_x, next_y = pos[0] + dist_x, pos[1] + dist_y
        if 0 <= next_x < riadky and 0 <= next_y < stlpce:
            if mapa[next_y][next_x] != "X":
                moves.append((next_x, next_y))

    return moves


fronta = deque([(start, 0)])
visited = {tuple(start)}
vysledok = -1

while fronta:
    curr, dist = fronta.popleft()

    for this_x, this_y in ziskaj_tahy(curr):
        if mapa[this_y][this_x] == "B":
            vysledok = dist + 1
            fronta.clear()
            break

        if (this_x, this_y) not in visited:
            visited.add((this_x, this_y))
            # Ozančenie dočasne čiste pre vizualizáciu
            if mapa[this_y][this_x] == ".": mapa[this_y][this_x] = str(dist + 1)[-1]
            fronta.append(([this_x, this_y], dist + 1))

# Vlna vizualizácia
for radek in mapa:
    print(" ".join(radek))

print(vysledok)