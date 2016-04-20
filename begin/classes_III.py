
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

# todo: print all RED fruits here

fruits[0].paint(paint_color='red')

# todo: print all RED fruits again


