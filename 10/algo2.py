import numpy as np
import array
from pprint import pprint

dafaFile = "10/data.txt"
# dafaFile = "10/data_small.txt"




dataArr = [] 

with open(dafaFile) as f1:
    for line in f1:
        line = line.strip()
        dataArr.append([int(x) for x in list(line)])

pprint(dataArr)


def search(row, col, dataArr, start = 0):
    
    if row < 0 or row >= len(dataArr):
        return 0
    if col < 0 or col >= len(dataArr[row]):
        return 0
    
    if dataArr[row][col] == start and start == 9:
        # dataArr[row][col] = -1
        return 1
    
    ends = 0
    if dataArr[row][col] == start:
        ends += search(row, col+1, dataArr, start+1)
        ends += search(row, col-1, dataArr, start+1)
        ends += search(row+1, col, dataArr, start+1)
        ends += search(row-1, col, dataArr, start+1)

        return ends

    return 0
    


ans = 0

for row in range(len(dataArr)):
    for i, item in enumerate(dataArr[row]):
        if item == 0:
            _dataArrCopy = np.copy(dataArr)
            found = search(row, i, _dataArrCopy)
            # print("Found: ", found)
            ans += found

print("Answer: ", ans)
