with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day14/input.txt", "r") as file:
    lines = file.readlines()

    inputPolymer = lines[0].strip()
    lookupTable = {}

    steps = 10

    for line in lines:
        if "->" in line:
            lookup, value = line.split("->")
            lookupTable[lookup.strip()] = value.strip()

    savedInput = inputPolymer
    for i in range(steps):
        string = ""
        for i in range(len(savedInput) - 1):
            lookupValue = lookupTable.get(savedInput[i:i+2])
            string += savedInput[i] + lookupValue

        string += savedInput[-1]
        savedInput = string
    
    uniqueLetters = set(string)
    objectsCounted = {}
    for letter in uniqueLetters:
        objectsCounted[letter] = string.count(letter)
    
    maxKey = max(objectsCounted.values())
    minKey = min(objectsCounted.values())
    print("Solution Task 1: %i" %(maxKey - minKey))