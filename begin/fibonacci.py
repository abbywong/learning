
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

def fib(x):
	# list=[]
	if x<=2:
		return 1
	return fib(x-2)+fib(x-1)
print(fib(3))
print(fib(8))
for x in range(20):
	print(fib(x))
#todo: make faster

# print(list(4-1).append.fib(4))
