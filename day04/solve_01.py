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
            temp = np.where(temp == caller, 0, temp)
            
            if ((~temp.any(axis=0)).any() or (~temp.any(axis=1)).any()):
                shortestSolve.append(index)
                sol.append(np.sum(temp) * caller)
                break

            
    quickestIndex = min(shortestSolve)
    sol_index = shortestSolve.index(quickestIndex)
    print(sol[sol_index])