from collections import deque


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, node):
        self.root = node

    def __repr__(self):
        reprStr = ''
        q = deque([self.root])
        while q:
            current = q.popleft()
            if not current:
                continue
            reprStr += '({}) '.format(current.key)
            q.append(current.left)
            q.append(current.right)
        return reprStr

    def addNode(self, newNode, parentKey, isLeft):
        q = deque([self.root])
        while q:
            current = q.popleft()
            if current.key == parentKey:
                if isLeft:
                    if not current.left:
                        current.left = newNode
                        return
                    else:
                        print("{}'s left is already occupied".format(parentKey))
                        return
                else:
                    if not current.right:
                        current.right = newNode
                        return
                    else:
                        print("{}'s right is already occupied".format(parentKey))
                        return
            q.append(current.left)
            q.append(current.right)

    def deleteNode(self, key):
        pass


root = Node(10)
b = BinaryTree(root)
b.addNode(Node(11), 10, True)
b.addNode(Node(9), 10, False)
b.addNode(Node(7), 11, True)
b.addNode(Node(15), 9, True)
b.addNode(Node(8), 9, False)
print(b)
# Question 1: Insert Value 12
b.addNode(Node(12), 11, False)
print(b)
