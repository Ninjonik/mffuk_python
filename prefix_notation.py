from collections import deque

"""

Napište program, který vyhodnotí zadaní výraz v polské reverzní (prefixové) notaci, případně napíše, že je výraz chybný.
Vstupem programu je právě jeden řádek se zadaným výrazem. Výraz se skládá z operátorů +, -, * a / a celých čísel. 
Všechny operátory i čísla jsou navzájem odděleny mezerami.
Můžete předpokládat, že všechna čísla včetně všech mezivýsledků se vejdou do datového typu longint.
Operátor / představuje celočíselné dělení. Pokud by mělo dojít k dělení nulou, vypište, že se jedná o chybný výraz.
Výstupem programu je jedno celé číslo, které představuje hodnotu výrazu (nebo slovo CHYBA.

Příklad 1:

Vstup:
/ + 1 2 2 

Výstup:
1

Jak to vyhodnotit? Stejne jako infixová (najdi poslední operátor)
^ To je pri prefixove notace trivialni!
U pref. notace není operátor prímo za číslem
Zakladni krok - cislo, rek. krok: operator
"""

vstup = deque(input().split(" "))

def vyhodnot_vyraz(vyraz):
    if not vyraz or vyraz == "":
        raise Exception

    retazec = vyraz.popleft()
    try:
        retazec = int(retazec)
        return retazec
    except:
        if retazec in "+-*/":
            lavy = vyhodnot_vyraz(vyraz)
            pravy = vyhodnot_vyraz(vyraz)

            if retazec == "+":
                return lavy + pravy
            elif retazec == "-":
                return lavy - pravy
            elif retazec == "*":
                return lavy * pravy
            elif retazec == "/":
                if pravy == 0:
                    raise Exception
                return lavy // pravy
        else:
            raise Exception

try:
    vysledok = vyhodnot_vyraz(vstup)

    # zostali nejaké nevyužité veci
    if len(vstup) > 0:
        print("CHYBA")
    else:
        print(vysledok)
except:
    print("CHYBA")



