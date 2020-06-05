import math
m,n,a = input().split()
a = int(a)
r = math.ceil(int(m)/a)
c = math.ceil(int(n)/a)

s = r*c

print(s)

