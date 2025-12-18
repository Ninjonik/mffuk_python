from collections import deque

vstup = input()

zavorky = {
    ")": "(",
    "]": "[",
    ">": "<",
    "}": "{"
}

oteviraci_zavorky = zavorky.values()
zaviraci_zavorky = zavorky.keys()

zasobnik = deque()

for char in vstup:
    if char in oteviraci_zavorky:
        zasobnik.append(char)
    else:
        zacatek_zavorka = zasobnik.pop()
        if zavorky[char] != zacatek_zavorka:
            print("chyba")
            break
else:
    print("OK")
