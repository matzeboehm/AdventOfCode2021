with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day02/input.txt", "r") as file:
    lines = file.readlines()

    horizontal = 0
    vertical = 0
    aim = 0

    for i in lines:
        a = i.split()

        if a[0] == "forward":
            horizontal += int(a[1])
            vertical += aim * int(a[1])
        elif a[0] == "up":
            aim -= int(a[1])
        elif a[0] == "down":
            aim += int(a[1])

    print(horizontal*vertical)