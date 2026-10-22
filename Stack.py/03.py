# Stack Reverse implementation in  LL.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse(self):
        prev = None
        current = self.top
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.top = prev

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Original Stack:")
s.display()
s.reverse()
print("Reversed Stack:")
s.display()