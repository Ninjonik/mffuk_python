import random

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node

        current = self.head
        while current.value <= value and current.next:
            current = current.next

        if current.value <= value:
            current.next = Node(value)
        else:
            current.next = Node(current.value, current.next)
            current.value = value
            return True

    def dequeue(self, value):
        if not self.head:
            return None

        current = self.head
        while current.value != value and current.next:
            current = current.next

        if current.value != value:
            return False
        else:
            current.value = current.next.value
            current.next = current.next.next
            return True

    def __str__(self):
        to_return = ""
        current = self.head
        to_return += str(current.value) + " "
        while current.next:
            current = current.next
            to_return += str(current.value) + " "

        return to_return

f = OrderedLinkedList()
random_numbers = []
for i in range(10):
    random_number = random.randint(1, 10)
    random_numbers.append(random_number)
    f.enqueue(random_number)

print(f)
print(random_numbers)

random_choice = random.choice(random_numbers)
f.dequeue(random_choice)

print(random_choice)
print(f)
