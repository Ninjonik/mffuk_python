pole = [3, 45, 23, 23, 1 , 2, 43, 9, 8]

for i in range(len(pole)):
    j = i
    while j > 0 and pole[j] < pole[j - 1]:
        print(pole[j], "switch s ", pole[j - 1])
        pole[j], pole[j - 1] = pole[j - 1], pole[j]
        j -= 1

print(pole)