#An e-commerce company maintains product IDs in a BST to enable efficient product searching.
# Tasks:
# 1. Create a BST using product IDs. Insert the following product IDs:150, 100, 200, 75, 125, 175, 250, 60, 90, 110.
# 2. Display product IDs in ascending order.
# 3. Search for product ID 175 exists.
# 4. Delete product ID 100.
# 5. Display the BST using inorder, preorder, and postorder traversals.
# 6. Find the minimum and maximum product IDs
class Node:
    def __init__(self, data):
        self.left = None
        self.pid = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.pid < temp.pid:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.pid, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.pid, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)
        self.postorder(rt.right)
        print(rt.pid, end=" ")

    def search(self, rt, val):
        if rt is None:
            return False
        if rt.pid == val:
            return True
        elif val < rt.pid:
            return self.search(rt.left, val)
        else:
            return self.search(rt.right, val)

    def Findminmax(self):
        if self.root is None:
            print("\nTree is empty")
            return
        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:", temp.pid)
        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:", temp.pid)

    def del_node(self, rt, val):
        if rt is None:
            return None
        if val < rt.pid:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.pid:
            rt.right = self.del_node(rt.right, val)
        else:
            # Node has no left child
            if rt.left is None:
                return rt.right
            # Node has no right child
            if rt.right is None:
                return rt.left
            # Node has two children(left and right)
            succ = self.get_successor(rt)
            rt.pid = succ.pid
            rt.right = self.del_node(rt.right, succ.pid)
        return rt

    def get_successor(self, rt):
        temp = rt.right
        while temp.left is not None:
            temp = temp.left
        return temp

b1 = BST()
b1.insert(Node(150))
b1.insert(Node(100))
b1.insert(Node(200))
b1.insert(Node(75))
b1.insert(Node(125))
b1.insert(Node(175))
b1.insert(Node(250))
b1.insert(Node(60))
b1.insert(Node(90))
b1.insert(Node(110))

# Display product IDs in ascending order
print("\nDisplay product IDs in ascending order:")
b1.inorder(b1.root)

# Search for product ID
val = int(input("\n\nSearch for product ID: "))
if b1.search(b1.root, val):
    print("ID found:", val)
else:
    print("ID not found:", val)

# Delete product ID 100
b1.root = b1.del_node(b1.root, 100)
print("\nAfter deleting 100:")
b1.inorder(b1.root)

# Display BST traversals
print("\n\nInorder:")
b1.inorder(b1.root)
print("\nPreorder:")
b1.preorder(b1.root)
print("\nPostorder:")
b1.postorder(b1.root)

# Find minimum and maximum product IDs
b1.Findminmax()
