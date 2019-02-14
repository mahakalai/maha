x=int(input())
sum=0
while x:
	rem=x%10
	sum=sum+(rem*rem)
	x=x//10
print(sum)
