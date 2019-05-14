import math
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
c=[int(x) for x in input().split()]
d=[int(x) for x in input().split()]
ab= math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
ad= math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
bc= math.sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
cd=math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
if ab==ad==bc==cd:
	print("yes")
else:
	print("no")
