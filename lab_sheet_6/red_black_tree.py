class TreeNode:
    # Color 1: red 0: black
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
        self.color = 1


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = TreeNode(key)
        temp = self.root
        # BST insertion
        if not temp:
            node.color = 0
            self.root = node
            return
        while temp:
            if node.key < temp.key:
                if not temp.left:
                    temp.left = node
                    temp.left.parent = temp
                    break
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = node
                    temp.right.parent = temp
                    break
                else:
                    temp = temp.right

        # If new node is a child of root, return
        if not node.parent.parent:
            return

        while node != self.root and node.color == 1 and node.parent.color == 1:
            gp = node.parent.parent
            p = node.parent
            if gp:
                if gp.left == p:
                    if (not gp.right) or gp.right.color == 0:
                        # If aunt is black
                        if node == node.parent.right:
                            self.leftRotate(node.parent)
                            node = node.left
                        self.rightRotate(gp)
                        node.parent.color = 0
                        node.parent.right.color = 1
                        node = node.parent
                    else:
                        # If aunt is red
                        gp.color = 1
                        p.color = 0
                        gp.right.color = 0
                        node = node.parent.parent
                else:
                    if (not gp.left) or gp.left.color == 0:
                        # If aunt is black
                        if node == node.parent.left:
                            self.rightRotate(node.parent)
                            node = node.right
                        self.leftRotate(gp)
                        node.parent.color = 0
                        node.parent.left.color = 1
                        node = node.parent
                    else:
                        # If aunt is black
                        gp.color = 1
                        p.color = 0
                        gp.left.color = 0
                        node = node.parent.parent
            else:
                node = node.parent
        self.root.color = 0

    def leftRotate(self, node):
        rightNode = node.right
        node.right = rightNode.left
        if node.right:
            node.right.parent = node
        if not node.parent:
            self.root = rightNode
        elif node == node.parent.left:
            node.parent.left = rightNode
        else:
            node.parent.right = rightNode
        rightNode.parent = node.parent
        rightNode.left = node
        node.parent = rightNode

    def rightRotate(self, node):
        leftNode = node.left
        node.left = leftNode.right
        if node.left:
            node.left.parent = node
        if not node.parent:
            self.root = leftNode
        elif node == node.parent.left:
            node.parent.left = leftNode
        else:
            node.parent.right = leftNode
        leftNode.parent = node.parent
        leftNode.right = node
        node.parent = leftNode

    def printTree(self):
        self.printTreeCore(self.root)
        print()

    def printTreeCore(self, root):
        if not root:
            return
        print("({} ({}), {})".format("Black" if root.color == 0 else "Red", root.key, "P: " + str(root.parent.key if root.parent else "None")), end=" ")
        self.printTreeCore(root.left)
        self.printTreeCore(root.right)


rbt = RedBlackTree()
rbt.insert(3)
rbt.insert(1)
rbt.insert(5)
rbt.insert(7)
rbt.insert(6)
rbt.insert(8)
rbt.printTree()
