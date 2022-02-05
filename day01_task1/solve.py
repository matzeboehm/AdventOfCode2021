with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day01_task1/input.txt", "r") as file:
    lines = file.readlines()
    counter = 0
    
    for index,line in enumerate(lines):
        if index < len(lines) - 1:
            if lines[index + 1] > line:
                counter += 1
                print(line)
                print(lines[index +1])

    print(counter)