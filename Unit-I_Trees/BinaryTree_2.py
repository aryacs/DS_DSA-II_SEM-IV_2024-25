class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left is None:
                curr_node.left = node
                break
            else:
                queue.append(curr_node.left)
            if curr_node.right is None:
                curr_node.right = node
                break
            else:
                queue.append(curr_node.right)
def inOrderT(root):
    if root is None:
        return
    inOrderT(root.left)
    print(root.data, end = " ")
    inOrderT(root.right)
def preOrderT(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrderT(root.left)
    preOrderT(root.right)
def postOrderT(root):
    if root is None:
        return
    postOrderT(root.left)
    postOrderT(root.right)
    print(root.data, end=" ")

tree = BinaryTree(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)

#print('Root of the Tree is:', tree.data)
print("InOrder Traversal is: ", end = " ")
inOrderT(tree.node)
print()
print("PreOrder Traversal is: ", end = " ")
preOrderT(tree.node)
print()
print("PostOrder Traversal is: ", end = " ")
postOrderT(tree.node)