
from numpy import dot, array, float32, linspace, sin, eye, ones
from numpy.linalg import norm, eig
from numpy.random import random


M = random(size=[5, 5,])
v = random(size=[5,])

print('matrix')
print(M)
print('transpose')
print(M.T)
print('vector')
print(v)
print('first row of matrix')
print(M[:, 0])
print('last column of matrix')
print(M[-1, :])
print('middle value of matrix')
print(M[2, 2])
print('3 specific values')
print(M[2, 2:5])

print('scalar multiplication')
v *= 10
print('scalar addition')
v -= 5
print('matrix multiplication')
D = dot(M, v)
print(D)

print('size')
print(D.shape)
print('type')
print(D.dtype)
print('convert')
I = D.astype(int)
print(I)

q = array([0, 1, 4, 9, 16, 25, 36], dtype=float32)
T = array([
	[ 2, -1,  0,  0],
	[-1,  2, -1,  0],
	[ 0, -1,  2, -1],
	[ 0,  0, -1,  2],
])
print('diff. matrix')
print(T)
print('some vector')
print(q)
print('normalize')
q /= norm(q)
print(q)

print('eigenvalues')
vals, vecs = eig(T)
print(vals)
print('first eigenvectors')
e = vecs[:, 0]
print(e)
print('check')
c = dot(T, e)
print(c / e / vals[0])

print('grid')
x = linspace(-5, 5, num=41)
print(x)
print('sin')
y = sin(2 * x) + 1
print(y)
print('identity matrix')
print(eye(4))
print('unity matrix (nonsquare)')
print(ones(shape=[5, 3]))

#todo: do some linear algebra stuff!


