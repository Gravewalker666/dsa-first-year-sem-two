import math

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val


class BST:
    def __init__(self, root):
        self.n = 1
        self.root = root

    def printBST(self):
        self.inOrder(self.root)
        print()

    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.left)
        print(node.data, end=" ")
        self.inOrder(node.right)

    def addNode(self, newNode):
        temp = self.root
        parent = None
        leftFlag = False
        while temp:
            if temp.data > newNode.data:
                leftFlag = True
                parent = temp
                temp = temp.left
            elif temp.data < newNode.data:
                leftFlag = False
                parent = temp
                temp = temp.right
            if not temp:
                self.n += 1
                if leftFlag:
                    parent.left = newNode
                else:
                    parent.right = newNode

    def createVine(self):
        temp = self.root
        parent = None
        while temp:
            if temp.left:
                leftNode = temp.left
                temp.left = leftNode.right
                leftNode.right = temp
                if parent:
                    parent.right = leftNode
                else:
                    self.root = leftNode
                parent = leftNode
                temp = leftNode
            else:
                parent = temp
                temp = temp.right

    def createBalancedTree(self):
        m = int(math.pow(2, math.floor(math.log(self.n + 1, 2))) - 1)
        for i in range(self.n - m):
            pass


rootNode = Node(20)
bst = BST(rootNode)
bst.addNode(Node(15))
bst.addNode(Node(30))
bst.addNode(Node(17))
bst.addNode(Node(19))
bst.addNode(Node(25))
bst.addNode(Node(40))
bst.addNode(Node(32))
bst.addNode(Node(50))
bst.printBST()
bst.createVine()

bst.createBalancedTree()
