"""
Collatzovy posloupnosti
Collatzova posloupnost je posloupnost přirozených čísel taková, že číslo
následující po čísle n je:
• n/2 , když je n sudé, a
• 3n + 1, když liché.


vstup nezáporné celé číslo n

výstup seřazená čísla, pro která dojde Collatzova posloupnost jimi
začínající k jedničce do n kroků, a odpovídající počty kroků; mezi
čísly a počty kroků je tabulátor
"""

n = int(input())

d = {}
def collutzuj(balance, number: int):
    if number not in d:
        d[number] = f"{number}\t{n - balance}"

    if balance == 0:
        return

    next_number_left = number * 2
    next_number_right = (number - 1) // 3

    # ak je ďalšie číslo párne, tak sem mohlo dojsť, inak ne
    if next_number_left % 2 == 0:
        collutzuj(balance - 1, next_number_left)

    # ak je ďalšie číslo nepárne, tak sem mohlo dojsť, inak nie
    if ((number - 1) % 3 == 0) and next_number_right % 2 != 0:
        collutzuj(balance - 1, next_number_right)

collutzuj(n, 1)

for key in sorted(d):
    print(d[key])