class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inOrderTraversal(root):
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.data, end = " ")
    inOrderTraversal(root.right)
def preOrderTraversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.data, end=" ")

root = BinaryTree('R')
nodeA = BinaryTree('A')
nodeB = BinaryTree('B')
nodeC = BinaryTree('C')
nodeD = BinaryTree('D')
nodeE = BinaryTree('E')
nodeF = BinaryTree('F')
nodeG = BinaryTree('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print('Root of the Tree is:', root.data)
print("InOrder Traversal is: ", end = " ")
inOrderTraversal(root)
print()
print("PreOrder Traversal is: ", end = " ")
preOrderTraversal(root)
print()
print("PostOrder Traversal is: ", end = " ")
postOrderTraversal(root)
#print("root.right.left.data:", root.right.left.data)