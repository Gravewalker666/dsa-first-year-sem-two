from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}
        self.time = 0

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

    def dfsTraversal(self, u, low, disc, stackMember, st):
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        stackMember[u] = True
        st.append(u)

        for v in self.vertices[u]:
            if disc[v] == -1:
                self.dfsTraversal(v, low, disc, stackMember, st)
                low[u] = min(low[u], low[v])
            elif stackMember[v]:
                low[u] = min(low[u], low[v])

        w = -1
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                stackMember[w] = False
            print()

    def findSCC(self):
        noOVertices = len(self.vertices)
        disc = [-1] * noOVertices
        low = [-1] * noOVertices
        stackMember = [False] * noOVertices
        st = []

        for i in self.vertices:
            if disc[i] == -1:
                self.dfsTraversal(i, low, disc, stackMember, st)


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)

g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(1, 3)

g.printGraph()
print("Strongly connected components :")
g.findSCC()
