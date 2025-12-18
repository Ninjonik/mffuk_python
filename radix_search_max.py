halda = [3, 45, 23, 23, 1 , 2, 43, 9, 8]

for i in range(len(halda)):
    cislo = halda[i]

    # vybublej
    rodic_i = (i - 1) // 2
    while rodic_i >= 0 and halda[rodic_i] < cislo:
        halda[rodic_i], halda[i] = cislo, halda[rodic_i]
        i = rodic_i
        rodic_i = (rodic_i - 1) // 2

for i in range(len(halda)):
    # odeber minimum (switch min s poslednym)
    posledny = len(halda) - i - 1
    halda[0], halda[posledny] = halda[posledny], halda[0]

    # zabublej
    parent = 0
    left_i = 2 * parent + 1
    right_i = 2 * parent + 2

    while left_i < posledny:
        if right_i >= posledny:
            mensi_i = left_i
        else:
            mensi_i = left_i if halda[left_i] > halda[right_i] else right_i

        if halda[parent] < halda[mensi_i]:
            halda[mensi_i], halda[parent] = halda[parent], halda[mensi_i]
            parent = mensi_i
            left_i = 2 * parent + 1
            right_i = 2 * parent + 2
        else:
            break

print(halda)