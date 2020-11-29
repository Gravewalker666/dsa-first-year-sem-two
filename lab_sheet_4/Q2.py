from collections import deque

current_year = 2018


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, v):
        self.vertices[v] = deque()

    def addEdge(self, u, v):
        self.vertices[u].append(v)

    def printGraph(self):
        print("-------------------------------")
        for v in self.vertices:
            print("{} -> (".format(v), end=" ")
            for u in self.vertices[v]:
                print(u, end=" ")
            print(")")
        print("-------------------------------")


def timeMachineCount(Q, malDict, malDictB):
    g = Graph()
    for i in range(current_year, Q - 1, -1):
        g.addVertex(i)
        for j in range(i - 1, i - 7, -1):
            g.addEdge(i, j)
    count = 0
    years = []
    current = current_year
    while current:
        if current == Q:
            years.append(Q)
            print(years)
            return count
        count += 1
        next_year = min(g.vertices[current])
        while next_year in malDict:
            next_year += 1
        years.append(current)
        for u in g.vertices[current]:
            if u in malDictB and next_year > malDictB[u] >= Q:
                next_year = malDictB[u]
            if u == Q:
                years.append(Q)
                print(years)
                return count
        current = next_year
    return -1


T = int(input())
for i in range(T):
    Q = int(input())
    K = int(input())
    malDict = {}
    for j in range(K):
        m = input().split(" ")
        malDict[int(m[0])] = int(m[1])
    L = int(input())
    malDictB = {}
    for j in range(L):
        mb = input().split(" ")
        malDictB[int(mb[0])] = int(mb[1])
    print(timeMachineCount(Q, malDict, malDictB))
