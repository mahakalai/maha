from itertools import combinations
n,k=map(int,input().split())
b=len(str(z))
x=list(combinations(str(z),b-k))
x=(sorted(x))
y="".join(x[0])
print(y)
