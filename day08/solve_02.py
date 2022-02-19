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
    length_lookup = {len(one):1, len(four):4, len(seven):7, len(eight):8}

    sol = 0

    for line in lines:
        clues, numbers = line.split("|")
        clues = clues.split()
        numbers = numbers.split()

        # store with unique length
        lookup = {}
        len_6 = set()
        len_5 = set()
        for i in clues:
            # all strings are sorted alphabetically
            sorted_string = sorted(i)
            string = "".join(sorted_string)
            # unique lengths --> numbers 1, 4, 7, 8
            if len(i) in length_lookup.keys():                
                if not lookup.get(length_lookup[len(i)]):
                    lookup[length_lookup[len(i)]] = string
            # All length 6 --> numbers 0, 6, 9
            elif len(i) == len(zero):
                if string not in len_6:
                    len_6.add(string)
            # All length 5 --> numbers 2, 3, 5
            elif len(i) == len(two):
                if string not in len_5:
                    len_5.add(string)

        # 1 must contain c and f. c is in 4 out of all len5 and len6, f is in 5 out of all len5 and len6
        code_c = ""
        code_f = ""
        tempList = list(len_5.union(len_6))
        
        one_v = lookup.get(1)
        counter = 0
        for i in tempList:
            if one_v[0] in i:
                counter += 1
        if counter == 4:
            code_c = one_v[0]
            code_f = one_v[1]
        elif counter == 5:
            code_f = one_v[0]
            code_c = one_v[1]
        
        for i in len_5:
            if code_c in i and code_f not in i:
                lookup[2] = i
            elif code_c in i and code_f in i:
                lookup[3] = i
            elif code_c not in i and code_f in i:
                lookup[5] = i

        # in the unique lenghts, e and g only appears in 8. e and g appear together in 0
        unique_147 = {i for i in (lookup[1] + lookup[4] + lookup[7])}
        unique_8 = {i for i in lookup[8]}
        code_eg = list(unique_8.difference(unique_147))

        for i in len_6:
            if code_c not in i:
                lookup[6] = i
            elif all(j in i for j in code_eg):
                lookup[0] = i
            else:
                lookup[9] = i

        # invert lookup
        lookup = {y:x for x,y in lookup.items()}

        string = ""
        for number in numbers:
            sorted_number = "".join(sorted(number))
            string += str(lookup[sorted_number])
        
        sol += int(string)
    
    print("Sum of all numbers %i" %(sol))
