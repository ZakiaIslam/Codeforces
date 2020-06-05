n = int(input())
c = 0
for i in range(n):
    s = input()
    if (s == "X++"or s =="++X"):
        c +=1
    elif(s == "--X" or s == "X--"):
        c -=1

print(c)