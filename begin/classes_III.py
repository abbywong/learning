
"""
Now another advantage of classes: you can teach them actions! Which are just like functions.
"""

class Fruit:
	def __init__(self, name, color, is_tasty=True):
		"""
			__init__ is a special function, similar to sqrt(), that is run when you add a fruit.
			`self` is a special variable box that is the specific fruit, like banana or pear. It'll be clear later.
		"""
		self.name = name
		self.color = color
		self.is_tasty = is_tasty
		self.is_crushed=False

	def eat(self):
		"""
		Eat the fruit!
		"""
		if self.is_tasty:
			print('you eat a', self.name, 'and it is delicious!')
		else:
			print('you eat a', self.name, 'but it is not tasty...')

	def paint(self, paint_color):
		"""
		Paint the fruit another color
		"""
		self.color = paint_color
		print(self.name, 'is now', self.color)
	def crush(self):
		self.is_crushed=True
		print(self.name,"pung")


"""
There is a new trick here: the strawberry does not have `is_tasty`.
At __init__ you may see that it `is_tasty=True` by default!
Now, we only need to set it if it's not tasty (like banana), otherwise it's tasty.
"""
banana = Fruit(name='banana', color='yellow', is_tasty=False)
pear = Fruit(name='pear', color='green', is_tasty=True)
strawberry = Fruit(name='strawberry', color='red')
fruits = [banana, pear, strawberry]

"""
Let's try eating all the fruits!
"""
for fruit in fruits:
	fruit.eat()

"""
Now let's paint the bananas red.
"""

for fruit in fruits:
	if fruit.color == 'red':
		print(fruit.name)

fruits[0].paint(paint_color='red')

for fruit in fruits:
	if fruit.color == 'red':
		print(fruit.name)

for fruit in fruits:
	if fruit.is_crushed==True:
		print(fruit.name, 'is crushed, throw it away!')

fruits[1].crush()

for fruit in fruits:
	if fruit.is_crushed==True:
		print(fruit.name, 'is crushed, throw it away!')
for fruit in fruits:
	if fruit.is_tasty==False:
		fruit.crush()