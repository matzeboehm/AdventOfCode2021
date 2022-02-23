def insertInDict(mydict, mykey, myvalue):
    if mydict.get(mykey):
        mydict[mykey] += myvalue
    else:
        mydict[mykey] = myvalue

    return mydict

with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day14/input.txt", "r") as file:
    lines = file.readlines()

    inputPolymer = lines[0].strip()
    lookupTable = {}

    steps = 40

    # convert to lookup table
    for line in lines:
        if "->" in line:
            lookup, value = line.split("->")
            lookupTable[lookup.strip()] = value.strip()

    # make input into dict
    polymer = {}
    for i in range(len(inputPolymer) - 1):
        string = inputPolymer[i:i+2]
        polymer = insertInDict(polymer, string, 1)
    
    # iterate over polymer for n steps
    for i in range(steps):
        newPolymer = {}
        for key in polymer:
            letter = lookupTable.get(key)
            value = polymer.get(key)
            newKey1 = key[0] + letter
            newKey2 = letter + key[1]   

            newPolymer = insertInDict(newPolymer, newKey1, value)
            newPolymer = insertInDict(newPolymer, newKey2, value)

        polymer = newPolymer

    # find characters that appear most and least often
    # only look at second character of each key
    letters = {}
    for key in polymer:
        if letters.get(key[1]):
            letters[key[1]] += polymer.get(key)
        else:
            letters[key[1]] = polymer.get(key)
    
    maxLetter = max(letters.values())
    minLetter = min(letters.values())

    print(maxLetter - minLetter)