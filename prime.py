n=int(input())
i=2
c=0
while i<n:
	if n%i==0:
		c=c+1
	i=i+1
if c==0:
	print("yes")
else:
	print("no")
	
