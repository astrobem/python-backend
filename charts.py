import matplotlib.pyplot as plt
import numpy as np
import json

from models.Charts import MultiChart

plt.style.use('_mpl-gallery')

with open("ascending.txt") as file:
    lines = [json.loads(line.rstrip()) for line in file]
data = {}
for line in lines:
    for key, value in line.items():
        data.update({key: []})

for line in lines:
    for key, value in line.items():
        data[key].append(value)

print(data)

MultiChart.four("General data", **data)
