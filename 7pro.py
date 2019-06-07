import math
n=int(input())
b=math.log10(n)/math.log10(2)
if math.ceil(b)==math.floor(b):
	print("0")
else:
    c=(n-1)//2
    d=c*2
    print(n-d)
