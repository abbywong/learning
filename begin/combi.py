
"""
Several steps:

1. Create a function `g` with 'argument' N that generates:

	[1**2, 2**2, 3**2, ..., N**2]

and gives back (`return`) the sum of this list.

2. Use this function `g` to fill a list with the outcomes for EVEN numbers up to 150.

	[g(2), g(4), g(6), ... g(150)] =
	[5, 30, 91, ...]
"""

def g(N):
	all=[]
	for n in range(1,N+1):
		q=n**2
		all.append(q)
	return sum(all)
evenlist=[]
for N in range (2,151):
	if N%2==0:
		evenlist.append(g(N))
print(evenlist)
print(g(150))




