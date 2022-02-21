class Node:
    def __init__(self, name):
        self.name = name
        self.childNode = []

    def setChildNode(self, childNode):
        self.childNode.append(childNode)
    
    def getChildNode(self):
        return self.childNode

with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day12/test.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    uniquePoints = {}

    for line in lines:
        startPoint, endPoint = line.split("-")

        if startPoint not in uniquePoints.keys():
            uniquePoints[startPoint] = Node(startPoint)
        if endPoint not in uniquePoints.keys():
            uniquePoints[endPoint] = Node(endPoint)

        if uniquePoints.get(endPoint) not in uniquePoints.get(startPoint).getChildNode():
            uniquePoints[startPoint].setChildNode(uniquePoints[endPoint])
    

    print(uniquePoints)
    print(lines)
