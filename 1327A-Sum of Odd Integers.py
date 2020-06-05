t = int(input())
c = 0
for i in range(t):
	a,b = input().split()
	a = int(a)
	b = int(b)
	#c = a+b
	if ((a%2)==(b%2))and(b**2<=a):
		print("YES")
	else:
		print("NO")
