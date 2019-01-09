n=int(input())
l=[]
for i in range(0,n):
	if i==0 or i==1:
		l.append(1)
	else:
		c=l[i-1]+l[i-2]
		l.append(c)
for i in range(0,len(l)-1):
	print(l[i],end=" ")
print(l[-1])
