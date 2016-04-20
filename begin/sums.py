
"""
Make a sum of numbers 0 ... 20
"""
print(list(range(0, 20+1)))
print(sum(range(0,21)))

total=0
for i in range(21):
	total=total+i
print(i, total)

def better_sum(length):
	total=0
	for i in range(length+1):
		total=total+i
	return total

print(better_sum(20))
print(better_sum(25))
print(better_sum(2000))
print(better_sum(20)-10)

def better_product(length):
	total=1
	print(list(range(1, length)))
	print(list(range(1, length+1)))
	for i in range(1, length+1):
		total=total*i
	return total

print(better_product(4))
