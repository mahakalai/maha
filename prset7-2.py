s=input()
l=list(s)
l1=[]
l2=l[::-1]
if l==l2:
	print("0")
else:
	for i in range(0,len(l)):
		if len(l1)==0:
			l1.append(l[i])
		else:
			if l1[-1]==l[i]:
				l1.remove(l1[-1])
			else:
				l1.append(l[i])
	print(len(l1))			
