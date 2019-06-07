n,k=map(int,input().split())
c=1
s=str(n)
li=list(s)
if k==0:
	print(n)
else:
	while c<=k:
		li.remove(li[0])
		c=c+1
	for i in li:
		print(i,end="")
