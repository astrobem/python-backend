value_one = [
2,
2.5,
1,
1.5,
2,
2,
2.5,
3,
3.5,
4,
1,
1.5,
2,
2.5,
3,
3.5,
0.5,
1,
2,
1.5,
2,
1.5,
0.5,
3.5
]

value_two = [
590,
660,
430,
480,
600,
590,
650,
680,
710,
750,
440,
480,
590,
650,
690,
710,
380,
450,
600,
460,
590,
480,
400,
710
]

result = []

for i in range(len(value_one)):
    result.append(value_one[i] / value_two[i])

print(result)
