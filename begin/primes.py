
"""
Calculate all prime numbers between 1 and `limit`

A number is prime if it can only be divided by 1 and itself:

3: 3/1 and 3/3, so 3 IS prime
4: 4/1, 4/2 and 4/4, so 4 is NOT prime
5: 5/1 and 5/5, so 5 IS prime
6: 6/1, 6/2, 6/3 and 6/6, so 6 is NOT prime
...
"""

limit = 0
while not limit:
	answer = input('until how high do you want to calculate primes?\n')
	try:
		limit = int(answer)
	except ValueError:
		print('Sorry, {0} is not a valid number!'.format(answer))


for nr in range(1, limit+1):
	print('checking if {0} is prime'.format(nr))
	# check here!


