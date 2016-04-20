
from math import sqrt

"""
Make some code that calculates the long side of a right angle triangle (Pythagoras)
"""
a=float(input('短边长a\n'))
b=float(input('短边长b\n'))
c=sqrt(a**2+b**2)
print('长边长c',c)
