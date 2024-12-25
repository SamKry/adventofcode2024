import numpy as np
import array
from pprint import pprint

dataFile = "python/25/data.txt"
# dataFile = "python/25/data_small.txt"

"""
example:
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####
"""

with open(dataFile) as f:
    combsF = f.read().split("\n\n")

    # convert individual parts to 2D char array
    combs = []
    for c in combsF:
        co = []
        for l in c.split("\n"):
            co.append([x for x in l.strip()])
        combs.append(co)

# pprint(combs)


def convertToHeightCount(arr):
    hCount = [0] * len(arr[0])
    for col in range(len(arr[0])):
        for row in range(len(arr)):
            item = arr[row][col]
            if item == "#":
                hCount[col] += 1
    return [x - 1 for x in hCount]


locks = []
keys = []

for c in combs:
    if c[0][0] == "#":
        locks.append(convertToHeightCount(c))
    else:
        keys.append(convertToHeightCount(c))

# print("locks:")
# pprint(locks)
# print("keys:")
# pprint(keys)



def func(arg):
    pass


ans = 0

for lock in locks:
    for key in keys:
        works = True
        for i in range(len(key)):
            if key[i] + lock[i] > 5:
                works = False
                break
        print(lock, key, works)
        ans += works

print("Answer: ", ans)
