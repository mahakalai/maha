N,k=map(int,input().split())
l=[int(a) for a in input().split()]
c=0
for i in range(0,len(l)):
	if l[i]==k:
		c=c+1
print(c)		
