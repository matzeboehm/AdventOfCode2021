from collections import defaultdict

class Graph:
    def __init__(self):
        self.vertices = 0
        self.uniqueValues = {}
        self.graph = {}
        self.pathsThroughCave = []

    def addEdge(self, startNode, endNode):
        if startNode in self.graph:
            self.graph[startNode].append(endNode)
        else:
            self.graph[startNode] = [endNode]

        if startNode not in self.uniqueValues:
            self.vertices += 1
            self.uniqueValues[startNode] = False
        if endNode not in self.uniqueValues:
            self.vertices += 1
            self.uniqueValues[endNode] = False

    def printAllPaths(self, start, end, visited, path):
        if start.islower(): # visit only once
            visited[start] = True
        else:   # visit multiple times
            visited[start] = False
        path.append(start)

        if start == end:
            print(path)
            self.pathsThroughCave.append(path[:]) # attach copy of list otherwise the reference is empty
        else:
            for i in self.graph.get(start):
                if visited[i] == False:
                    self.printAllPaths(i, end, visited, path)
            
        path.pop()
        visited[start] = False

    def traverse(self, start, end):
        visited = self.uniqueValues.copy()
        path = []
        self.printAllPaths(start, end, visited, path)

    def printGraph(self):
        print(self.graph)

    def printPathsThroughCave(self):
        print(self.pathsThroughCave)
        print("Amount of paths %i" %(len(self.pathsThroughCave)))


with open("input.txt", "r") as file:
    lines = file.readlines()
    
    graph = Graph()

    for line in lines:
        start, end = line.strip().split("-")
        graph.addEdge(start, end)
        graph.addEdge(end, start)

    graph.printGraph()
    graph.traverse("start", "end")
    graph.printPathsThroughCave()