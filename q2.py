v=['a','e','i','o','u']

s=input("Enter string : ")
count=0
for i in s:
	if i in v:
		count+=1

if count > 1 or count<1:
		print("PLease enter string with exactly one vowels !!!!!!!")
	
if count==1:
		print(f"Perfect string : {s}")
