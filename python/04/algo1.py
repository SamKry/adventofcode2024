import re

# dafaFile = "04/data.txt"
# dafaFile = "04/data_small.txt"
dafaFile = "04/Boulus/data.txt"

# data example:
"""
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

word = ["X", "M", "A", "S"]



def search(startX, startY, directionX, directionY):
    found = False
    for w in word:
        if startX < 0 or startY < 0 or startX >= len(matrix) or startY >= len(matrix[startX]):
            return 0
        if matrix[startX][startY] != w:
            return 0
        startX += directionX
        startY += directionY
    print("Found at: ", startX, startY, directionX, directionY)
    return 1


foundCount = 0


# read line by line
matrix = []
with open(dafaFile) as f:
    for line in f:
        matrix.append(list(line.strip()))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            foundCount += search(i, j, 1, 0)
            foundCount += search(i, j, 0, 1)
            foundCount += search(i, j, 1, 1)
            foundCount += search(i, j, -1, 1)
            foundCount += search(i, j, 1, -1)
            foundCount += search(i, j, -1, -1)
            foundCount += search(i, j, -1, 0)
            foundCount += search(i, j, 0, -1)

    





print("Answer: ", foundCount)
