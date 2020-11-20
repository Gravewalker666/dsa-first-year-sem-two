# 19000073, Lab Sheet - Question 2
class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, v):
        self.vertices[v] = list()

    def addVertices(self, array):
        for v in array:
            self.addVertex(v)

    def addEdge(self, v1, v2):
        self.vertices[v1].append(v2)

    def removeVertex(self, v):
        self.vertices.pop(v)
        for u in self.vertices:
            self.vertices[u].remove(v)

    def printGraph(self):
        print("-------------------------------")
        for v in self.vertices:
            print("{} -> (".format(v), end=" ")
            for u in self.vertices[v]:
                print(u, end=" ")
            print(")")
        print("-------------------------------")


def heightBalancingTree(g, array):
    mid = int(len(array)/2)
    leftArray = array[0:mid]
    rightArray = array[mid+1:]
    # print(leftArray)
    # print(rightArray)
    if leftArray:
        g.vertices[array[mid]].append(leftArray[int(len(leftArray)/2)])
        heightBalancingTree(g, leftArray)
    if rightArray:
        g.vertices[array[mid]].append(rightArray[int(len(rightArray) / 2)])
        heightBalancingTree(g, rightArray)


array = [5, 10, 20, 8, 12, 21, 25]
array.sort()
print(array)
g = Graph()
g.addVertices(array)
heightBalancingTree(g, array)
g.printGraph()

array2 = [50, 17, 76, 9, 23, 54, 14, 19, 72, 12, 67]
array2.sort()
print(array)
g2 = Graph()
g2.addVertices(array2)
heightBalancingTree(g2, array2)
g2.printGraph()

array3 = [95, 72, 110, 43, 87, 102, 120, 2, 50, 85, 108, 47]
array3.sort()
print(array3)
g3 = Graph()
g3.addVertices(array3)
heightBalancingTree(g3, array3)
g3.printGraph()
