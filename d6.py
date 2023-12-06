import re
import numpy as np

input = open("d6.txt","r")
data = input.readlines()

part = 2

times = re.findall(r'\d+', data[0])
dist = re.findall(r'\d+', data[1])
if part == 1:
    times = list(map(int, times))
    dist = list(map(int, dist))
elif part == 2:
    times = [int("".join(times))]
    dist = [int("".join(dist))]

ways = []
for tt in range(0,len(times)):
    item = times[tt]
    count = 0
    for t in range(0,item):
        speed = t
        max_dist = (item-t)*t
        if max_dist > dist[tt]:
            count+=1
    ways.append(count)

print(np.prod(ways))