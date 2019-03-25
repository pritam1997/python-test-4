for r in range(6):
	if r==0 or r==5:
		for c in range(5):
			print("*",end="")
		print()
	else:
		for c in range(2):
			print("*",end="    ")
		print()