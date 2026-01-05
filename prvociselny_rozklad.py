def prvociselny_rozklad(n):
    if n <= 1:
        return {}

    rozklad = {}
    delitel = 2
    while n % delitel == 0:
        rozklad[delitel] = rozklad.get(delitel, 0) + 1
        n //= delitel

    delitel = 3
    while delitel * delitel <= n:
        while n % delitel == 0:
            rozklad[delitel] = rozklad.get(delitel, 0) + 1
            n //= delitel
        delitel += 2

    if n > 1:
        rozklad[n] = rozklad.get(n, 0) + 1

    return rozklad

print(prvociselny_rozklad(269))