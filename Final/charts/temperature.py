import matplotlib.pyplot as plt
import numpy as np


def gen(x, y):

    # x = np.linspace(0.1, 2 * np.pi, 41)
    # y = np.exp(np.sin(x))

    plt.stem(x, y)
    plt.show()
