def rychle_umocnovanie(x, n):
    vysledok = 1
    while n > 0:
        print(x, n, n % 2 == 1, vysledok)
        if n % 2 == 1:
            vysledok = vysledok * x

        x, n = x * x, n // 2
        print(x, n, n % 2 == 1, vysledok)
        print("-----------------------------")

    return vysledok

# print(rychle_umocnovanie(3, 5))
print(rychle_umocnovanie(3, 13))