m,n = input().split()
m = int(m)
n = int(n)

s = m*n    #8
c = 0
for i in range(1,s):   #1,2,3
    if (i*2<=s):
        c = i       #2>8   4>8     6>8

    else:
        break      #1   2   3

print(c)