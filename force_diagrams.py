import matplotlib.pyplot as plt
import numpy as np
import json

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

force = data["force"]

print(force)

force = [(f*100)/1023 for f in force]

print(force)

yLabelBox = dict(color="white", pad=0.2, alpha=1, boxstyle="round")
xLabelBox = yLabelBox
fig, axs = plt.subplots(ncols=2, nrows=1, figsize=(20, 10), layout="constrained")

x = 0
axs[x].set_title("Resultant Force")
axs[x].plot(force, color='blue', marker='o', linestyle='dashed')
axs[x].set_ylabel("Newtons",
                     bbox=yLabelBox)
axs[x].set_xlabel("Seconds",
                     bbox=xLabelBox)
x = 1

force = [f-0.24 for f in force]

axs[x].set_title("Inertia Force")
axs[x].plot(force, color='blue', marker='o', linestyle='dashed')
axs[x].set_ylabel("Newtons",
                     bbox=yLabelBox)
axs[x].set_xlabel("Seconds",
                     bbox=xLabelBox)

plt.show()
