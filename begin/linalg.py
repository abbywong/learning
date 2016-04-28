from matplotlib.pyplot import subplots, show
from numpy import dot, array, float32, linspace, sin, eye, ones
from numpy.linalg import norm, eig
from numpy.random import random


M = random(size=[5, 5])
v = random(size=[5])

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

print(M[1:, 3:4])
print(M[1:, 3].shape)
print(M[1:, 3:4].shape)
print(M[1:, 3:4].T.shape)
# exit()

print('scalar multiplication')
v *= 10
print('scalar addition')
v -= 5
print(v)
print('matrix multiplication')
D = dot(M, v)
print(D)

big = array([[0, 1], [2, 1]])
sml = array([[1], [-1]])
print(dot(big, sml))
# exit()
print(sml.shape)

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
print(norm(q))
q /= norm(q)
print(q)
print(norm(q))
print(dot(q, q)**0.5)

print('eigenvalues')
vals, vecs = eig(T)
print(vals)
print('first eigenvectors')
e = vecs[:, 0]
print(e)
print(norm(e))
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
print(-7.3 * ones(shape=[5, 3]))

#todo: do some linear algebra stuff!
figure, ax = subplots()
ax.scatter(x, y)
ax.plot(x, y)
ax.set_title('sin function cool')
ax.set_xlabel('x')
ax.set_ylabel('sin(2x+1)')

if __name__ == '__main__':
	show()


