import numpy as np
import array

import re

dafaFile = "python/09/data.txt"
# dafaFile = "python/09/data_small.txt"

"""
example:
2333133121414131402

gets to:

00...111...2...333.44.5555.6666.777.888899
009..111...2...333.44.5555.6666.777.88889.
0099.111...2...333.44.5555.6666.777.8888..
00998111...2...333.44.5555.6666.777.888...
009981118..2...333.44.5555.6666.777.88....
0099811188.2...333.44.5555.6666.777.8.....
009981118882...333.44.5555.6666.777.......
0099811188827..333.44.5555.6666.77........
00998111888277.333.44.5555.6666.7.........
009981118882777333.44.5555.6666...........
009981118882777333644.5555.666............
00998111888277733364465555.66.............
0099811188827773336446555566..............

"""


dataArr = []  # [2, 3, 3..]
compressedData = []

with open(dafaFile) as f1:
    for line in f1:
        for c in line:
            dataArr.append(int(c))

currentID = 0



# eg for len=3 and id = 6 : [6, 6, 6]
def getData(length):
    global currentID
    data = []
    for i in range(length):
        data.append(currentID)
    currentID += 1
    return data


# for len= 3: ['.', '.', '.']
def getFillData(length):
    char = "."
    data = []
    for i in range(length):
        data.append(char)
    return data


# build compressed data
for i, item in enumerate(dataArr):
    if i % 2 == 1:
        compressedData += getFillData(item)
    else:
        compressedData += getData(item)


# compress data
# reverse loop over compressed data



currIndex = 0

for i in reversed(range(len(compressedData))):
    item = compressedData[i]
    if isinstance(item, int):
        while currIndex < len(compressedData) and compressedData[currIndex] != ".":
            currIndex += 1
        if currIndex >= len(compressedData):
            break
        compressedData[currIndex] = item
        compressedData[i] = "."
    if(i-3 < currIndex):
        break


ans = 0

for i, item in enumerate(compressedData):
    # if item is number
    if isinstance(item, int):
        ans += item * i

print("Answer: ", ans)
