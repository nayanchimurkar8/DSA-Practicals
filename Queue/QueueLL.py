
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LQueue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_Node):
        if self.rear:
            self.rear.next=new_Node
            self.rear=new_Node
        else:
            self.front=self.rear=new_Node

    def dequeue(self):
        temp=self.front
        print("delete node: ",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Queue is empty")
            self.rear=None
        temp=None
        
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()
que=LQueue()
que.enqueue(Node(20))
que.enqueue(Node(30))
que.enqueue(Node(40))
que.enqueue(Node(50))
que.print()

que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()






            