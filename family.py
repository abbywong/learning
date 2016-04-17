
answer = 'hello'
ages = []
while answer:
	answer = input('how old is the next person? ')
	try:
		age = float(answer)
	except ValueError:
		print('thats not a good age!')
	else:
		ages.append(age)

# ages = [55, 59, 30, 28,]
print(ages)
print(sum(ages))
