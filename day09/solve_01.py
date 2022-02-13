import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [list(map(int, list(line.strip()))) for line in lines]
    
    input = np.array(lines)
    
    rows = len(input)
    columns = len(input[0])

    new_input = np.pad(input, 1, mode = "constant", constant_values = 10)

    low_points = []

    for i in range(1, rows +1 ):
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
    print("Risk Level: %i" %(risk_level))