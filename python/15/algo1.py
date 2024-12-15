import numpy as np
import array
from pprint import pprint

dataFile = "python/15/data.txt"
dataFile = "python/15/data_medium.txt"
dataFile = "python/15/data_small.txt"

"""
example:

########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""


board = [[], []]
moves = []

with open(dataFile) as f:
    board, moves = f.read().split("\n\n")
    board = [list(x) for x in board.split("\n")]
    # remive /n from moves
    moves = list(moves.replace("\n", ""))


# find @
for x, row in enumerate(board):
    for y, item in enumerate(row):
        if item == "@":
            start_x = x
            start_y = y
            break
    else:
        continue
    break

print("Start: ", start_x, start_y)


def move(direction, x, y):
    global start_x, start_y
    item = board[x][y]
    next_x = x
    next_y = y
    if direction == "^":
        next_x -= 1
    elif direction == "v":
        next_x += 1
    elif direction == "<":
        next_y -= 1
    elif direction == ">":
        next_y += 1

    nextItem = board[next_x][next_y]

    if nextItem == "#":
        return False

    if nextItem == "." or move(direction, next_x, next_y):
        board[next_x][next_y] = item
        board[x][y] = "."
        if item == "@":
            start_x = next_x
            start_y = next_y
        return True


for _move in moves:
    print("Move: ", _move, "Start: ", start_x, start_y)
        
    move(_move, start_x, start_y)

    pprint(board)


ans = 0

for x, row in enumerate(board):
    for y, item in enumerate(row):
        if item == "O":
            ans += 100 * x + y

print("Answer: ", ans)
