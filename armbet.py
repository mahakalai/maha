n,k=map(int,input().split())
l=[]
for i in range(n+1,k):
    n1=i
    sum=0
    while i>0:
        rem=i%10
        sum=sum+rem**3
        i=i//10
    if n1==sum:
        l.append(n1)
for i in range(0,len(l)-1):
    print(l[i],end=" ")
print(l[-1])
