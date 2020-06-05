k,n,w = map(int,input().split())
li = []
for i in range(w):
	li.append(i+1)

s = sum(li)
t = k*s
r = t- n
if r <0 :
	print(0)
else:
	print(r)