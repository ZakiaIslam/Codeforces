#python 3.7.1

n = 5
a =[]
for x in range(n):
	a.append([int(y) for y in input().split()])
for i in range(n):
	for j in range(n):
		if a[i][j]==1 :
			r = i
			c = j

r = abs(r - 2)
c = abs(c - 2)

print(r+c)