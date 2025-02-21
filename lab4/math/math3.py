import math
n=int(input("n: "))
l=int(input("l: "))
s=(n*l**2) / (4 * math.tan(math.pi / n))
print(round(s,1))