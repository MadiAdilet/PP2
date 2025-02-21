n = int(input())

def zxc(n):
    for i in range(n, 0, -1):
        yield i

print(*zxc(n))