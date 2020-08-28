t = int(input())
for i in range(t):
	x,y,z = map(int,input().split())
	if x==y and y==z:
		print("YES")
		print(x,y,z)
	elif x == y:
		if x>z:
			print("YES")
			print("1",y,z)
		else:
			print("NO")
		
	elif y==z:
		if y>x:
		
			print("YES")
			print("1",y,x)
		else:
			print("NO")
	elif z==x:
		if z > y:
			print("YES")
			print("1",y,z)
		else:
			print("NO")
			
	else:
		print("NO")