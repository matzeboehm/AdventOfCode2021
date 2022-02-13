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
        len_6 = []
        len_5 = []
        for i in clues:
            sorted_string = sorted(i)
            string = "".join(sorted_string)
            # unique lengths --> numbers 1, 4, 7, 8
            if len(i) in length_lookup.keys():                
                lookup[length_lookup[len(i)]] = string
            # All length 6 --> numbers 0, 6, 9
            elif len(i) == len(zero):
                if string not in len_6:
                    len_6.append(string)
            # Aöö length 5 --> numbers 2, 3, 5
            elif len(i) == len(two):
                if string not in len_5:
                    len_5.append(string)

        # aus 1 und 6 kann c bestimmt werden
        code_c = ""
        code_f = ""
        for i in len_6:
            one_v = set(lookup.get(1))
            temp = set(i)

            if len(one_v & temp) == 1:
                code_f = list(one_v & temp)[0]
                code_c = "".join(list(one_v)).replace(code_f, "")
                break

        for i in len_5:
            if code_c in i and code_f in i:
                lookup[3] = i
            elif code_c in i and code_f not in i:
                lookup[2] = i
            elif code_c not in i and code_f in i:
                lookup[5] = i

        code_e = ""
        one_v = set(lookup.get(1))
        four_v = set(lookup.get(4))
        seven_v = set(lookup.get(7))
        eight_v = set(lookup.get(8))
        compare = set.union(one_v, four_v, seven_v)
        for i in "".join(list(eight_v)):
            if i not in "".join(list(compare)):
                code_e = i
                break
        
        for i in len_6:
            if code_c not in i and code_f in i:
                lookup[6] = i
            elif code_c in i and code_e in i:
                lookup[0] = i
            elif code_c in i and code_e not in i:
                lookup[9] = i


        # in lookup steht welche Kombination (sortiert) gleich welcher Zahl entspricht
        lookup = {y:x for x,y in lookup.items()}

        # Aus Numbers muss jetzt noch umgewandelt werden 
        string_num = ""
        print(lookup)

        for i in numbers:
            sorted_string = sorted(i)
            string = "".join(sorted_string)

            string_num += str(lookup.get(string))

        int_num = int(string_num)
        print(int_num)
        sol += int_num
    print(sol)
    # not correct yet, not all values are correct in the lookup