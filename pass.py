with open('actions.txt') as f:
    a = f.read().splitlines()
actions = []
for i in a:
	if(i!=""):
		actions.append(i)
#print(actions)

with open('names.txt') as f:
    n = f.read().splitlines()
names = []
for i in n:
	if(i!=""):
		names.append(i)
#print(names)

with open('places.txt') as f:
    p = f.read().splitlines()
places = []
for i in p:
	if(i!=""):
		places.append(i)
#print(places)

sentence = []
for i in actions:
	for j in places:
		for k in names:
			s = k + " " + i + " " + j
			sentence.append(s)
for i in sentence:
	print(i)
#print(len(sentence))