p = input()
flag = 0

if("Danil" in p) :
	flag += 1
	if (p.count("Danil"))>1:
		flag = flag + (p.count("Danil"))

if("Olya" in p) :
	flag += 1
	if (p.count("Olya"))>1:
		flag = flag + (p.count("Olya"))

if("Slava" in p):
	flag += 1
	if (p.count("Slava"))>1:
		flag = flag + (p.count("Slava"))

if("Ann" in p):
	flag += 1
	if (p.count("Ann"))>1:
		flag = flag + (p.count("Ann"))
		
if("Nikita" in p):
	flag += 1
	if (p.count("Nikita"))>1:
		flag = flag + (p.count("Nikita"))

if flag == 1:
	print("YES")
else:
	print("NO")
