import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array

dafaFile = "11/data.txt"
# dafaFile = "11/data_small.txt"




dataArr = int2Array.toOneLineArray2(dafaFile, sepator=" ")

# pprint(dataArr)



def isEvenNumDigits(num):
    return len(str(num)) % 2 == 0


def processStone(item):
    res = []
    if item == 0:
        res.append(1)
    elif isEvenNumDigits(item):
        strItem = str(item)
        res.append(int(strItem[0:len(strItem)//2]))
        res.append(int(strItem[len(strItem)//2:]))
    else:
        res.append(item * 2024)
    return res


lengths = []

for blinks in range(25):
    for i in reversed(range(len(dataArr))):
        item = dataArr[i]
        items = processStone(item)
        if len(items) == 1:
            dataArr[i] = items[0]
        else:
            dataArr.pop(i)
            for j, newItem in enumerate(items):
                dataArr.insert(i+j, newItem)
    print("blinks: ", blinks, "len: ", len(dataArr))
        

ans = len(dataArr)

print("Answer: ", ans)
