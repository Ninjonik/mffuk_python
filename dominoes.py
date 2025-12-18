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
    cislo1, cislo2 = daj_sem_dalsie_cislo(), daj_sem_dalsie_cislo()
    cisla.append((cislo1, cislo2))

# domino: rekurze
# nacti_vstup
# nacti_kostku
# pridej_kostku <- zkusí všechná možná doplnění na začátku (který vlastně ani nepotřebujeme)

def rekurzuj(pocet_otvaracich, pocet_zatvaracich, output):
    # konec
    if pocet_otvaracich == 0 and pocet_zatvaracich == 0:
        # si list, tak vypis celu postupnost
        print(output)
        return output

    # musim pridat (
    if pocet_otvaracich == pocet_zatvaracich:
        output += "("
        return zavorkuj(pocet_otvaracich - 1, pocet_zatvaracich, output)

    # musim pridat )
    if pocet_otvaracich < 1:
        output += ")"
        return zavorkuj(pocet_otvaracich, pocet_zatvaracich - 1, output)

    # pridám (
    a = zavorkuj(pocet_otvaracich - 1, pocet_zatvaracich, output + "(")

    # pridám )
    b = zavorkuj(pocet_otvaracich, pocet_zatvaracich - 1, output + ")")

    return a + b

out = rekurzuj(pocet_parov, pocet_parov,"")


