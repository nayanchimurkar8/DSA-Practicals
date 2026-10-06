#singly Linear Linked List
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        if(self.head==None):
            self.head = new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node #append new node at the end
    def print(self):
        temp = self.head
        while temp.next:
            print(temp.data)
            temp = temp.next.next
        if temp:
            print(temp.data)

list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))
list1.append(Node(50))  
list1.print()
