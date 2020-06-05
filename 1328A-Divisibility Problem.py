def inc(a,b):
    i =0
    if a>b:
        if((a%b) != 0):
            r = (a//b)+1
            i = (b*r)-a
            return i
        else:
            return i 
    else:
        i = b-a
        return i 

n = int(input())
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print(inc(a,b))