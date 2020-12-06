from collections import deque


class Graph:
    def __init__(self):
        self.vertices = {}

	def __repr__(self):
		return self.vertices
	
	def addVertex(self, v):
		self.vertices[v] = deque()
	
    def addEdge(self, v, u):
		self.vertices[v].append(u)
	
    def getInDegree(self, v):
        inDegree = 0
        for u in self.vertices:
            for a in self.vertices[u]:
                if a == v:
                    inDegree += 1
        return inDegree
	
    def findUniversalSink(self):
        for u in self.vertices:
            if not self.vertices[u]:
                if self.getInDegree(u) == (len(self.vertices) - 1):
                    print("Universal sink found: {}".format(u))
                    return True
        return False


g = Graph()
g.addVertex(0)
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)

g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(3, 2)
g.addEdge(4, 2)

print (g)
g.findUniversalSink()
