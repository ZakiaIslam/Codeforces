n,k = input().split()
n = int(n)
k = int(k)

li = [int(x) for x in input().split()]

c = li[k-1]
count = 0

if c>0:
    for i in range(0,n):
        if (c <= li[i]):
            count+=1

else:
    for i in range(n):
        if c < li[i]:
            count+=1


print(count)



