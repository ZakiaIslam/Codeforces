n = int(input())

count=0

for i in range(n):
    x,y,z = input().split()
    x = int(x)
    y =int(y)
    z = int(z)
    s = x+y+z
    if s>=2:
        count+=1

print(count)