# Stack ,adding Pop function.
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("Popped value is: ", temp.data)
            self.top = self.top.next
            temp.next = None

    def print(self):
        if self.isempty():
            print("Stack is empty")
            return
        print("Stack contains.. ")
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next


s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.print()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.print()