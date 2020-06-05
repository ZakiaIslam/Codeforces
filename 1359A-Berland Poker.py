t = int(input())

for i in range(t):
	m,n,k = map(int,input().split())
	c = m//k
	if ((n==0)or(m==n)):
		print(0)
		continue
	if (c >= n):
		print(n)
		continue
	if(c<n):
		r = (n-c)%(k-1)
		v = (n-c)//(k-1)
		if r == 0:
			print(c-v)
		else:
			print(c-v-1)