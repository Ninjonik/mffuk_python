class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)

        if not self.head:
            self.head, self.tail = new_node, new_node

        print(self.tail.value, value)

        self.tail.next = new_node
        self.tail = new_node
        return self.tail

    def dequeue(self, value):
        if not self.head or not self.tail:
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

f = LinkedList()
for i in range(10):
    f.enqueue(i)

print(f.dequeue(5))
print(f.dequeue(2))

print(f)