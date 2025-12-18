import sys

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

    def pop(self):
        if not self.hlava:
            return
        data = self.hlava.data
        self.hlava = self.hlava.next
        return data

spojak = Spojak()
cisla = []

def to_int_char(ch):
    if '0' <= ch <= '9':
        return ord(ch) - ord('0')
    return None

def daj_sem_dalsie_cislo():
    char = sys.stdin.read(1)
    while char != '' and to_int_char(char) is None:
        char = sys.stdin.read(1)

    if char == '':
        return None

    cislo = 0
    while char != '' and (digit := to_int_char(char)) is not None:
        cislo = cislo * 10 + digit
        char = sys.stdin.read(1)

    return cislo


n = daj_sem_dalsie_cislo()
while n is not None:
    cisla.append(n)
    spojak.insert(n)
    n = daj_sem_dalsie_cislo()

for i in range(len(cisla)):
    print(spojak.pop(), end=" " if i < len(cisla) - 1 else "")
print()
