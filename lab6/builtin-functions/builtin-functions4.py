import math 
import time

def zxc(n,d):
    time.sleep(d/1000)
    s=math.sqrt(n)
    return s
n=int(input())
d=int(input())
print(f"Square root of {n} after {d} miliseconds is {zxc(n,d)} ")