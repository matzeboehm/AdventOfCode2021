def gausssum(number):
    return int((number*(number+1))/2)
    

with open("input.txt", "r") as file:
    input = file.readline().split(",")
    input = list(map(int, input))

    min_val = min(input)
    max_val = max(input)

    sol = {}

    for i in range(min_val, max_val + 1):
        temp = [gausssum(abs(value - i)) for value in input]
        sol[i] = sum(temp)

    min_fuel_key = min(sol, key=sol.get)
    min_fuel = sol[min_fuel_key]
    print("Minimum fuel needed: %i" %(min_fuel))
