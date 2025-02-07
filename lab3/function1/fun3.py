def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    return int(chickens), int(rabbits)

numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"Количество кур: {result[0]}, Количество кроликов: {result[1]}")