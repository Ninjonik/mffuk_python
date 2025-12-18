def rozklady(n):
    def rozklad(i, zbytok):
        if zbytok == 0:
            print(r[1:i])
            # tisk(n, i, r[1:i])
        else:
            for j in range(1, min(zbytok, r[i-1]) + 1):
                r[i] = j
                rozklad(i + 1, zbytok - j)

    r = [n] * (n+1)
    rozklad(1, n)

def tisk(n,i,r):
    print(n, end=" = ")
    for j in range(i-2):
        print(r[j], end=" + ")
    print(r[i-2])

rozklady(7)