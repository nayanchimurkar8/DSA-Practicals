class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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

    def reverse(self):
        temp = self.head
        prev_node = None
        while temp:
            prev_node = temp.prev
            temp.prev = temp.next
            temp.next = prev_node
            temp = temp.prev
        if prev_node:
            self.head = prev_node.prev

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
print("Original list:")
dll.display()
dll.reverse()
print("Reversed list:")
dll.display()
