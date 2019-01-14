s=input()
l=list(s)
c=0
d=0
for i in range(0,len(l)):
	if l[i].isnumeric():
		c=c+1
	elif l[i].isalpha():
		d=d+1
	else:
		continue
if c>0 and d>0:
	print("Yes")
else:
	print("No")
