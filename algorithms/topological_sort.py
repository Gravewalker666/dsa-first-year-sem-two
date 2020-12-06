from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, v):
        self.vertices[v] = deque()

    def addEdge(self, u, v):
        self.vertices[u].append(v)

    def dfs(self, v, visited):
        for u in self.vertices[v]:
            if u not in visited:
                self.dfs(u, visited)
        visited.append(v)

    def topSort(self):
        visited = []
        for v in self.vertices:
            if v not in visited:
                self.dfs(v, visited)
        visited.reverse()
        print(visited)


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)

g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(5, 0)
g.addEdge(5, 2)

g.topSort()
