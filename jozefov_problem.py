"""
Při dobývání Tróje byla hrstka obránců zahnána řeckými válečníky do polorozbořené budovy chrámu a obklíčena.
Aby unikli ponižující porážce, rozhodli se Trójané spáchat sebevraždu.
Stoupli si do kruhu, přiřadili si čísla a ob jednoho postupně nalehli na svůj meč.
Začali vynecháním vojáka s číslem 1 a pokračovali v kruhu tak dlouho, dokud nebyli všichni mrtví.
Jeden z Trójanů, říkejme mu Josef, ale s tímto postupem nesouhlasil a mnohem radši by se vzdal Řekům a zachránil si život.
Poraďte Josefovi, na jaké místo v kruhu si má stoupnout,
aby při rozpočítávání zůstal jako poslední a nikdo z Trójanů se tak nedozvěděl o jeho potupě.

Na standardním vstupu dostanete jedno celé číslo N v rozsahu typu longint - počet trójských vojáků.
Vypište na standardní výstup celé číslo J(N) - místo v kruhu, na které si má Josef stoupnout.
Při nekorektním vstupu vypište pouze řetězec 'ERROR'.

Pro N = 5 probíhá tedy vyřazování takto:

    1 2 3 4 5 => 1 3 4 5 (vypadl voják 2)
    1 3 4 5 => 1 3 5 (vypadl voják 4)
    1 3 5 => 3 5 (vypadl voják 1)
    3 5 => 3 (vypadl voják 5)
    J(N) = 3

Příklad 1:
Vstup_
  37
Výstup
  11

Příklad 2:
Vstup:
  -5
Výstup:
  ERROR

"""

vstup = int(input())

def je_parne(n):
    if n % 2 == 0:
        return True
    else:
        return False

def rekurzuj(n, counter, zabijam_prveho = False):
    counter += 1

    if n == 0:
        return -1

    if n == 1:
        #print("end", counter)
        return 1

    if zabijam_prveho:
        zabijam = "liche"
    else:
        zabijam = "sude"

    vysl = 0
    if je_parne(n):
        vysl = rekurzuj(n // 2, counter, zabijam_prveho)
    else:
        vysl = rekurzuj(n // 2 if zabijam_prveho else n // 2 + 1, counter, not zabijam_prveho)

    #print(f"zabijam {zabijam}, carry {zabijam_prveho}, n {n} returním {vysl * 2 + (-1 if zabijam_prveho else 0)}")
    return vysl * 2 + (0 if zabijam_prveho else -1)

vysledok = (rekurzuj(vstup, 0))
if vysledok < 1:
    print("ERROR")
else:
    print(vysledok)