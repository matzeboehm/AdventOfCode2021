import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()
    maximumSize = 0

    for line in lines: 
        numbers = ",".join(line.strip().split(" -> "))
        numbers = list(map(int, numbers.split(",")))
        
        if max(numbers) > maximumSize:
            maximumSize = max(numbers)

    array = np.zeros((maximumSize + 1,maximumSize + 1), dtype = int)

    for line in lines:
        start, end = line.strip().split(" -> ")
        start = tuple(map(int, start.split(",")))
        end = tuple(map(int, end.split(",")))

        dx = abs(end[0] - start[0])
        dy = abs(end[1] - start[1])

        if dx == 0:
            min_r = min(start[1], end[1])
            max_r = max(start[1], end[1])
            for i in range(min_r, max_r + 1):
                array[start[0]][i] += 1
        elif dy == 0:
            min_r = min(start[0], end[0])
            max_r = max(start[0], end[0])
            for i in range(min_r, max_r + 1):
                array[i][start[1]] += 1
        elif dx == dy != 0:
            min_x = min(start[0], end[0])
            max_x = max(start[0], end[0])
            min_y = min(start[1], end[1])
            max_y = max(start[1], end[1])
            slope = (start[1] - end[1])/(start[0] - end[0])

            for i in range(min_x, max_x + 1):
                if slope > 0:
                    array[i][min_y + (i - min_x)] += 1
                elif slope < 0:
                    array[i][max_y - (i - min_x)] += 1

    count = 0
    for row in array:
        for element in row:
            if element >= 2:
                count += 1
    print(count)
