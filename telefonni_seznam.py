import sys

class Vagon:
    def __init__(self, data, dalsi = None):
        self.data = data
        self.dalsi = dalsi

class Spojak:
    def __init__(self, hlava = None, ocas = None):
        self.hlava = hlava
        self.ocas = ocas

    def vloz(self, data):
        """
        Metóda vloží daný prvok na koniec spojáku.
        :param data: int
        :return: Vagon
        """
        novy_vagon = Vagon(data)

        if not self.hlava:
            self.hlava = novy_vagon
            self.ocas = novy_vagon
            return novy_vagon

        # pridaj vagón na koniec
        self.ocas.dalsi = novy_vagon
        self.ocas = novy_vagon
        return novy_vagon

    def vymaz(self, data):
        """
        Metóda vymaže daný prvok zo spojáku, ak sa v ňom nachádza.
        :param data: int
        :return: bool
        """
        if not self.hlava:
            return False

        if self.hlava.data == data:
            # nastav ocas na None, keď už nič v zozname nie je
            if not self.hlava.dalsi:
                self.ocas = None

            # nastav nasledovníka ako hlavu (môže byť aj None)
            self.hlava = self.hlava.dalsi
            return True

        current = self.hlava
        # dokým nie je current posledný prvok
        while current.dalsi:
            # ak current má ďalšieho nasledovníka takého, ktorého chceme zmazať
            if current.dalsi.data == data:
                # ak je nasledovník ocas (určite - je posledný)
                if not current.dalsi.dalsi:
                    self.ocas = current

                # nastav nasledovníka nasledovníka na nasledovníka current (aj None je OK)
                current.dalsi = current.dalsi.dalsi
                return True

            # nastav current na nasledovníka
            current = current.dalsi

        return False

    def __zoraduj(self, start = 0):
        """
        Privátna metóda nájde maximum od 0 až po koniec a toto maximum položí na začiatok spojáku.
        :param start: int
        :return: bool
        """
        if not self.hlava:
            return False

        # zoraď pomocou SelectSort
        # získaj prvok, od ktorého začíname
        start_vagon = self.hlava
        start_rodic = None

        for _ in range(start):
            if not start_vagon.dalsi:
                return False
            start_rodic = start_vagon
            start_vagon = start_vagon.dalsi

        # nájdi lokálne maximum
        current = start_vagon
        maximum = start_vagon
        maximum_rodic = start_rodic

        while current.dalsi:
            if current.dalsi.data > maximum.data:
                maximum_rodic = current
                maximum = current.dalsi
            current = current.dalsi

        # presuň maximum na start
        if maximum != start_vagon:
            # ak je maximum ocas, aktualizuj ocas
            if maximum == self.ocas:
                self.ocas = maximum_rodic if maximum_rodic else start_vagon

            # odpoj maximum z pôvodnej pozície, pripoj ďalší vagón
            if maximum_rodic:
                maximum_rodic.dalsi = maximum.dalsi

            # vlož maximum na start
            if start_rodic:
                start_rodic.dalsi = maximum
            else:
                self.hlava = maximum
            maximum.dalsi = start_vagon

        return True

    def __pocet_prvkov(self):
        """
        Privátna metóda vráti celkový počet prvkov vo spojáku.
        :return: int
        """
        current = self.hlava
        count = 0
        while current:
            count += 1
            current = current.dalsi

        return count

    def zorad(self):
        """
        Metóda zoradí celý spoják zostupne.
        :return: bool
        """
        count = self.__pocet_prvkov()
        res = False
        for i in range(count):
            # zoraď count-krát
            res = self.__zoraduj(i)
            if not res:
                return res

        return res


    def __str__(self):
        """
        Metóda vypíše aktuálne vagóny vo spojáku.
        :return: str
        """
        if not self.hlava:
            return ""

        current = self.hlava
        out = ""

        while current:
            out += f"{current.data}\n"
            current = current.dalsi

        # odstráň posledný linebreak
        return out.rstrip("\n")

seznam = Spojak()

for riadok in sys.stdin:
    riadok = riadok.strip()
    riadok = riadok.split(" ")

    operacia, argument = None, None

    if len(riadok) == 1:
        operacia = riadok[0]

    if len(riadok) == 2:
        operacia, argument = riadok

    if operacia:
        if operacia == "1" and argument:
            argument = int(argument)
            if argument > 0:
                seznam.vloz(argument)
        elif operacia == "2" and argument:
            argument = int(argument)
            if argument > 0:
                seznam.vymaz(argument)
        elif operacia == "4":
            seznam.zorad()
        elif operacia == "5":
            vystup = str(seznam)
            if vystup:
                print(vystup)
        elif operacia == "6":
            break