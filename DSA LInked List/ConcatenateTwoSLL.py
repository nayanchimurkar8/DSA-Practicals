# Concatenate two Singly Linked Lists
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at the end
    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    # Concatenate two linked lists
    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = list2.head

    # Display linked list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create first linked list
list1 = LinkedList()
list1.append(10)
list1.append(20)
list1.append(30)

# Create second linked list
list2 = LinkedList()
list2.append(40)
list2.append(50)
list2.append(60)

print("First Linked List:")
list1.display()

print("Second Linked List:")
list2.display()

# Concatenate both lists
list1.concatenate(list2)

print("After Concatenation:")
list1.display()
