
import matplotlib.pyplot as plt
import numpy as np


def gen(time, data_one, data_two):

	fix, ax1 = plt.subplots()
	fix.set_facecolor("#04345c")

	data_one = [int(d) for d in data_one]
	data_two = [int(d) for d in data_two]
	# plt.plot(time, data_one, linewidth=2, color="white", fillstyle="full")

	ax1.set_xlabel('time [ ms ]')

	ax1.set_ylabel('Altitude [ m ]', color="#6bd4cd")
	ax1.plot(time, data_one, color="#6bd4cd", linewidth=2)
	ax1.tick_params(axis='y', labelcolor="#6bd4cd")

	ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

	ax2.set_ylabel('Pressure [ Pa ]', color="white")  # we already handled the x-label with ax1
	ax2.plot(time, data_two, color="white", linewidth=2)
	ax2.tick_params(axis='y', labelcolor="white")

	# plt.tick_params(axis='x', color='w', labelcolor='w')
	ax = plt.gca()
	ax1.set_facecolor("#04345c")
	ax.xaxis.label.set_color('#6bd4cd')
	ax.tick_params(axis='x', colors='#6bd4cd')
	#frame = plt.gca()
	# frame.axes.get_xaxis().set_visible(False)

	ax.spines['bottom'].set_color("#6bd4cd")
	ax.spines['top'].set_color("#04345c")
	ax.spines['right'].set_color("#6bd4cd")
	ax.spines['left'].set_color("#6bd4cd")

	plt.xlabel('time [ ms ]')
	plt.show()
