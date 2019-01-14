n= int(input())
l=[]
while n:
	rem=n%10
	l.append(rem)
	n=n//10
for i in range(len(l),1,-1):
	print(l[i-1], end=" ")
print(l[0])	
