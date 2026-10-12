class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,newnode):
        if self.head==None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode

    def insert(self,newnode):
        pos=int(input("enter position"))
        temp=self.head
        if pos==1:
            newnode.next=self.head
            self.head=newnode
        else:
            p=1
            temp=self.head
            while p!=pos:
                temp=temp.next
                p+=1
            temp.next=newnode
            newnode.next=temp.next

    def delete(self,val):
        temp=self.head
        if temp.data==val:
            self.head=self.head.next
            return
        while(temp):
            if temp.data==val:
                break
            else:
                prev=temp
                temp=temp.next
        if temp==None:
            print("value not there")
            return
        prev.next=temp.next
        temp=None

    def see(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def reverse(self):
        curr=self.head
        prev=None
        while(curr):
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        return prev

n1=Node(30)
n2=Node(40)
n3=Node(50)
list=LinkedList()
list.append(n1)
list.append(n2)
list.append(n3)
list.see()
list.delete(30)
list.see()

#sum of 2 consicutive nodes 