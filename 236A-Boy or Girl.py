s = input()
c = []
for i in range(len(s)):
	if s[i] not in c:
		c.append(s[i])
		
x = len(c)
if x%2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!" )