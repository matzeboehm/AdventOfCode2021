with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [int(i) for i in lines]
    counter = 0
    
    for index in range(len(lines) - 3):
        A = lines[index] + lines[index + 1] + lines[index + 2]
        B = lines[index + 1] + lines[index + 2] + lines[index + 3]
        
        if B > A:
            counter += 1
        
    print(counter)
