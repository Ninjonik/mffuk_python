class Uzel:
    """
    třída pro reprezentaci uzlu
    """

    def __init__(self, hodnota=None, dalsi=None):
        self.hodnota = hodnota
        self.dalsi = dalsi


class FrontaSpojovySeznam:
    """
    implementace ADT Fronta
    pomocí (cyklického) spojového seznamu
    """

    def __init__(self):
        """
        vytvoří prázdnou frontu
        """
        self.konec = None
        self.delka = 0

    def empty(self):
        """
        vrátí True je-li fronta prázdná
        """
        return self.delka == 0

    def enqueue(self, hodnota):
        """
        vloží prvek x na konec fronty
        """
        novy = Uzel(hodnota)  # vytvoř nový uzel
        if self.empty():
            novy.dalsi = novy  # vytvoř cyklickou frontu délky 1
        else:
            novy.dalsi = self.konec.dalsi  # nový odkazuje na hlavu
            self.konec.dalsi = novy  # původní koncový uzel odkazuje na nový
        self.konec = novy  # nový se stane koncovým uzlem
        self.delka += 1

    def dequeue(self):
        """
        odebere a vrátí prvek ze začátku fronty
        je-li fronta neprázdná
        """
        if self.delka == 0:  # fronta musí být neprázná
            raise IndexError("prázdná fronta")

        odebirany = self.konec.dalsi  # uzel k odebrání
        if self.delka == 1:
            self.konec = None  # fronta se vyprázdnila
        else:
            self.konec.dalsi = odebirany.dalsi  # přeskoč původní začátek
        self.delka -= 1
        return odebirany.hodnota

    def print(self):
        """
        Vytiskne prvky od začátku do konce fronty
        """
        delkaFronty = self.delka
        if delkaFronty > 0:
            p = self.konec.dalsi
            for i in reversed(range(delkaFronty)):
                print(p.hodnota, end=" ")
                p = p.dalsi


# testovaci data
f = FrontaSpojovySeznam()
for i in range(10):
    f.enqueue(i)

