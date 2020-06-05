n = int(input()) 
li = [int(x) for x in input().split()] 
li.sort() 
i = int((n-1)/2) 	
print(li[i])