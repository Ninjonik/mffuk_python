class Stack:
    data = []

    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def push(self, item):
        return self.data.append(item)

    def pop(self):
        return self.data.pop()

nice = Stack()
nice.push(2)
nice.push(4)
nice.push(5)
nice.push(6)
print(nice)
nice.pop()
nice.pop()
print(nice)

