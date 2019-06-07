from itertools import permutations
n=input()
prem=[''.join(p) for p in permutations(n)]
for i in prem:
	print(i)
