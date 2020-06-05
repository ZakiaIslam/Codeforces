def hq(p):
	for i in range(len(p)):
		if (p[i]=="H" or p[i]== "Q" or p[i]=="9"):
			print("YES")
			return
	
	print("NO")

p = input()

hq(p)