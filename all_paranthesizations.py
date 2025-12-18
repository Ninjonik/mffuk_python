"""
Na vstupu je zadání číslo n<50 určující počet párů závorek, které máte k dispozici.
Vypište všechna platná uzávorkování s využitím těchto n párů závorek.
Uzávorkování je platné, pokud se nestane, že by některá otevírací závorka zůstala
nezavřená a současně ve výrazu není neotevřená zavírací závorka.
Uzávorkování vypisujte lexikograficky uspořádané tak, že otevírací závorka je
lexikograficky před závorkou uzavírací. Každé (platné) uzávorkování vypište na samostatný řádek.

Vstup: 2

Výstup:
(())
()()
"""

pocet_parov = int(input())

pocet_otvaracich = pocet_parov
pocet_zatvaracich = pocet_parov

def zavorkuj(pocet_otvaracich, pocet_zatvaracich, output):
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

out = zavorkuj(pocet_parov, pocet_parov,"")