#!/usr/bin/python3

with open('15.in') as f:
    line = f.read().split(',')

v = {int(v): k + 1 for k, v in enumerate(line[:-1])}
last_spoken = line[-1]
for t in range(len(v), 30000000):
    last_added = last_spoken
    last_spoken = t - v[last_spoken] if last_spoken in v else 0
    v[last_added] = t
    if t == 2019: print(last_spoken)

print(last_spoken)
