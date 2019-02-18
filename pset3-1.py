l1=[int(x) for x in input().split()]
l2=[int(x) for x in input().split()]
l3=[int(x) for x in input().split()]
if l1[0]==l2[0] and l2[0]==l3[0] and l3[0]==l1[0]:
	print("yes")
elif l1[1]==l2[1] and l2[1]==l3[1] and l3[1]==l1[1]:	
	print("yes")
else:
	print("no")
