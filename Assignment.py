
def solution():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        # Create linked list
        def create(self, values):
            for value in values:
                self.insert_end(value)

        # Insert at the end
        def insert_end(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        # Display linked list
        def display(self):
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

        # Insert at a specific position (1-based)
        def insert_position(self, data, position):
            if position < 1:
                return
            new_node = Node(data)
            if position == 1:
                new_node.next = self.head
                self.head = new_node
                return
            temp = self.head
            for _ in range(position - 2):
                if temp is None:
                    return
                temp = temp.next
            if temp is None:
                return
            new_node.next = temp.next
            temp.next = new_node

        # Find middle node
        def middle(self):
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            if slow:
                print(slow.data)

        # Delete at a specific position
        def delete(self, position):
            if self.head is None or position < 1:
                return
            if position == 1:
                self.head = self.head.next
                return
            temp = self.head
            for _ in range(position - 2):
                if temp.next is None:
                    return
                temp = temp.next
            if temp.next is None:
                return
            temp.next = temp.next.next

        # Reverse linked list
        def reverse(self):
            previous = None
            current = self.head
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            self.head = previous

        # Sum of every two consecutive nodes
        def consecutive_sum(self):
            temp = self.head
            while temp and temp.next:
                print(temp.data + temp.next.data, end=" ")
                temp = temp.next
            print()

    # Main program
    ll = LinkedList()
    print("Enter number of nodes:")
    n = int(input())
    print("Enter node values: ")
    values = list(map(int, input().split()))
    ll.create(values[:n])
    print("Original list:")
    ll.display()
    print("Which position you want to insert:")
    position = int(input())
    print("Enter value to insert:")
    data = int(input())
    ll.insert_position(data, position)
    print("After inserted List:")
    ll.display()
    print("Middle node:")
    ll.middle()
    print("Enter delete position:")
    position = int(input())
    ll.delete(position)
    print("After deleted:")
    ll.display()
    ll.reverse()
    print("Reversed list:")
    ll.display()
    print("Consecutive sums:")
    ll.consecutive_sum()
    
if __name__ == "__main__":
    solution()
