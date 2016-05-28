
from sys import stdout
from matplotlib.animation import ArtistAnimation
from matplotlib.pyplot import subplots, show
from matplotlib.cm import Reds
from numpy import zeros, where, copy
from scipy.linalg import norm
from scipy.misc import imread


"""
Load the image.
"""
# image = imread('data/flow.png')
image = imread('data/flow_small.png')
background_frac = 0.01
steps_per_frame = 10
frame_cnt = 70

"""
Create data structures.
"""
amount = zeros(image.shape[:2], dtype=int)
xflow_spd = zeros(image.shape[:2])
yflow_spd = zeros(image.shape[:2])
body_xy = where(image[:-1, :-1, -1] == 255)
body_index = list(zip(*body_xy))

"""
Construct flow speed.
"""
print('constructing & plotting flow data')
for m, n in body_index:
	redness  = image[m, n, 0] if image[m, n, 0] > 100 and image[m, n, 2] < 100 else 0
	blueness = image[m, n, 2] if image[m, n, 2] > 100 and image[m, n, 0] < 200 else 0
	xdiff = norm(image[m, n, :3] - image[m + 1, n, :3])
	ydiff = norm(image[m, n, :3] - image[m, n + 1, :3])
	xflow_spd[m, n] = (redness + blueness) * xdiff
	yflow_spd[m, n] = (redness + blueness) * ydiff
mx = 4.5 * max(xflow_spd.max(), yflow_spd.max())
xflow_spd = xflow_spd / mx + background_frac
yflow_spd = yflow_spd / mx + background_frac

"""
Show images.
"""
fig, (ax1, ax2, ax3) = subplots(1, 3, tight_layout=True, figsize=(15,12))
for ax in (ax1, ax2, ax3):
	ax.set_xticks([])
	ax.set_yticks([])
ax1.imshow(image)
ax1.set_title('image')
ax2.imshow(xflow_spd, cmap=Reds)
ax2.set_title('x-flow')
ax3.imshow(yflow_spd, cmap=Reds)
ax3.set_title('y-flow')

"""
Start animation.
"""
stdout.write('building animation')
ims = []
afig, aax = subplots(tight_layout=True, figsize=(5,12))
aax.set_xticks([])
aax.set_yticks([])
for k in range(frame_cnt):
	stdout.write('\nframe {0:2d} / {1:d} '.format(k + 1, frame_cnt))
	for j in range(steps_per_frame):
		amount[70, 5] += 10000000
		stdout.write('.')
		stdout.flush()
		old = copy(amount)
		for m, n in body_index:
			grad_flow = xflow_spd[m, n] * (old[m, n] - old[m + 1, n])
			amount[m, n] -= grad_flow
			amount[m + 1, n] += grad_flow
			if m > 0:
				grad_flow = xflow_spd[m, n] * (old[m, n] - old[m - 1, n])
				amount[m, n] -= grad_flow
				amount[m - 1, n] += grad_flow
			grad_flow = yflow_spd[m, n] * (old[m, n] - old[m, n + 1])
			amount[m, n] -= grad_flow
			amount[m, n + 1] += grad_flow
			if n > 0:
				grad_flow = yflow_spd[m, n] * (old[m, n] - old[m, n - 1])
				amount[m, n] -= grad_flow
				amount[m, n - 1] += grad_flow
	ims.append((
		# aax.imshow(127 + image // 2),
		aax.imshow(copy(amount), cmap=Reds, vmin=0, vmax=1000000, interpolation='nearest'),
		aax.annotate('frame {0:2d}/{1:d} '.format(k + 1, frame_cnt),
			xy=(1, 1), xycoords='axes fraction', ha='right', va='top'),
		aax.annotate('{0:.0f}'.format(amount.sum() / 10000000), xy=(1, 0), xycoords='axes fraction', ha='right', va='bottom'),
	))
stdout.write('\n')
anim = ArtistAnimation(fig=afig, artists=ims, repeat=True, interval=150, repeat_delay=1000,)
# anim.save('flow.mp4',)


if __name__ == '__main__':
	show()


