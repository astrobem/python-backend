import numpy as np
import matplotlib.pyplot as plt

def gen(x, y_one, y_two):

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('time (miliseconds)')
    ax1.set_ylabel('Calculated acceleration', color=color)
    ax1.plot(x, y_one, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Dedicated sensor acceleration', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, y_two, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
