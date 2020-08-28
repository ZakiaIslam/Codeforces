t = int(input())
for x in range(t):
	n = int(input())
	li = [int(i) for i in input().split()]
	oc = 0
	ec = 0
	for i in range(len(li)):
		if (i%2==0):
			if (li[i]%2==1):
				oc += 1
		if (i%2==1):
			if (li[i]%2==0):
				ec += 1	
	if(oc == ec):
		print(oc)
	else:
		print(-1)
