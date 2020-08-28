li = [int(x) for x in input().split()]
n4 = max(li)
li.remove(n4)
l = []    
for i in range(3):
	n = n4-li[i]
	l.append(n)
print(l[2],l[1],l[0])
