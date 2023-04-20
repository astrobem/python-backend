
import matplotlib.pyplot as plt
import numpy as np


def gen(time, data):

	print(data)

	fix, ax = plt.subplots()
	fix.set_facecolor("#04345c")

	# data = [int(d) for d in data]
	plt.plot(time, data, linewidth=2, color="white", fillstyle="full")

	# ax.set_ylim(-80, -130)

	plt.tick_params(axis='x', color='w', labelcolor='w')
	ax = plt.gca()
	ax.set_facecolor("#04345c")
	ax.xaxis.label.set_color('#6bd4cd')
	ax.tick_params(axis='x', colors='#6bd4cd')
	frame = plt.gca()
	# frame.axes.get_xaxis().set_visible(False)

	ax.spines['bottom'].set_color("#6bd4cd")
	ax.spines['top'].set_color("#04345c")
	ax.spines['right'].set_color("#04345c")
	ax.spines['left'].set_color("#6bd4cd")

	plt.ylabel('Force [ N ]')
	plt.xlabel('Time [ ms ]')
	plt.show()
