from xxlimited import new


with open("/Users/matthiasboehm/Documents/AdventOfCode2021/day03/input.txt", "r") as file:
    lines = file.readlines()

    string = [str(i).strip() for i in lines]
    length = len(string[0])


    # oxygen
    new_string = string[:]
    for i in range(length):
        if len(new_string) == 1:
            break

        temp = ""
        for line in new_string:
            temp += line[i]
        
        zeros = temp.count("0")
        ones = len(temp) - zeros

        if zeros > ones:
            new_string = [binary for binary in new_string if binary[i] == "0"]
        else:
            new_string = [binary for binary in new_string if binary[i] == "1"]
           
    oxygen = new_string[0]    

    # CO2
    new_string = string[:]
    print(new_string)
    for i in range(length):
        if len(new_string) == 1:
            break
        
        temp = ""
        for line in new_string:
            temp += line[i]

        zeros = temp.count("0")
        ones = len(temp) - zeros

        if zeros > ones:
            new_string = [binary for binary in new_string if binary[i] == "1"]
        else:
            new_string = [binary for binary in new_string if binary[i] == "0"]
        
    co2 = new_string[0]

    print(int(oxygen, 2) * int(co2, 2))