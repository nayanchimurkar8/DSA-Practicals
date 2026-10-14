#singly Circular linked list 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

    # Display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

        print("(back to head)")


# Main program
cll = CircularLinkedList()

n = int(input("Enter number of nodes: "))
for i in range(n):
    value = int(input("Enter Nodes: "))
    cll.append(value)


print("Circular Linked List:")
cll.display()
