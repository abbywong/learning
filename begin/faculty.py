
"""
Now you can learn to make a function. Here's an example:
"""

def square(x):
	return x*x

print('squares:')
print(square(4))
print(square(11))

"""
You added a new command to the language!

Your function will be more difficult: you should calculate the faculty of a number:

1! = 1
2! = 2 * 1 = 2
3! = 3 * 2 * 1 = 6
4! = 4 * 3 * 2 * 1 = 24
...
8! = 8 * 7! = 40320

Please change the function below to be correct:
"""
def faculty(length):
	total=1
	# print(list(range(1, length)))
	# print(list(range(1, length+1)))
	for i in range(1, length+1):
		total=total*i
	return total
print(faculty(4))


#jia = ['baba', 'mama', 'gege', 'saozi', 'zhuangzhuang']
#for jiaren in jia:
	# print('hello', jiaren)
#
# print(list(range(8)))
# for i in range(10):
# 	print(i**2)

# i = 0
# while i < 10:
# 	i = i + 1
# 	print(i**2)

print('faculty:')
print(faculty(4))
# print(faculty(6))
# print(faculty(9))


