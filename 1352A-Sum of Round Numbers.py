n = int(input())
for i in range(n):
	a = input()
	c = a.count("0")
	l = len(a)
	a = int(a)
	d = l-c		
	print(d)
	for j in range(d):
		a = str(a)
		if (len(a)) == 1:
			print(a)
			break
		else:
			l = len(a)-1
			v = 10** (l)
			a = int(a)
			f = int(a/v)
			print(f*v)
			a = a%v