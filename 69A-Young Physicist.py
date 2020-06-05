n = int(input())
l = []
a= 0
b = 0
c = 0
for y in range(n):
	i ,j,k = map(int, input().split())
	a += i
	b += j
	c += k

if (a == 0 and b == 0 and c == 0) :
	print("YES")
else:
	print("NO")