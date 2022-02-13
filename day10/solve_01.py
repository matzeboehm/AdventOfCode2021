with open("input.txt","r") as file:
    lines = file.readlines()

    symbol_dict = {"]":"[", ")":"(", ">":"<", "}":"{"}
    symbol_values = {"]":57, ")":3, ">":25137, "}":1197}
    error_score = 0

    for line in lines:
        symbol_list = []
        for char in line:
            if char in symbol_dict.values():
                symbol_list.append(char)
            elif char in symbol_dict.keys():
                if symbol_list[-1] == symbol_dict.get(char):
                    symbol_list = symbol_list[:-1]
                else:
                    error_score += symbol_values.get(char)
                    break

print(error_score)