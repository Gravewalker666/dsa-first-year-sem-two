class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinNode(self, root):
        if root.left:
            return self.getMinNode(root.left)
        return root

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        x.height = 1 + max(self.getHeight(x.right), self.getHeight(x.left))
        y.height = 1 + max(self.getHeight(y.right), self.getHeight(y.left))
        return y

    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        y.height = 1 + max(self.getHeight(y.right), self.getHeight(y.left))
        x.height = 1 + max(self.getHeight(x.right), self.getHeight(x.left))
        return x

    def printTree(self):
        self.printTreeCore(self.root)
        print()

    def printTreeCore(self, root):
        if not root:
            return
        print(root.key, end=" ")
        self.printTreeCore(root.left)
        self.printTreeCore(root.right)

    def insertNode(self, key):
        self.root = self.insertNodeCore(self.root, key)

    def insertNodeCore(self, root, key):
        if not root:
            return TreeNode(key)
        if key < root.key:
            root.left = self.insertNodeCore(root.left, key)
        else:
            root.right = self.insertNodeCore(root.right, key)
        root.height = 1 + max(self.getHeight(root.right), self.getHeight(root.left))
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def searchNode(self, key):
        return self.searchNodeCore(self.root, key)

    def searchNodeCore(self, root, key):
        if not root:
            return False
        if root.key > key:
            return self.searchNodeCore(root.left, key)
        elif root.key < key:
            return self.searchNodeCore(root.right, key)
        else:
            return True

    def deleteNode(self, key):
        self.root = self.deleteNodeCore(self.root, key)

    def deleteNodeCore(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.deleteNodeCore(root.left, key)
        elif key > root.key:
            root.right = self.deleteNodeCore(root.right, key)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.getMinNode(root.right)
            root.key = temp.key
            root.right = self.deleteNodeCore(root.right, temp.key)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root


avl = AVLTree()
avl.insertNode(33)
avl.insertNode(13)
avl.insertNode(52)
avl.insertNode(9)
avl.insertNode(21)
avl.insertNode(61)
avl.insertNode(8)
avl.insertNode(11)
avl.printTree()

print(avl.searchNode(19))
print(avl.searchNode(61))

avl.deleteNode(13)
avl.printTree()
