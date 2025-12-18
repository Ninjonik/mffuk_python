import sys

def to_int_char(str_char):
    if(ord(str_char) >= 48 and ord(str_char) <= 57):
        return ord(str_char) - 48

    return None

def daj_sem_dalsie_cislo():
    char = sys.stdin.read(1)
    cislo = None
    # ked je medzi 0 vr?tane a 9 vr?tane v ASCII tabu?ke
    while(ord(char) >= 48 and ord(char) <= 57):
        if cislo is None: cislo = 0
        cislica = to_int_char(char)
        cislo = (cislo * 10) + cislica
        char = sys.stdin.read(1)

    if not cislo:
        return daj_sem_dalsie_cislo()

    return cislo

pocet_cisel = daj_sem_dalsie_cislo()
cisla = []

for i in range(pocet_cisel):
    cisla.append(daj_sem_dalsie_cislo())

current_i = len(cisla) - 1
previous_i = len(cisla) - 2
if previous_i < 0:
    neexistuje = True
else:
    neexistuje = False

while cisla[current_i] < cisla[previous_i]:
    current_i -= 1
    previous_i -= 1
    if previous_i < 0:
        neexistuje = True
        break

if neexistuje:
    print("NEEXISTUJE")
else:
    hranica = previous_i
    previous_i = len(cisla) - 1
    while cisla[hranica] > cisla[previous_i]:
        previous_i -= 1
        if previous_i < 0:
            previous_i = 0
            break

    cisla[hranica], cisla[previous_i] = cisla[previous_i], cisla[hranica]
    cisla[hranica + 1:] = reversed(cisla[hranica + 1:])
    for i in range(len(cisla)):
        cislo = cisla[i]
        print(cislo, end=" " if i < len(cisla) - 1 else "")