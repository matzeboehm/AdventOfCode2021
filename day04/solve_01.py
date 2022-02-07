import numpy as np

with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day04/input.txt", "r") as file:
    lines = file.readlines()

    callout = lines[0].replace("\n", "").split(",")
    callout = [int(i) for i in callout]
    
    numbers = lines[2:]
    numbers = [i.replace("\n", "") for i in numbers]
    
    sol = []
    shortestSolve = []

    for i in range(int((len(numbers) + 1) /6)):
        temp = np.array([
                    numbers[i*6].split(), 
                    numbers[i*6+1].split(),
                    numbers[i*6+2].split(),
                    numbers[i*6+3].split(),
                    numbers[i*6+4].split()])
        temp = temp.astype(int)

        for index, caller in enumerate(callout):
            # replace number called with -1
            temp = np.where(temp == caller, -1, temp)

            # check if the one row or one column has only -5, if so BINGO
            # for sum, those values must be counted as 0
            if -5 in temp.sum(axis=0) or -5 in temp.sum(axis=1):
                shortestSolve.append(index)
                temp = np.where(temp == -1, 0, temp)
                sol.append(np.sum(temp) * caller)
                break
            
    quickestIndex = min(shortestSolve)
    sol_index = shortestSolve.index(quickestIndex)
    print(sol[sol_index])
    print(len(sol))