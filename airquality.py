
from matplotlib.pyplot import subplots, show
from numpy import genfromtxt, array


# load the data file
data = genfromtxt('data/airquality.csv', delimiter=',', dtype=str)

# check what is inside
print('shape', data.shape)
print(data[:5, :10])


# extract useful data and convert to the correct data type

for colnr in range(1, data.shape[1]):
	for pos, val in enumerate(data[: ,colnr]):
		if val == 'NA':
			data[pos, colnr] = '0'
ozone = data[1:, 1].astype(int)
solar = data[1:, 2].astype(int)
wind = data[1:, 3].astype(float)
temp = data[1:, 4].astype(int)
alldata = array([ozone, solar, wind, temp], dtype=float).T
print(alldata.shape)
names = ['ozone','solar','wind','temp']
# print(ozone)
# exit()
# brain = data[1:, 2].astype(float)
# names = data[1:, 0]
# for nr, name in enumerate(names):
# 	names[nr] = name.strip('"')
# print(names)
# print(body)
# exit()

fig, axes = subplots(4,3, figsize=(10, 14))

corrcoef

#print(alldata[:, 1].shape)
#print(alldata[:, 3].shape)
for column in range(4):
	for row in range(4):
		if column == row:
			continue
		elif column > row:
			ax = axes[column, row]
		else:
			ax = axes[column, row-1]
		# if column==row:
		# 	ax.set_delete(False)
		# 	continue
		# print(column,row)
		ax.scatter(alldata[:, column], alldata[:, row])
		ax.set_title('')
		ax.set_xlabel(names[column])
		ax.set_ylabel(names[row])
		ax.grid()
fig.tight_layout()

if __name__ == '__main__':
	show()




