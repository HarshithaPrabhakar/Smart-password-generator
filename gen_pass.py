from random import randint



with open('sentence.txt') as f:
    a = f.read().splitlines()
sen = []
for i in a:
	if(i!=""):
		sen.append(i)
#print(sen)
c = 0
sy = ['!','@','#','$','%','^','&','*']
for i in sen:
	#print(i)
	#x = len(i)

	s = i.split(" ")
	pa = []
	l1 = len(s)
	n = randint(0,7)
	q = randint(0,l1-1)
	#print(q)
	for j in range(0,l1):
		if(len(s[j]) > 0):
			if(j == 0):
				pa.append(sy[n])
			if(j == q):
				pa.append(str(randint(0,1000)))
			if(len(s[j]) > 0):
				pa.append(s[j][0])
	pa.append(sy[n])
	str1 = ''.join(pa)
	#print("User",c, sep='', end=":")
	print(str1)
	c = c+1

