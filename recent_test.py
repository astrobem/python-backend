import matplotlib.pyplot as plt
import numpy as np
import json


with open("recent_test_data.txt") as file:
    lines = [json.loads(line.rstrip()) for line in file]

keys = ["force", "temperature", "pressure", "acceleration_x", "acceleration_y", "acceleration_z", "rotation_x", "rotation_y", "rotation_z", "time", "lat", "lng", "altitude"]

data = [{keys[i]: line[i] for i in range(len(line))} for line in lines]

print(data)
