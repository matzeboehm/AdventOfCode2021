import numpy as np

def getRiskLevel(new_input, rows, columns) -> int:
    low_points = []

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            comp = [
                new_input[i-1][j],
                new_input[i][j-1],
                new_input[i][j+1],
                new_input[i+1][j]
            ]
            if all(k > new_input[i][j] for k in comp):
                low_points.append(new_input[i][j])
    
    risk_level = sum(low_points) + len(low_points)
    return risk_level

def checkNeighbors(new_input, i,j, locationsChecked):
    currentValue = new_input[i][j]
    neighbors = [
        new_input[i][j+1],  # Right
        new_input[i][j-1],  # Left
        new_input[i+1][j],  # Below
        new_input[i-1][j]   # Above
    ]
    index_neighbors = [(0,1), (0,-1), (1,0), (-1,0)]

    for index, neighbor in enumerate(neighbors):
        if neighbor >= 9:
            pass
        elif currentValue < neighbor:
            x,y = index_neighbors[index]
            locationsChecked.add((i+x, j+y))
            checkNeighbors(new_input, i+x , j+y, locationsChecked)
        
    return locationsChecked


with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [list(map(int, list(line.strip()))) for line in lines]
    
    input = np.array(lines)
    
    rows = len(input)
    columns = len(input[0])

    new_input = np.pad(input, 1, mode = "constant", constant_values = 10)

    risk_level = getRiskLevel(new_input, rows, columns)
    print("Risk Level: %i" %(risk_level))

    basin_lenghts = []

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            currentValue = new_input[i][j]
            neighbors = [
                new_input[i][j+1],  # Right
                new_input[i][j-1],  # Left
                new_input[i+1][j],  # Below
                new_input[i-1][j]   # Above
            ]
            
            # all neighbors are higher --> basin
            if all(currentValue < i for i in neighbors):
                #print("Basin found at %i:%i" %(i,j))
                locationsChecked = set()
                locationsChecked.add((i,j))
                # recursivly check all neighbors
                locationsChecked = checkNeighbors(new_input, i, j, locationsChecked)

                basin_lenghts.append(len(locationsChecked))
                
    intersting_lengths = basin_lenghts[:]
    intersting_lengths.sort()
    intersting_lengths = intersting_lengths[-3:]

    solution = 1
    for i in intersting_lengths:
        solution *= i
    print("Three biggest basins : %i" %(solution))