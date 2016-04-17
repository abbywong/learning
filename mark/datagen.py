
from matplotlib.pyplot import subplots, show
from numpy import linspace, sin, zeros, savetxt
from numpy.fft import fft, ifft
from numpy.random import randn


N = 120
x = linspace(0, +20, num=N)
s1 = 1.4 * sin(17.3 * x + 0.3)
s2 = 0.4 * sin(2 * x + 0.9)
noise = randn(*x.shape) + 12
ydata = s1 + noise


def make(a, b, c, noise=0.02):
	f = zeros((120,))
	f[7] = a
	f[19] = b
	f[25] = c
	y = ifft(f)
	z = noise * randn(x.shape[0])
	return (y + z).real

A = zeros((N, 7))
A[:, 0] = x
A[:, 1] = make(1, 0, 0, noise=0)
A[:, 2] = make(0, 1, 0, noise=0)
A[:, 3] = make(0, 0, 1, noise=0)
A[:, 4] = make(2, 2, 2, noise=0.012)
A[:, 5] = make(0.9, 2.4, 0., noise=0.01)
A[:, 6] = 10 * make(1.9, 1.2, 2.1, noise=0.015)

q = A[:, 6]

fig, (ax1, ax2) = subplots(2, 1, figsize=(10, 10))
# ax1.plot(xgrid, ydata)
# ax2.plot(fft(ydata).real)
# ax1.plot(f)
ax1.plot(x, q)
ax2.plot(fft(q).real, color='b')
ax2.plot(fft(q).imag, color='g')


if __name__ == '__main__':
	savetxt('../data/signal.csv', A, delimiter=',', header='wavelength,molecule1,molecule2,molecule3,mixtureA,mixtureB,mixtureC')
	show()


