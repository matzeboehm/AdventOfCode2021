from input import returnInput

input = returnInput()

days = 80

for i in range(days):
    add = 0
    for index, value in enumerate(input):
        if value == 0:
            input[index] = 6 
            add += 1
        else:
            input[index] = input[index] - 1
        
    input.extend([8] * add)
    
print("Total amount of lanternfish: %i" %(len(input)))