from numpy import median
with open("input.txt","r") as file:
    lines = file.readlines()

    symbol_dict = {"]":"[", ")":"(", ">":"<", "}":"{"}
    symbol_values = {"]":57, ")":3, ">":25137, "}":1197}
    score_values = {"[":2, "(":1, "<":4, "{":3}
    error_score = 0
    total_score = []

    for line in lines:
        symbol_list = []
        corrupted = False
        for char in line:
            if char in symbol_dict.values():
                symbol_list.append(char)
            elif char in symbol_dict.keys():
                if symbol_list[-1] == symbol_dict.get(char):
                    symbol_list = symbol_list[:-1]
                else:
                    error_score += symbol_values.get(char)
                    corrupted = True
                    break
        
        if corrupted == False:
            score = 0
            for i in symbol_list[::-1]:
                score = score * 5 + score_values[i]
            total_score.append(score)

print("Error score: %i" %(error_score))
print("Median: %i" %(median(total_score)))