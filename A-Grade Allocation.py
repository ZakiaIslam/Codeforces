t = int(input())
for x in range(t):
	n,m = map(int,input().split())
	li = [int(x) for x in input().split()]
	s = sum(li)
	if s > m:
		print(m)
	else:
		print(s)
