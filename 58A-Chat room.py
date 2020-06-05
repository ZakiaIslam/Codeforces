g = "hello"
s = input()
j = 0
c = 0
for i in range(len(s)):
	if s[i] == g[j]:
		j += 1
		c += 1
		if c == 5:
			break
if c == 5:
	print("YES")
else:
	print("NO")