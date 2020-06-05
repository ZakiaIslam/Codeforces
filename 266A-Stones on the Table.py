def sto(n,s):
	c = 0
	i = 0
	for i in range(n-1):
		if s[i]== s[i+1]:
			c += 1
	return c
	
n = int(input())	
s = input()
print(sto(n,s))