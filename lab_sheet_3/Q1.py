# 19000073, Lab Sheet 3 - Question 1
from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    # Add vertex Question 1 part 1
    def addVertex(self, v):
        self.vertices[v] = list()

    # Add edge Question 1 part 1
    def addEdge(self, v1, v2):
        self.vertices[v1].append(v2)

    # Remove vertex Question 1 part 2
    def removeVertex(self, v):
        self.vertices.pop(v)
        for u in self.vertices:
            self.vertices[u].remove(v)

    # Find path and length of the path between two vertices
    # Question 1 part 3, 4
    def findPath(self, s, d):
        q = deque()
        q.append(s)
        visited = [s]
        prev = [None] * len(self.vertices)
        while q:
            current = q.popleft()
            for n in self.vertices[current]:
                if n not in visited:
                    q.append(n)
                    visited.append(n)
                    prev[n] = current
        current = d
        path = [current]
        while current:
            current = prev[current]
            path.append(current)
        path.reverse()
        if path[0] == s:
            print("Path found: {} to {}".format(s, d))
            print("- Path: ", end=" ")
            for v in path:
                print(v, end=" ")
            print("")
            print("- Length: {}".format(len(path) - 1))
            return
        print("Path not found: {} to {}".format(s, d))

    def printGraph(self):
        print("-------------------------------")
        for v in self.vertices:
            print("{} -> (".format(v), end=" ")
            for u in self.vertices[v]:
                print(u, end=" ")
            print(")")
        print("-------------------------------")


g = Graph()

# Add vertices
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.addVertex(7)
g.addVertex(8)
g.addVertex(9)
g.addVertex(10)
g.addVertex(11)
g.addVertex(12)

# Add edges
g.addEdge(0, 7)
g.addEdge(0, 9)
g.addEdge(0, 11)
g.addEdge(9, 8)
g.addEdge(9, 10)
g.addEdge(7, 11)
g.addEdge(7, 6)
g.addEdge(7, 3)
g.addEdge(8, 1)
g.addEdge(8, 12)
g.addEdge(10, 1)
g.addEdge(6, 5)
g.addEdge(3, 4)
g.addEdge(3, 2)
g.addEdge(12, 2)

g.printGraph()
g.findPath(0, 2)
g.findPath(9, 5)
g.findPath(0, 11)
g.findPath(0, 12)
