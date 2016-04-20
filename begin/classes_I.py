
"""
Now we're found several types of things that Python can store:

* int:
	0
	-7
	99999999

* float:
	3.1415
	1.0
	-9999999.999

* str (text):
	'hello'
	'贝贝'
	'1.0'
	'True'

* bool (yes/no):
	True
	False

* list (a collection of other things):
	[0, 1, 2, 3, 4, 5]
	['baba', 'mama', 'gege', 'saozi']
	[0, 1, 2, 'baba']
	[['a', 'b', 'c'], [1, 2, 3]]

And now we'll add:
* dict (dictionary):
	papa_info = {'name': 'Henk', 'age': 49, 'kids': ['Stijn', 'Sjaak', 'Mara'],}
	fruit_color = {'banana': 'yellow', 'pear': 'green',}
"""

"""
Now we want to store someone's name, age, and the titles of their children. We could do one of these:
"""
papa_info_1 = ['Henk', 49, 'Stijn', 'Sjaak', 'Mara']
papa_info_2 = ['Henk', 49, ['Stijn', 'Sjaak', 'Mara']]

print('one way:')
print('name', papa_info_1[0])
print('age ', papa_info_1[1])
print('kids', papa_info_1[2:])

print('another way:')
print('name', papa_info_2[0])
print('age ', papa_info_2[1])
print('kids', papa_info_2[2])

"""
This can work, of course. But we have to remember that #0 is the name, #1 is the age and #3 are the children.
And maybe we'll want to add more, or store different things for different people.
There's a better way (these are two ways to write the same thing):
"""
papa_info_3 = {'name': 'Henk', 'age': 49, 'kids': ['Stijn', 'Sjaak', 'Mara'],}
papa_info_4 = {
	'name': 'Henk',
	'age': 49,
	'kids': ['Stijn', 'Sjaak', 'Mara'],
}
print('dictionary way:')
print('name', papa_info_4['name'])
print('age ', papa_info_4['age'])
print('kids', papa_info_4['kids'])

"""
This is called a 'dictionary', because there are unique words which have some info about what they are.
We could even do the above one automatically:
"""
print('automatic way:')
for dictionary_word, dictionary_meaning in papa_info_4.items():
	print(dictionary_word, '=', dictionary_meaning)

"""
We can easily add information
"""
papa_info_4['has_a_car'] = True
print('updated:')
for dictionary_word, dictionary_meaning in papa_info_4.items():
	print(dictionary_word, '=', dictionary_meaning)

"""
Unlike a (western) dictionary though, the words are in no particular order. If you run it twice, it may change! Try!
This doesn't matter, because we don't care about the 'first value', we care about the 'age' or 'name'.
"""

"""
Now you can make your own dictionary. For example, store the ages of your friends, or the colors or tastiness of fruits.
"""
ages_of_friends = {}  #todo
# print('Alice is', ages_of_friends['Alice'], 'years old')
# print('Sarah is', ages_of_friends['Sarah'], 'years old')

fruit_color = {
	'banana': 'yellow',
	'pear': 'green',
	#todo
}
fruit_is_tasty = {
	'banana': False,
	'pear': True,
	'apple': True,
	'strawberry': True
	#todo
}

"""
Now you can show all tasty fruits:
"""
for name, tasty in fruit_is_tasty.items():
	if tasty == True:
		print(name, 'is tasty')

"""
Your turn! Show all fruits that have the same color as a pear.
"""
#todo


"""
Now show all friends who are older than a number the user types.
"""
minimum_age = input('at least how old? ')
#todo


