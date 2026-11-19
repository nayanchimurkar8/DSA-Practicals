# Reversing Queue using Stack
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self,node):
        node.next=self.top
        self.top=node

    def pop(self):
        if self.top==None:
            print("Stack is Empty")
        else:
            temp=self.top
            self.top=self.top.next
            temp.next=None
            return temp

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,node):
        if self.front==None:
            self.front=self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        if self.front==None:
            print("Queue is Empty")
        else:
            temp=self.front
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            temp.next=None
            return temp

    def display(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ")
            temp=temp.next

q=Queue()
s=Stack()

q.enqueue(Node(10))
q.enqueue(Node(20))
q.enqueue(Node(30))
q.enqueue(Node(40))

print("Original Queue")
q.display()
while q.front:
    s.push(q.dequeue())
while s.top:
    q.enqueue(s.pop())
print("\nReversed Queue")
q.display()
