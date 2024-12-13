import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array

dafaFile = "12/data.txt"
# dafaFile = "12/data_small.txt"

"""
example:
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


dataArr = char2Array.to2DArray(dafaFile)

pprint(dataArr)


def getRegion(x, y):
    # Boundary and validity check
    if not (0 <= x < len(dataArr) and 0 <= y < len(dataArr[0])):
        return []

    # Target character for the region
    target_char = dataArr[x][y]
    
    # Set to track visited cells and store the region
    visited = set()
    region = set()

    # Stack for DFS (Depth First Search)
    stack = [(x, y)]

    while stack:
        cx, cy = stack.pop()

        # Skip if already visited
        if (cx, cy) in visited:
            continue

        visited.add((cx, cy))

        # Check if the current cell matches the target character
        if dataArr[cx][cy] == target_char:
            region.add((cx, cy))

            # Add adjacent cells to the stack
            for nx, ny in [(cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)]:
                if 0 <= nx < len(dataArr) and 0 <= ny < len(dataArr[0]):
                    stack.append((nx, ny))

    # Convert the region to an array of coordinates
    return [[coord[0], coord[1]] for coord in region]




def getPermimeter(x, y):
    perimeter = 0
    char = dataArr[x][y]
    if char == " ":
        return 0
    if x - 1 < 0 or dataArr[x - 1][y] != char:
        perimeter += 1
    if y - 1 < 0 or dataArr[x][y - 1] != char:
        perimeter += 1
    if x + 1 >= len(dataArr) or dataArr[x + 1][y] != char:
        perimeter += 1
    if y + 1 >= len(dataArr[0]) or dataArr[x][y + 1] != char:
        perimeter += 1
    return perimeter


def exploreRegion(x, y):
    regions = getRegion(x, y)
    perimeter = 0
    for x, y in regions:
        perimeter += getPermimeter(x, y)

    for x, y in regions:
        dataArr[x][y] = " "
    return perimeter * len(regions)


ans = 0

for row in range(len(dataArr)):
    for col, item in enumerate(dataArr[row]):
        if item != " ":
            ans += exploreRegion(row, col)
            # pprint(dataArr)

print("Answer: ", ans)

print(getPermimeter(8, 8))
