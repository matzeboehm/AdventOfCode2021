import numpy as np

with open("input.txt", "r") as file:
    lines = file.readlines()

    dataPoints = []
    foldInstructions = []
    maxRow = 0
    maxCol = 0

    for line in lines:
        if "fold along" in line:
            temp = line.replace("fold along ", "").strip()
            axis, position = temp.split("=")
            foldInstructions.append((axis, int(position)))
        elif "," in line:
            temp = line.strip()
            x, y = temp.split(",")
            x = int(x)
            y = int(y)

            if x > maxCol:
                maxCol = x
            if y > maxRow:
                maxRow = y

            dataPoints.append((x, y))

    dataArray = np.zeros((maxRow + 1, maxCol + 1), int)

    for col, row in dataPoints:
        dataArray[row][col] = 1

    visible = []

    for axis, position in foldInstructions:
        #newArray = 0
        #foldArray = 0
        if axis == "x":
            newArray = dataArray[0:, 0:position]
            foldArray = dataArray[0:, position+1:]
            foldArray = np.fliplr(foldArray)
        elif axis == "y":
            newArray = dataArray[0:position]
            foldArray = dataArray[position+1:]
            foldArray = np.flipud(foldArray)
        
        # check if newArray and foldArray have the same dimension, otherwise add zero columns or rows so you can add them
        if len(newArray) != len(foldArray): # add padding to the top of foldArray
            adder = np.zeros((len(newArray) - len(foldArray), len(newArray[0])), int)
            foldArray = np.r_[adder, foldArray]
        if len(newArray[0]) != len(foldArray[0]): # add padding to left side of foldArray
            adder = np.zeros((len(newArray), len(newArray[0]) - len(foldArray[0])), int)
            foldArray = np.c_[adder, foldArray]
        dataArray = newArray + foldArray
        
        counter = 0
        for i, row in enumerate(dataArray):
            for j, val in enumerate(row):
                if val != 0:
                    counter += 1
                    if val != 1:
                        dataArray[i][j] = 1
        visible.append(counter)

    print(visible)  # part 1

    # part 2
    for line in dataArray:
        string = ""
        for char in line:
            if char == 0:
                string = string + " "
            else:
                string = string + "▓"
        print(string)
