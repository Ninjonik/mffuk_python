"""

Určete poslední dvě číslice zadané mocniny. Na prvním řádku vstupu je číslo a,

které je základem mocniny.

Na druhém řádku je zadaný exponent b. Zatímco základ je zadán v desítkové soustavě,

exponent je zadán v soustavě dvojkové.

Určete poslední dvojčíslí mocniny a^b. Povšimněte si, prosím, že neříkáme,

zda se zadaná čísla vejdou vůbec do nějakého datového typu (neřkuli do paměti).


Příklad:

Vstup:

111111111111111111111111111111111111111111111111111111111111111111

111111111111111111111111111111111111111111111111111111111111111111

Výstup:

31

Nápověda


Vstup načítejte po znacích s využitím


sys.stdin.read(1) (jak bylo vysvětleno na cvičení) a využijte Hornerovo schéma (ideálně alespoň dvakrát).

Po dvou týdnech (1. termin) odevzdaná řešení ručně vyhodnotím a přidám dalších (až) 6 bodů dle toho,

jak se budete (či nebudete) řídit těmito instrukcemi.


"""

import sys


def to_int_char(str_char):
    if ord(str_char) >= 48 and ord(str_char) <= 57:
        return ord(str_char) - 48

    return None


def daj_sem_dalsie_cislo(toNumber=True):
    char = sys.stdin.read(1)

    cislo = None

    je_zaporne = True if ord(char) == 45 else False

    # ked je medzi 0 vr?tane a 9 vr?tane v ASCII tabu?ke

    while ((ord(char) >= 48 and ord(char) <= 57) or ord(char) == 45):

        if ord(char) == 45:
            char = sys.stdin.read(1)
            continue

        if toNumber:

            if cislo is None:
                cislo = 0

            cislica = to_int_char(char)

            cislo = (cislo * 10) + cislica

        else:

            if cislo is None:
                cislo = ""

            cislica = char

            cislo += cislica

        char = sys.stdin.read(1)

    if not cislo:
        return daj_sem_dalsie_cislo()

    return cislo * -1 if je_zaporne else cislo


mocnenec = daj_sem_dalsie_cislo()
mocnitel = daj_sem_dalsie_cislo(False)

def mocnina_fn(mocnenec, mocnitel):
    je_zaporny = True if mocnenec < 0 else False
    if je_zaporny:
        mocnenec *= -1
    mocnenec %= 100
    vysledok = 1
    for bit in mocnitel:
        vysledok = (vysledok * vysledok) % 100
        if bit == "1":
            vysledok = (vysledok * mocnenec) % 100
    return 0 - vysledok if je_zaporny else vysledok

print(mocnina_fn(mocnenec, mocnitel))
