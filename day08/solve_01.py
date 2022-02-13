with open("input.txt", "r") as file:
    lines = file.readlines()
    
    zero = "abcefg"   # len 6
    one = "cf"        # len 2
    two = "acdeg"     # len 5
    three = "acdfg"   # len 5
    four = "bcdf"     # len 4
    five = "abdfg"    # len 5
    six = "abdefg"    # len 6
    seven = "acf"     # len 3
    eight = "abcdefg" # len 7
    nine = "abcdfg"   # len 6
    # --> unique: one, four, seven, eight

    sum_unique = 0

    for line in lines:
        clues, numbers = line.split("|")
        clues = clues.split()
        numbers = numbers.split()

        for i in numbers:
            if len(i) == len(one) or len(i) == len(four) or len(i) == len(seven) or len(i) == len(eight):
                sum_unique += 1

    print(sum_unique)