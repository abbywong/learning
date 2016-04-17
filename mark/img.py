
from matplotlib.pyplot import subplots, show, figure
from mpl_toolkits.mplot3d import Axes3D
from numpy import meshgrid
from scipy.misc import imread
from scipy.ndimage import gaussian_filter


D = imread('../data/cells.png')
print(D.shape)

fig, axes = subplots(2, 2, figsize=(10, 10))
axes[0][0].imshow(D, interpolation='nearest')
axes[1][0].imshow(D[:, :, 1], cmap='Greys', interpolation='nearest')
axes[0][1].imshow(D[:, :, 2], cmap='Greys', interpolation='nearest')
axes[1][1].imshow(D[:, :, 0], cmap='Greys', interpolation='nearest')


Dsmth = gaussian_filter(D[:, :, 0], 3)
fig2 = figure()
ax2 = Axes3D(fig2)
X, Y = meshgrid(range(Dsmth.shape[1]), range(Dsmth.shape[0]))
ax2.plot_surface(X, Y, Dsmth, cmap='rainbow')

show()


