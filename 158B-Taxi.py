n = int(input())
li = [int(x) for x in input().split()]


g4 = li.count(4)
g3 = li.count(3)
g2 = li.count(2)
g1 = li.count(1)


if g3 >= g1:  # g3=2 g1=2  =>g3 = 2, g1 = 0
    g1=0
else:
    g1 = g1 - g3

if g2%2 == 0:  #g2=2 =>g2=1
    g2 = g2//2
else:
    g2= g2//2 + 1
    if g1 > 0:
        if g1<=2:
            g1 =0
        elif g1 > 2:
            g1 = g1-2
if g1 > 0 and g1 <= 4:
    g1 = 1
else:
    if g1%4==0:
        g1 = g1//4
    else:
        g1 = g1//4 +1



t = g4+g2+g3+g1
print(t)
