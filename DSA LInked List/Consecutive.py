#print sum of 2 consecutive nodes in a linked list
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        print("List elements:")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

# Sum of every 2 consecutive nodes(sum of every 2 numbers)
    def sum_consecutive(self):
        temp = self.head
        while temp and temp.next:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


# Create linked list
list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(50))
list.append(Node(60))
list.print()

print("Sum of consecutive nodes:")
list.sum_consecutive()