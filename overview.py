
"""
int
"""
0
-7
99999999
int('10')
int(7.3)

a = 42
a += 3
print(a)
print(a % 4)


"""
float
"""
3.1415
1.0
-9999999.999
float('2.7')


"""
str (text)
"""
"hello"
'贝贝'
'1.0'
'True'
str(7)

""" string is like a list of letters """
word = '王博士'
letter = word[0]
name = '王' + '贝贝'

""" separate parts: """
line = 'elephants are really big'
words = line.split(' ')
print(words)

""" put back together """
words.append('animals')
together = ' '.join(words)
print(together)


"""
bool (yes/no)
"""
True
False
print('bool(0) =', bool(0))
print('bool(1) =', bool(1))
print('bool(2) =', bool(2))
print('bool("") =', bool(''))
print('bool("hi") =', bool('hi'))


"""
list (a collection of other things)
"""
[0, 1, 2, 3, 4, 5]
[0, 1, 2, 'baba']
[['a', 'b', 'c'], [1, 2, 3]]
family = ['baba', 'mama', 'gege', 'saozi']

""" make list of numbers automatically """
nrs = list(range(5, 12))
print(nrs)

""" change a list """
nrs.append(12)
print('second item is', nrs[1])
nrs[4] = 42
nrs[5] -= 11
print(nrs)

""" everything in list """
for person in family:
	print('the first letter of', person, 'is', person[0])

for nr in nrs:
	if nr > 10:
		print(nr, 'is larger than 10')


"""
dict (dictionary)
"""
papa_info = {'name': 'Henk', 'age': 49, 'kids': ['Stijn', 'Sjaak', 'Mara'],}
fruit_color = {'banana': 'yellow', 'pear': 'green',}

""" change a dict """
fruit_color['pear'] = 'red'
fruit_color['apple'] = 'red'
fruit_color.pop('banana')
print(fruit_color)

""" everything in dict """
for fruit, color in fruit_color.items():
	print(fruit, 'is', color)

for fruit in fruit_color.keys():
	print(fruit, 'is a fruit')

colors = ' and '.join(fruit_color.values())
print(colors)


