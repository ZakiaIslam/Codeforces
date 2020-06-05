n,k = input().split()
n = int(n)
k = int(k)


for i in range(k):
	if (n%10):
		n = n - 1
	else:
		n = n//10

print(n)