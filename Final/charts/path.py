import matplotlib.pyplot as plt
import numpy as np


def gen(x: list, y: list, z: list):
	theta = np.linspace(0, 2 * np.pi)
	#  x = np.cos(theta - np.pi / 2)
	print(x)
	# y = np.sin(theta - np.pi / 2)
	print(y)
	# z = theta
	print(z)
	# fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
	# markerline, stemlines, baseline = ax.stem(x, y, z, bottom=-1, orientation='x')
	# ax.set(xlabel='x', ylabel='y', zlabel='z')

	fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
	markerline, stemlines, baseline = ax.stem(
		x, y, z, linefmt='none', bottom=np.pi)
	markerline.set_linestyle("None")

	plt.show()
