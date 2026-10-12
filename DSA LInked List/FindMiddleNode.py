
def solution():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_end(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node

        def create(self, values):
            for value in values:
                self.insert_end(value)

        # Display linked list
        def display(self):
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

        # Find middle node
        def middle(self):
            slow = self.head
            fast = self.head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            if slow:
                print("Middle node:", slow.data)

    ll = LinkedList()
    ll.create([10, 20, 30, 40, 50])
    ll.display()
    ll.middle()

solution()
