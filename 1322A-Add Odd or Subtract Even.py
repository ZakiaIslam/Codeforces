def st(a,b):
	m = abs(a-b)
	if a>b:
		if(m%2==0):
			return 1
		else:
			return 2
	elif b>a:
		if (m%2==0):
			return 2
		else:
			return 1
	else:
		return 0
		


n = int(input())
for x in range(n):
	a,b = input().split()
	a = int(a)
	b = int(b)
	print(st(a,b))