# Student Priority Management
class Node:
    def __init__(self,name,id,pr):
        self.name=name
        self.id=id
        self.pr=pr
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=None

    def enqueue(self,node):
        if self.front==None or node.pr<self.front.pr:
            node.next=self.front
            self.front=node
            return
        temp=self.front
        while temp.next and temp.next.pr<=node.pr:
            temp=temp.next
        node.next=temp.next
        temp.next=node

    def display(self):
        temp=self.front
        while temp:
            print(temp.name,temp.id,temp.pr)
            temp=temp.next

    def dequeue(self):
        if self.front==None:
            print("Queue is empty")
        else:
            print("Removed student",self.front.name)
            self.front=self.front.next

    def display_next(self):
        if self.front==None:
            print("Queue is empty")
        else:
            print("Next student",self.front.name)


q=PriorityQueue()

q.enqueue(Node("Rahul",101,2))
q.enqueue(Node("Amit",102,1))
q.enqueue(Node("Sneha",103,3))
q.enqueue(Node("Priya",104,1))

print("All Students")
q.display()

print("Next Student")
q.display_next()

q.dequeue()

print("After Deletion")
q.display()
