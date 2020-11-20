# 19000073, Lab Sheet 3 - Question 3
from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}
        self.noOfEdges = 0

    def addVertex(self, v):
        self.vertices[v] = list()

    def addEdge(self, v1, v2):
        self.noOfEdges += 1
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)

    def printGraph(self):
        print("-------------------------------")
        for v in self.vertices:
            print("{} -> (".format(v), end=" ")
            for u in self.vertices[v]:
                print(u, end=" ")
            print(")")
        print("-------------------------------")

    def isBipartite(self):
        part1 = {0}
        part2 = set()
        for a in self.vertices:
            if not self.vertices[a]:
                part1.add(a)
        part1Prev = set()
        part2Prev = set()
        while not len(part1.union(part2)) == len(self.vertices):
            part1Prev = part1
            part2Prev = part2
            for i in part1:
                part2 = part2.union(set(self.vertices[i]))
            for i in part2:
                part1 = part1.union(set(self.vertices[i]))
            if part1 == part1Prev and part2 == part2Prev:
                tempSet = set(self.vertices) - part1.union(part2)
                part1.add(tempSet.pop())
            print(part1)
            print(part2)
        if part1.intersection(part2):
            print("Not bipartite")
            return False
        print("Bipartite")
        return True

    def isBipartiteBFS(self):
        q = deque()
        q.append(list(self.vertices.keys())[0])
        visited = []
        part1 = {list(self.vertices.keys())[0]}
        part2 = set()
        while q:
            current = q.popleft()
            visited.append(current)
            if current in part1:
                part2 = part2.union(self.vertices[current])
            elif current in part2:
                part1 = part1.union(self.vertices[current])
            else:
                part1.add(current)
                part2 = part2.union(self.vertices[current])
            for v in self.vertices[current]:
                if v not in visited:
                    q.append(v)
            if not q and len(set(visited)) != len(self.vertices):
                q.append(list(set(self.vertices) - set(visited))[0])
        print(part1)
        print(part2)
        if part1.intersection(part2):
            print("Not bipartite")
            return False
        print("Bipartite")
        return True


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)

g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(6, 2)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(2, 5)
g.addEdge(4, 1)
g.addEdge(4, 3)
g.addEdge(4, 5)
# g.addEdge(4, 2)

g.printGraph()
g.isBipartiteBFS()

g1 = Graph()
g1.addVertex(0)
g1.addVertex(1)
g1.addVertex(2)

g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(0, 1)

g1.printGraph()
g1.isBipartiteBFS()

g2 = Graph()
g2.addVertex(0)
g2.addVertex(1)
g2.addVertex(2)
g2.addVertex(3)

g2.printGraph()
g2.addEdge(0, 1)
g2.addEdge(2, 3)
g2.isBipartiteBFS()
