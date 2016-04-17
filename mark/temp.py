
from matplotlib.pyplot import subplots, show
from numpy import genfromtxt, corrcoef, log, exp, polyfit, empty, logspace
from scipy.optimize import minimize


# load the data file
data = genfromtxt('../data/airquality.csv', delimiter=',', dtype=str)

# check what is inside
print('shape', data.shape)
print(data[:5, :10])

# extract useful data and convert to the correct data type
T = data[1:, 4].astype(float)
print(T)
fig, ax = subplots()
ax.hist(T)

if __name__ == '__main__':
	show()


