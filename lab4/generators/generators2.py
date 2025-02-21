def zxc(n):
    x=0
    for i in range(1,n+1):
        if i%2==0:
            x=i
            yield x            
        
n=int(input())

even=zxc(n)
for i in range(n//2):
    print(even.__next__())