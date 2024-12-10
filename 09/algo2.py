import numpy as np

dafaFile = "09/data.txt"
# dafaFile = "09/data_small.txt"

"""
example:
2333133121414131402

gets to:

00...111...2...333.44.5555.6666.777.888899

0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..

0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..

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


# return the first empty block that fits the size
def findEmptyBlock(arr, size):
    __start = 0
    for i, item in enumerate(arr):
        if item == ".":
            __start = i
            __end = i
            while __end < len(arr) and arr[__end] == ".":
                __end += 1
                if __end - __start == size:
                    return __start
    return -1
    
# print(findEmptyBlock(['.','.','1','.','.','.','2','.','.',], 8))

# clean up compressed data
# find next last block of same IDs
# find first empty block that fits the lenth of the last block
# swap them
# repeat until no more swaps are possible


reverseIndex = len(compressedData) - 1

while reverseIndex > 0:
    # find next last block of same IDs
    _lastID = compressedData[reverseIndex]
    _from = reverseIndex
    _to = reverseIndex
    if isinstance(_lastID, int):
        _to = reverseIndex
        while reverseIndex > 0 and compressedData[reverseIndex] == _lastID:
            reverseIndex -= 1
        reverseIndex += 1
        _from = reverseIndex

        # find first empty block that fits the lenth of the last block

        diff1 = _to - _from + 1

        emptyBlockIndex = findEmptyBlock(compressedData, diff1)

        if _from >= emptyBlockIndex:

            # print(
            #     "from: {} to: {} from_empty: {} diff1: {} ID: {}".format(
            #         _from, _to, emptyBlockIndex, diff1, _lastID
            #     )
            # )

            if emptyBlockIndex != -1:
                # swap them
                (
                    compressedData[_from : _to + 1],
                    compressedData[emptyBlockIndex : emptyBlockIndex + diff1],
                ) = (
                    compressedData[emptyBlockIndex : emptyBlockIndex + diff1],
                    compressedData[_from : _to + 1],
                )
                # print("".join(map(str, compressedData)))

    reverseIndex -= 1


# calculate checksum
ans = 0

for i, item in enumerate(compressedData):
    # if item is number
    if isinstance(item, int):
        ans += item * i

print("Answer: ", ans)
