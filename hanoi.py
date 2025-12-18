"""
Naprogramujte, jak se maji prehazovat kotouce Ha-noiskych vezi.
Na vstupu prectete cislo n urcujici pocet kotoucu.
Vypiste posloupnost pokynu, jak prestehovat n kotoucu z prvni tyce na tyc druhou.
Instrukce piste stylem "Kotouc cislo_kotouce z cislo_tyce na cislo_tyce",
kde cislo_kotouce a poobakrat cislo_tyce jsou cisla.
Kazdou instrukci piste na zvlastni radek.
Tedy napriklad na vstup 2 vypisete tri radky a to:
"Kotouc 1 z 1 na 3" "Kotouc 2 z 1 na 2" a "Kotouc 1 z 3 na 2".
Predpokladejte, ze vstup se vejde do 32bitoveho integeru.

Hint: Kdy lze stehovat spodni kotouc? - skoro nikdy
Hint2: Odstehuj k-1 vezi stranou, prestehujte posledni kotouc, odstehujte k-1 na nej
"""

pocet_kotucov = int(input())

def ries_problemo(pocet_kotucov, odkud, kam, rezervni, id):
    if pocet_kotucov == 1:
        print(f"Kotouc {id} z {odkud} na {kam}")
    else:
        ries_problemo(pocet_kotucov - 1, odkud, rezervni, kam, id - 1)
        ries_problemo(1, odkud, kam, rezervni, id)
        ries_problemo(pocet_kotucov - 1, rezervni, kam, odkud, id - 1)

ries_problemo(pocet_kotucov, 1, 2, 3, pocet_kotucov)