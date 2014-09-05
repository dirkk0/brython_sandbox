import sys
import random

map = []

for i in range(3):
    map.append([])
    for j in range(3):
        map[i].append(random.randrange(2))

print(map)