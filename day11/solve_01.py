import numpy as np
with open("input.txt", "r") as file:
    lines = file.readlines()

    rows = len(lines)
    cols = len(lines[0].strip())

    input = np.zeros((rows, cols), int)
    ones = np.ones((rows, cols), int)

    steps = 100

    totalFlashes = 0

    for i, row in enumerate(lines):
        for j, val in enumerate(row.strip()):
            input[i][j] = int(val)
    
    whereToAdd = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for step in range(steps):
        input += ones
        flashed = []

        while np.amax(input) >= 10:    
            adder = np.zeros((rows+2, cols+2), int)
            paddedInput = np.pad(input, 1, mode = "constant", constant_values=0)

            for i in range(1, rows + 2):
                for j in range(1, cols + 2):
                    if ((i,j)) not in flashed and paddedInput[i][j] >= 10:
                        flashed.append((i,j))
                        totalFlashes += 1

                        for k in whereToAdd:
                            x,y = k
                            row_adder = i + x
                            col_adder = j + y

                            if (0 < row_adder < (rows + 2)) and (0 < col_adder < (cols + 2)) and ((row_adder, col_adder)) not in flashed:
                                adder[row_adder][col_adder] += 1

            for flash in flashed:
                x,y = flash
                paddedInput[x][y] = 0
            
            input = paddedInput[1:-1, 1:-1]

            adder = adder[1:-1, 1:-1]
            input += adder
            
        print("Step %i" %(step + 1))   
        print(input)
    print("Total flashes %i" %(totalFlashes))
    # 1755
            