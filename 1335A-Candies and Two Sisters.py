n = int(input())
r = 0
for i in range(n):
	c = int(input())
	if (c%2):
		print(int(c//2))
	else:
		print(int((c/2)-1))