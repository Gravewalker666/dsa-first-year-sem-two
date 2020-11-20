from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, v):
        self.vertices[v] = list()

    def addEdge(self, v, u):
        self.vertices[v].append(u)

    def printGraph(self):
        print("-------------------------------")
        for v in self.vertices:
            print("{} -> (".format(v), end=" ")
            for u in self.vertices[v]:
                print(u, end=" ")
            print(")")
        print("-------------------------------")

    def DFSTraversal(self):
        visited = []
        for a in self.vertices:
            if a not in visited:
                stack = deque([a])
                while stack:
                    current = stack.popleft()
                    if current not in visited:
                        visited.append(current)
                        for u in self.vertices[current]:
                            stack.appendleft(u)
        return visited

    def getTranspose(self):
        transpose = Graph()
        for v in self.vertices:
            transpose.addVertex(v)
        for v in self.vertices:
            for u in self.vertices[v]:
                transpose.addEdge(u, v)
        return transpose

    def getSCC(self):
        orderStack = deque(self.DFSTraversal())
        gt = self.getTranspose()
        visited = []
        sccList = []
        for a in orderStack:
            if a not in visited:
                stack = deque([a])
                currentScc = []
                while stack:
                    current = stack.popleft()
                    if current not in visited:
                        visited.append(current)
                        currentScc.append(current)
                        for u in gt.vertices[current]:
                            stack.appendleft(u)
                sccList.append(currentScc)
        return sccList


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)

g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)

g.printGraph()
print("Strongly connected components :", end=" ")
print(g.getSCC())
