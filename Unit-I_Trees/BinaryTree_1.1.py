class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val, end = " ")
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.val, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val, end=" ")

root = Node(5)
root.left = Node(10)
root.right = Node(15)

root.inorder()
print()
root.preorder()
print()
root.postorder()