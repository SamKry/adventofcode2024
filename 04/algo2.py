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


only relevant characters:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

"""

# search for any MAS written as an X in the matrix like this:
# M.S
# .A.
# M.S


word = ["M", "A", "S"]



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

def countPairs(__foundAt_CenterOfWord):
    count = 0
    for i in range(len(__foundAt_CenterOfWord)):
        for j in range(i+1, len(__foundAt_CenterOfWord)):
            if(__foundAt_CenterOfWord[i][0] == __foundAt_CenterOfWord[j][0] and __foundAt_CenterOfWord[i][1] == __foundAt_CenterOfWord[j][1]):
                count += 1
    return count


foundCount = 0


# read line by line
matrix = []
with open(dafaFile) as f:
    for line in f:
        matrix.append(list(line.strip()))

    foundAt_CenterOfWord = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(search(i, j, 1, 1)):
                foundAt_CenterOfWord.append((i+1, j+1))
            if(search(i, j, -1, 1)):
                foundAt_CenterOfWord.append((i-1, j+1))
            if(search(i, j, 1, -1)):
                foundAt_CenterOfWord.append((i+1, j-1))
            if(search(i, j, -1, -1)):
                foundAt_CenterOfWord.append((i-1, j-1))

    foundCount = countPairs(foundAt_CenterOfWord)


    





print("Answer: ", foundCount)
