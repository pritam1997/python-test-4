t="*"
for r in range(6):
	if r == 0 or r==3:
		for c in range(5):
			print(t,end="")
	else:
		for a in range(2):
			print(t,end="")
			for s in range(3):
				print(" ",end="")
			print()