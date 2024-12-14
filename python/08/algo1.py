from pprint import pprint

dafaFile = "python/08/data.txt"
# dafaFile = "python/08/data_small.txt"

"""
example:
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

ans = 0

dataArr = []

size_x = 0
size_y = 0

def getAntinodes(point_A, point_B):
    if point_A == point_B:
        return []
    diff_x = point_B[0] - point_A[0]
    diff_y = point_B[1] - point_A[1]
    __antiniodes = []
    antinode1 = (point_B[0] + diff_x, point_B[1] + diff_y)
    if antinode1[0] >= 0 and antinode1[0] < size_x and antinode1[1] >= 0 and antinode1[1] < size_y:
        __antiniodes.append(antinode1)
    antinode2 = (point_A[0] - diff_x, point_A[1] - diff_y)
    if antinode2[0] >= 0 and antinode2[0] < size_x and antinode2[1] >= 0 and antinode2[1] < size_y:
        __antiniodes.append(antinode2)
    # print(point1, point2, " -> ", antiniodes)
    return __antiniodes

antiniodes = []

def findNumAnodes(anodes):
    numAnodes = 0
    for y in range(size_y):
        for x in range(size_x):
            if anodes[y][x] == "#":
                numAnodes += 1
    return numAnodes

with open(dafaFile) as f1:
    dataf = f1.readlines()
    for line in dataf:
        line = line.strip()
        dataArr.append(list(line))

    size_x = len(dataArr[0])
    size_y = len(dataArr)

    antiniodes = [["." for _ in range(size_x)] for _ in range(size_y)]

    for y1 in range(size_y):
        for x1 in range(size_x):
            if dataArr[y1][x1] != ".":
                for y2 in range(size_y):
                    for x2 in range(size_x):
                        if dataArr[y2][x2] != "." and dataArr[y1][x1] == dataArr[y2][x2]:
                            antiniodes_ = getAntinodes((x1, y1), (x2, y2))
                            # print(antiniodes_)
                            for antinode in antiniodes_:
                                antiniodes[antinode[1]][antinode[0]] = "#"
    ans = findNumAnodes(antiniodes)

for line in antiniodes:
    print("".join(line))

print("Answer: ", ans)
