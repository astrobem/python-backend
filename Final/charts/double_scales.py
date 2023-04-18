import numpy as np
import matplotlib.pyplot as plt

def gen(x, y_one, y_two):

    # Create some mock data
    #t = np.arange(0.01, 10.0, 0.01)
    #data1 = np.exp(t)
    #data2 = np.sin(2 * np.pi * t)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (miliseconds)')
    ax1.set_ylabel('temperature', color=color)
    ax1.plot(x, y_one, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('pressure', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, y_two, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
