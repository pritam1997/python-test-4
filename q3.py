for i in range(-999,999,1):
	s = str(i)
	c=0
	if len(s) == 4:
		l = []
		for n in s:
			if n == '-':
				continue
			l.append(int(n))
		if s[0]=='-':
			for m in range(1,3):
				q=int(s[m])
				c=c-q
			else:
				q=int(s[m])
				c=c+q
		if c==0:
			print(i)

	elif len(s)==3 and s.isnumeric():
		for m in s:
			c= c+int(m)
		if c == 0:
			print(i)
