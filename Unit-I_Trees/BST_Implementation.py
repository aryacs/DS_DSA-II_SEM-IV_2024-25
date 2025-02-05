class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node

#Driver code
tree = Tree()
root = tree.createNode(5)
tree.createNode(2)
tree.createNode(4)
tree.createNode(8)
tree.createNode(6)
tree.createNode(10)
print("Root of Tree is:", root.data)


