s = input("Enter word : ")
r = [x for x in s]
r.reverse()
s=str()
for i in r:
	s=s+i
print(s)