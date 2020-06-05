n = int(input())
for i in range(n):
	x,y = map(int,input().split())

	if x<y:
		z = x
		z = 2*z
		if z>y:
			print(z**2)
		else:
			print(y**2)
	else:
		z = y
		z = 2*z
		if z>x:
			print(z**2)
		else:
			print(x**2)