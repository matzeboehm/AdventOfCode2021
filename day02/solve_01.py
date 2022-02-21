with open("input.txt", "r") as file:
    lines = file.readlines()

    horizontal = 0
    vertical = 0

    for i in lines:
        a = i.split()

        if a[0] == "forward":
            horizontal += int(a[1])
        elif a[0] == "up":
            vertical -= int(a[1])
        elif a[0] == "down":
            vertical += int(a[1])

    print(horizontal*vertical)
