from input import returnInput

input = returnInput()
days = 256

sol = {}
for i in input:
    if sol.get(i):
        sol[i] += 1
    else:
        sol[i] = 1

for i in range(days):
    temp = sol.get(0, 0)
    for i in range(8):
        sol[i] = sol.get(i+1, 0)
    sol[8] = temp
    sol[6] = sol.get(6, 0) + temp
    
print("Total amount of lanternfish: %i" %(sum(sol.values())))