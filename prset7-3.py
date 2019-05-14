s=input()
l=list(s)
l1=[]
for i in range(0,len(l)):
	if l[i] not in l1:
		l1.append(l[i])
	else:
		break
print(len(l1))
