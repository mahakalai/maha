from itertools import combinations
n,k=map(int,input().split())
b=len(str(n))
x=list(combinations(str(n),b-k))
x=(sorted(x))
y="".join(x[0])
print(y)
