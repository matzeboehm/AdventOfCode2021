with open("input.txt", "r") as file:
    lines = file.readlines()

    string = [str(i).strip() for i in lines]
    length = len(string[0])

    gamma = ""
    epsilon = ""

    for i in range(length):
        temp = ""
        for line in string:
            temp += line[i]
        
        zeros = temp.count("0")
        ones = len(temp) - zeros

        if zeros > ones:
            gamma += "0"
            epsilon += "1"
        elif ones > zeros:
            gamma += "1"
            epsilon += "0"

    print(int(gamma, 2) * int(epsilon, 2))
