def yearc(a,b):
	year = 0

	while(1):
		if (a*3 > b*2):
			year += 1
			return year
		else:
			a *= 3
			b *= 2
			year += 1

a,b = input().split()
a = int(a)
b = int(b)
print(yearc(a,b))