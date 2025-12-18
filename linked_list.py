from typing import Optional

class Node:
    def __init__(self, hodnota = None, dalsi: 'Node' = None):
        self.head: Optional['Node'] = dalsi
        self.hodnota = hodnota

class LinkedList:
    def __init__(self):
        self.head: Optional['Node'] = None

    def __str__(self):
        pass

    def empty(self):
        return self.head is None

    def member(self, data):
        pom = self.head
        while pom.hodnota != data and pom.head:
            pom = pom.head

        if not pom.head:
            return None
        else:
            return pom.hodnota


    def push(self, item):
        if not self.head:
            self.head = Node(item, None)
        elif item <= self.head.hodnota:
            self.head = Node(item, self.head)
        else:
            pom = self.head
            while pom.head and pom.head.hodnota:
                pass


    def pop(self):
        if not self.head:
            return
        hodnota = self.head.hodnota
        self.head = self.head.dalsi
        return hodnota

nice = LinkedList()
nice.push(2)
nice.push(4)
nice.push(5)
nice.push(6)
print(nice)
nice.pop()
nice.pop()
print(nice)

