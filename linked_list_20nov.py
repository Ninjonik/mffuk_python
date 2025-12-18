class Vagon:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

# je to usporadany spojak
class Spojak:
    def __init__(self):
        self.hlava = None

    def member(self, co):
        pass

    def insert(self, co):
        if not self.hlava or self.hlava.data >= co: # seznam prazdny nebo vkladame prvni do neprazdneho
            self.hlava = Vagon(co, self.hlava)
            return
        pom = self.hlava # pomocna
        while pom.next and pom.next.data < co:
            pom = pom.next

        pom.next = Vagon(co, pom.next)

    # pripady ktere muzou nastat
    """
    1. obecny
    2. neni tam
    2b mažeme větší než maximum
    3. vice vyskytu
    4. mažeme prvni
    5. mažeme posledni
    6. mažeme menší než minimum
    7. žádny prvek není v seznamu
    """
    def delete(self, co):
        if not self.hlava or self.hlava.data > co:
            return
        if self.hlava.data == co:
            self.hlava = self.hlava.next
            return
        pom = self.hlava
        while pom.next.data != co and pom.next != none:
            pom = pom.next

        if pom.next != None:
            pom.next = pom.next.next

def merguj(self, prvni, druhy):
    vysl = Vagon("hlava") # vysledny spojovy seznam
    posl = vysl
    while prvni.hlava and druhy.hlava:
        if prvni.hlava.data <= druhy.hlava.data:
            posl.next = prvni.hlava
            prvni.hlava = prvni.hlava.next
            posl = posl.next
        else:
            posl.next = druhy.hlava
            posl = posl.next
            druhy.hlava = druhy.hlava.next
        if not prvni.hlava:
            posl.next = druhy.hlava
        else:
            posl.next = prvni.hlava

        return vysl.next