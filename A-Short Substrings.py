t = int(input())
for x in range(t):
	a = []
	b = input()
	for i in range(len(b)):
		if ((i%2)==0):
			a.append(b[i])
	if (len(b)%2==0):
		a.append(b[-1])
	s ="".join(a)
	print(s)
