n = input()
n = n.lower()
li = []
#for i in range(len(n)):

for i in range(len(n)):
    if (n[i]!="a" and n[i]!="e" and n[i]!="i" and n[i]!="o" and n[i]!="u" and n[i]!="y"):
        li.append('.')
        li.append(n[i])
        # s = n.replace(n[i], "")
        # print(s)
n = "".join([str(i) for i in li])
print(n)