
"""
Please store the third powers of all HALF numbers up to 1000 in a list, then print it to the screen.

[0**3, 0.5**3, 1**3, 1.5**3, 2**3, 2.5**3, ..., 999.5**3, 1000**3]
"""
b=0
cs=[]
while b<=1000:
	c=b**3
	b=float(b+0.5)
	cs.append(c)
print(cs)




