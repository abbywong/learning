
"""
Here is another solution of the faculty problem. Can you understand it?
"""


def faculty(n):
	if n <= 1:
		return 1
	previous = faculty(n - 1)
	return n * previous


print('faculty:')
print(4, faculty(4))
print(6, faculty(6))
print(9, faculty(9))


