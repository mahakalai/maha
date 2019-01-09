n,k=map(int,input().split(" "))
l=[]
for n in range(n+1,k):
    N=n
    i=2
    while i<n:
        if n%i==0:
            break
        i=i+1
    if N==i:
        l.append(N)
for i in range(0,len(l)-1):
    print(l[i],end=" ")
print(l[-1])  

    
        
        
        
