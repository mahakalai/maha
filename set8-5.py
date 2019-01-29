s=input()
l=list(s)
m=len(l)//2
if len(l)%2==0:
	l[m]="*"
	l[m-1]="*"
	s1="".join(l)
	print(s1)
else:
	l[m]="*"
	s2="".join(l)
	print(s2)
