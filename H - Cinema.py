def m(x,y):
	if x > y:
		return x
	else:
		return y


for i in range(int(input())):
	c,k=map(int,input().split())
	s = input()
	f =0
	b = 0
	for j in range(c):
			if s[j]=="0":
				f += 1
			else:
				b = m(b,f)	
				f = 0
	b = m(b,f)	
	if (b>k):
		print("yes")	
	else:
		print("no")	
