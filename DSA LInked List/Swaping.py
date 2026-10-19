#write a function to swap first & last node in DLL.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return
        first = self.head
        last = self.head
        while last.next:
            last = last.next
        first.data, last.data = last.data, first.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

ll = DoublyLinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Before swapping:")
ll.display()

ll.swap_first_last()

print("After swapping:")
ll.display()
