s = input()
x = []
for i in range(len(s)):
	if s[i] != '+':
		x.append(s[i])
x.sort()
s = '+'.join(x)
print(s)