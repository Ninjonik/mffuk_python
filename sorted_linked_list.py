class Node:
    def __init__(self, data, next = None):
        self.next = next
        self.data = data

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)

        # list is empty
        if not self.head:
            self.head = new_node
            return new_node

        # compare list with the head nore first
        if self.head.data < new_node.data:
            new_node.next = self.head
            self.head = new_node
            return new_node

        # list is not empty
        current = self.head
        while current.next:
            # match, insert the node
            if current.next.data < new_node.data:
                new_node.next = current.next
                current.next = new_node
                break

            # no match, continue
            current = current.next
        else:
            # no match ever, add the node at the end of the list
            current.next = new_node

        return new_node

    def remove(self, data):
        # list is empty
        if not self.head:
            return False

        # compare with the head
        if self.head.data == data:
            self.head = self.head.next
            return True

        # list is not empty
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True

            # no match, continue
            current = current.next

        # no match ever found
        return False


    def __str__(self):
        current = self.head
        out = ""
        while current and current.next and current.data:
            out += f"{current.data} -> "
            current = current.next

        return out


ll = LinkedList()
ll.insert(2323)
ll.insert(88)
ll.insert(74)
ll.insert(984)
ll.insert(7)
ll.insert(90284)
ll.insert(2329233)

print(ll)

ll.remove(2323)
print(ll)
ll.remove(2329233)
print(ll)
ll.remove(74)
print(ll)