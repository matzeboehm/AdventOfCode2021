from curses import flash
import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()

    rows = len(lines)
    cols = len(lines[0].strip())

    input = np.zeros((rows, cols), int)
    ones = np.ones((rows, cols), int)
    
    # Convert string to numpy array
    for i, line in enumerate(lines):
        for j, val in enumerate(line.strip()):
            input[i][j] = int(val)

    #steps = 100
    steps = 250
    flashCounter = 0
    brightestFlash = []

    neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    for step in range(steps):
        input += ones
        flashesThisStep = []

        # while max value in array greater than 10
        while np.amax(input) >= 10:
            paddedInput = np.pad(input, 1, mode="constant", constant_values=0)
            adder = np.zeros((rows+2, cols+2), int)

            for row in range(1, rows+1):
                for col in range(1, cols+1):
                    if paddedInput[row][col] >= 10 and ((row,col)) not in flashesThisStep:
                        flashesThisStep.append((row,col))
                        flashCounter += 1

                        for neighbor in neighbors:
                            deltaRow, deltaCol = neighbor
                            rowCheck = row + deltaRow
                            colCheck = col + deltaCol

                            adder[rowCheck][colCheck] += 1

            paddedInput += adder

            # set all flashed values to 0
            for pos in flashesThisStep:
                x,y = pos
                paddedInput[x][y] = 0

            input = paddedInput[1:-1, 1:-1]

        # all fishes bright up 
        if np.sum(input) == 0:
            brightestFlash.append(step + 1)

        print("After Step %i" %(step + 1))
        print(input)

    print("Flash Counter %i" %(flashCounter))
    if brightestFlash:
        print(brightestFlash[0])