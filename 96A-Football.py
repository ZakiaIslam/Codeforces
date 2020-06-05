
li = input()
def com(li,num):   #1000000001  0
    c = 0
    for i in li:    #1
        if int(i)==num:     #1==0 0==0
            c+=1
            if c >= 7:
                return True
                break
        else:
            c=0
    return False


if com(li,0) or com(li,1):
    print("YES")
else:
    print("NO")


