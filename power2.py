n=int(input())
d=0
for i in range(0,n):
    c=2**i
    if n==c:
        d=d+1
if d==1:
    print("yes")
else:
    print("no")
