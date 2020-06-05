#import math
s1 = input()
s1 = s1.lower()
s2 = input()
s2 = s2.lower()
li1 = [ord(x) for x in s1]
li2 = [ord(x) for x in s2]
lis1=0
lis2 =0

c=0

for i in range(len(li1)):
     lis1 += li1[i]

for i in range(len(li1)):
   lis2 += li2[i]


#else:
for i in range(len(li1)):
    if li1[i]>li2[i]:
        print(1)
        break
    elif li1[i]<li2[i]:
        print(-1)
        break
    else:
        c +=1

if (c==len(li2)):
     print(0)



# for i in range(len(li1)):
#     lis1 += li1[i]
#
# for i in range(len(li1)):
#     lis2 += li2[i]
#
#
# if (lis1>lis2):
#     print(1)
# elif(lis1<lis2):
#     print(-1)
# else:
#     print(0)
