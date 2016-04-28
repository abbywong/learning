
from matplotlib.pyplot import subplots, show
from numpy import genfromtxt, corrcoef, log, exp, polyfit, empty, logspace
from scipy.optimize import minimize


# load the data file
data = genfromtxt('data/brainmass.csv', delimiter=',', dtype=str)

# check what is inside
print('shape', data.shape)
print(data[:5, :10])

# extract useful data and convert to the correct data type
body  = data[1:, 1].astype(float)
brain = data[1:, 2].astype(float)
names = data[1:, 0]
for nr, name in enumerate(names):
	names[nr] = name.strip('"')
# print(names)
# print(body)
# exit()

# transform the data if needed
lbody = log(body)
lbrain = log(brain)

# calculate interesting quantities
correlation_matrix = corrcoef(lbody, lbrain)
print('the correlation of log data is', correlation_matrix[1][0])
heaviest_animal_number = body.argmax()
print('the heaviest animal is {0}, which weights {1}kg'.format(names[heaviest_animal_number], body[heaviest_animal_number]))
print('it\'s brain is {0:0f}% of it\'s mass'.format(100 * brain[heaviest_animal_number] / body[heaviest_animal_number]))
brain_percentage = (brain / body)
heaviest_brain_number = brain_percentage.argmax()
print('the animal with RELATIVELY the heaviest brain is {0}'.format(names[heaviest_brain_number]))

# make polynomial fits (least squares)
body_grid = logspace(-3, +5, num=100)
lbody_grid = log(body_grid)
lin_first, lin_zeroth = polyfit(lbody, lbrain, deg=1)
quad_second, quad_first, quad_zeroth = polyfit(lbody, lbrain, deg=2)
linear_fit = exp(lin_zeroth + lin_first * lbody_grid)
quadratic_fit = exp(quad_zeroth + quad_first * lbody_grid + quad_second * lbody_grid ** 2)

# make a better fit
# remove the dinosaurs
is_modern_animal = empty(names.shape, dtype=bool)
is_modern_animal[:] = True
for nr, name in enumerate(names):
	if name in ['Brachiosaurus', 'Triceratops', 'Dipliodocus']:
		is_modern_animal[nr] = False
lbody_nodino = lbody[is_modern_animal]
lbrain_nodino = lbrain[is_modern_animal]
print(lbody.max(), lbody_nodino.max())
nodino_first, nodino_zeroth = polyfit(lbody_nodino, lbrain_nodino, deg=1)
nodino_fit = exp(nodino_zeroth + nodino_first * lbody_grid)
# make a fit where 0kg body has nodino_first brain (through origin)
def linear_fit_function_through_zero(fit_params, body_arg, brian_arg):
	# this function predicts the brain weight based on body weight
	brain_prediction = fit_params[0] * body_arg
	prediction_errors = (brain_prediction - brian_arg)**2
	return prediction_errors.sum()
result = minimize(linear_fit_function_through_zero, x0=[lin_first],
	args=(lbody_nodino, lbrain_nodino), method='Nelder-Mead')
better_fit_slope = result.x[0]
origin_fit = exp(better_fit_slope * lbody_grid)
print('slope updated from {0} to {1}'.format(lin_first, better_fit_slope))
if not result.success:
	print('fit did not succeed!\n', result)
	exit()

# show the data in a scatter-plot
figure, axes = subplots(figsize=(15, 9))
axes.scatter(body, brain, label='data', color='blue')
axes.plot(body_grid, linear_fit, label='linear fit', color='green')
axes.plot(body_grid, quadratic_fit, label='quadratic fit', color='black')
axes.plot(body_grid, origin_fit, label='through origin', color='grey')
axes.plot(body_grid, nodino_fit, label='no dinos fit', color='red')
axes.set_title('land animal body vs brain mass')
axes.set_xlabel('body mass')
axes.set_ylabel('brain mass')
axes.set_xscale('log')
axes.set_yscale('log')
axes.set_xlim([1.4e-3, 1e5])
axes.set_ylim([1e-1, 1e4])
axes.legend(loc='upper left')

# add the interesting animal names
for x, y, name in zip(body, brain, names):
	if name in ['Human', 'Mouse', 'Rat', 'African elephant', 'Brachiosaurus', 'Triceratops', 'Dipliodocus']:
		axes.annotate(name, (x, y))

figure, axes = subplots(figsize=(12, 9))
axes.scatter(body, exp(nodino_zeroth + nodino_first * lbody) / brain, label='data', color='blue')
for x, y, name in zip(body, exp(nodino_zeroth + nodino_first * lbody) / brain, names):
	axes.annotate(name, (x, y))
axes.set_xscale('log')
axes.set_yscale('log')

# standard trick to display the plots
if __name__ == '__main__':
	show()


