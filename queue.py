class CyclicQueue:
    data = []
    zacatek = 0
    pocet = 0
    kapacita = 0

    def __init__(self, kapacita):
        self.data = [None] * kapacita
        self.kapacita = kapacita
        self.zacatek, self.pocet = 0, 0

    def __str__(self):
        return str(self.data[self.zacatek:])

    def push(self, item):
        if self.pocet == self.kapacita:
            raise IndexError("ur mom too fat L bozo + ratio")

        self.data[(self.zacatek + self.pocet) % self.kapacita] = item

    def pop(self):
        if self.pocet == 0:
            raise IndexError("nice")

        self.pocet -= 1
        item = self.data[self.zacatek]
        self.zacatek = (self.zacatek + 1) % self.kapacita
        return item


nice = CyclicQueue(4)
nice.push(2)
nice.push(4)
nice.push(5)
nice.push(6)
print(nice)
nice.pop()
nice.pop()
print(nice)

