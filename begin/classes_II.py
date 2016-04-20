
"""
Dictionaries are useful, but sometimes even that is not enough.

Fruits have names, colors and tastiness. You can store it in two dictionaries like before, but there's a better way.
"""

banana = {
	'name': 'banana',
	'color': 'yellow',
	'is_tasty': False,
}
pear = {
	'name': 'pear',
	'color': 'green',
	'is_tasty': True,
}
fruits = [banana, pear]
my_fruit = fruits[1]
print(my_fruit['name'], 'is', my_fruit['color'])

"""
Can you print the name and color of all fruits?
"""
#todo


"""
There exists another way to write the above type of thing. It's more confusing now, but much more convenient later.

Let's teach the computer about a new type(class) of thing: Fruit.
"""

class Fruit:
	"""
	This is a fruit
	"""

banana = Fruit()
banana.name = 'banana'
banana.color = 'yellow'
banana.is_tasty = False

pear = Fruit()
pear.name = 'pear'
pear.color = 'green'
pear.is_tasty = True

fruits = [banana, pear]
my_fruit = fruits[1]
print(my_fruit.name, 'is', my_fruit.color)

"""
Can you print the name and color of all fruits again?
"""
#todo

"""
This is not a very short way to write it. And maybe someone will make a fruit without name. Let's solve that!
"""
class Fruit2:
	def __init__(self, name, color, is_tasty):
		"""
			__init__ is a special function, similar to sqrt(), that is run when you add a fruit.
			`self` is a special variable box that is the specific fruit, like banana or pear. It'll be clear later.
		"""
		self.name = name
		self.color = color
		self.is_tasty = is_tasty

"""
Now we make fruits like this:
"""
banana = Fruit2(name='banana', color='yellow', is_tasty=False)
pear = Fruit2(name='pear', color='green', is_tasty=True)

"""
Test that you can still print all fruits the same way as before!
"""
#todo

"""
Also test what happens if you make a fruit without name. It should not be allowed!
"""
#todo



