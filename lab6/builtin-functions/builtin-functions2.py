def txt(n):
    upper = 0
    lower = 0
    for i in n:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper,lower

n = input()
upp,low = txt(n)
print("Upper:",upp,"Lower:",low)