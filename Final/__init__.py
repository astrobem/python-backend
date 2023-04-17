import json

from Final.models import Result
from Final.models import Record

import Final.charts.path as path

records: dict = {}

lines = []

if __name__ != "Final":
    quit()

print(f"Fetching file from file {__name__}")
with open("results/receiver.txt") as file:
    for line in file:
        rssi, line = line.rstrip().split(": ")
        line = json.loads(line)
        line.append(rssi.replace("Received (RSSI = ", "").replace(")", ""))
        lines.append(line)

records.update({"receiver": Result([Record(*record) for record in lines])})

path.gen([result.lng for result in records["receiver"]][200:],
         [result.lat for result in records["receiver"]][200:],
         [result.altitude for result in records["receiver"]][200:])

test = iter(records["receiver"])
dict(next(test))
