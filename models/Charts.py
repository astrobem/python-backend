import matplotlib.pyplot as plt


class MultiChart:
	yLabelBox = dict(color="white", pad=0.2, alpha=1, boxstyle="round")
	units = {
		"temperature": "Celsius",
		"pressure": "Pascals",
		"force": "Newtons",
		"altitude": "Meters"
	}

	@staticmethod
	def four(title: str = None, **data):
		keys = list(data.keys())
		fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(20, 10), layout="constrained")
		for x in range(2):
			for y in range(2):
				axs[x, y].set_title(keys[x+y])
				axs[x, y].plot(data[keys[x+y]], color='blue', marker='o', linestyle='dashed')
				axs[x, y].set_ylabel(MultiChart.units[keys[x+y]], bbox=MultiChart.yLabelBox)
				axs[x, y].annotate(keys[x+y], (0.5, 0.5),
				                   transform=axs[x, y].transAxes,
				                   ha='center', va='center', fontsize=18,
				                   color='lightblue')
		if title:
			fig.suptitle(title)
		plt.show()
