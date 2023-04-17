import json

from adapt import Result
from adapt import Record

lines = []

with open("results.txt") as file:
    for line in file:
        rssi, line = line.rstrip().split(": ")
        line = json.loads(line)
        line.append(rssi.replace("Received (RSSI = ", "").replace(")", ""))
        lines.append(line)

keys = ["force", "temperature", "pressure", "altitude_bmp", "acceleration_x", "acceleration_y", "acceleration_z", "rotation_x", "rotation_y", "rotation_z", "time", "lat", "lng", "altitude", "rssi"]

data = [{keys[i]: line[i] for i in range(len(line))} for line in lines]

result: Result = Result([Record(r["time"], r) for r in data])

for r in result:
    print(r.get("rssi"))
