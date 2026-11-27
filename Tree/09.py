#BST for traversal level wise.
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.cnt=0

    def insert(self, new_node):
        if self.root is None:
            self.root=new_node
            self.cnt+=1
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                        self.cnt+=1
                        return
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=new_node
                        self.cnt+=1
                        return
                    else:
                        temp=temp.right

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            return
        arr=[]
        count=0
        arr.append(rt)
        while count < len(arr):
            node_count = len(arr) - count
            print("\nLevel:",node_count, end=" ")
            for i in range(node_count):
                temp = arr[count]
                count += 1        #for counting the number of nodes in the array
                print(temp.data, end=" ")
                if temp.left is not None:
                    arr.append(temp.left)
                if temp.right is not None:
                    arr.append(temp.right)

b1=BST()
b1.insert(Node(100))
b1.insert(Node(20))
b1.insert(Node(450))
b1.insert(Node(10))
b1.insert(Node(40))
b1.insert(Node(70))
b1.insert(Node(90))
b1.insert(Node(65))
b1.insert(Node(300))
print("\n Inorder")
b1.inorder(b1.root)
print("\n Level Order Traversal:")
b1.level_order(b1.root)

