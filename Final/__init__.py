import json
import typing

from Final.models import Result
from Final.models import Record

import Final.charts.path as path
import Final.charts.model1 as model1
import Final.charts.model2 as model2
import Final.charts.model3 as model3

records: typing.Dict[str, Result] = {}

if __name__ != "Final":
    quit()

with open("results/receiver.txt") as file:
    lines = []
    for line in file:
        rssi, line = line.rstrip().split(": ")
        line = json.loads(line)
        line.append(rssi.replace("Received (RSSI = ", "").replace(")", ""))
        line[1] = line[1] - 10
        lines.append(line)

    records.update({"receiver": Result([Record(*record) for record in lines])})

with open("results/up-down.txt") as file:
    lines = []
    for line in file:
        line = json.loads(line)
        line.append(0)

        lines.append(line)

    records.update({"up-down": Result([Record(*record) for record in lines])})

"""
path.gen([result.lng for result in records["receiver"]][200:],
         [result.lat for result in records["receiver"]][200:],
         [result.altitude for result in records["receiver"]][200:])
"""
model2.gen([result.time for result in records["receiver"]],
           [result.force for result in records["receiver"]])

