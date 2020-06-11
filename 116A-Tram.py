n = int(input())
s = 0
m = 0
for i in range(n):
	a,b = map(int,input().split())
	s = s - a + b
	if s > m:
		m = s

print(m)