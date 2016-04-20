
"""
The Fibonacci series is like this:

	0 1 1 2 3 5 8 13 21 34 55 89 144 ...

Can you see the pattern? Please complete the list below with at least 150 numbers (automatically).
"""
nrs=[0,1,1]
L=len(nrs)
while L<=150:
	newone=nrs[L-2]+nrs[L-1]
	nrs.append(newone)
	L=len(nrs)
print(nrs)
