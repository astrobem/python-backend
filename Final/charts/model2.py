import numpy as np
import matplotlib.cbook as cbook
import matplotlib.dates as dates
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt


def gen(x, y):
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(x, y)  # Plot some data on the axes.
    plt.show()
