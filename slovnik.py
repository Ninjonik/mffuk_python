class Vrchol:
    def __init__(self, index, data = None, lavy = None, pravy = None):
        self.lavy = lavy
        self.pravy = pravy
        self.index = index
        self.data = data

class Strom:
    def __init__(self, koren = None):
        self.koren = koren

    def search(self, index, start = None, first = False):
        # prvá iterácia
        if not start and first:
            start = self.koren

        # strom je prázdny
        if not self.koren and not start:
            return None

        # prvok nebol nájdený
        if not start:
            print("-----------------")
            return None

        # base case rekurzie, prvok nájdený
        if start and start.index == index:
            return start.data

        # patrí do pravej časti podstromu
        if index > start.index:
            return self.search(index, start.pravy)
        # patrí do ľavej časti podstromu
        else:
            return self.search(index, start.lavy)

    def insert(self, index, data, vrchol = None, first = False):
        if first:
            vrchol = self.koren

        if not vrchol:
            vrchol = Vrchol(index, data)
            # strom je prázdny
            if not self.koren:
                self.koren = vrchol
        # patrí doprava
        elif index > vrchol.index:
            vrchol.pravy = self.insert(index, data, vrchol.pravy)
        # patrí doľava
        elif index < vrchol.index:
            vrchol.lavy = self.insert(index, data, vrchol.lavy)

        return vrchol

    def __str__(self):
        out = []
        output = ""
        def ziskaj_vrcholy(koren):
            if not koren:
                pass
            else:
                # output += f"{(koren.index, koren.lavy.index if koren.lavy else "-", koren.pravy.index if koren.pravy else "-")} \n"
                lavy = ziskaj_vrcholy(koren.lavy)
                pravy = ziskaj_vrcholy(koren.pravy)
                out.append(f"{koren.index} {koren.lavy.index if koren.lavy else "-"} {koren.pravy.index if koren.pravy else "-"}")

        ziskaj_vrcholy(self.koren)
        return "\n".join(out)

strom = Strom()
strom.insert(2, "n", None, True)
strom.insert(0, "n", None, True)
strom.insert(4, "o", None, True)
strom.insert(1, "i", None, True)
strom.insert(3, "g", None, True)
strom.insert(5, "r", None, True)

print(strom.search(0, None, True))
print(strom.search(1, None, True))
print(strom.search(2, None, True))
print(strom.search(3, None, True))
print(strom.search(4, None, True))
print(strom.search(5, None, True))