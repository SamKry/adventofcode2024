import numpy as np
import array
from pprint import pprint

dataFile = "python/15/data.txt"
# dataFile = "python/15/data_medium.txt"
# dataFile = "python/15/data_small.txt"
# dataFile = "python/15/data_small_2.txt"

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
    # remove /n from moves
    moves = list(moves.replace("\n", ""))


# prepare the board

"""
If the tile is #, the new map contains ## instead.
If the tile is O, the new map contains [] instead.
If the tile is ., the new map contains .. instead.
If the tile is @, the new map contains @. instead.
"""
for x, row in enumerate(board):
    for y in reversed(range(len(row))):
        item = board[x][y]
        if item == "#":
            board[x][y] = "#"
            board[x].insert(y + 1, "#")
        elif item == "O":
            board[x][y] = "["
            board[x].insert(y + 1, "]")
        elif item == ".":
            board[x][y] = "."
            board[x].insert(y + 1, ".")
        elif item == "@":
            board[x][y] = "@"
            board[x].insert(y + 1, ".")

# for row in board:
#     print("".join(row))
# pprint(moves)


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


def moveBox(direction, x, y, moveIt):

    itemLeft = board[x][y]

    if itemLeft == "]":
        y -= 1
        itemLeft = board[x][y]

    itemRight = board[x][y + 1]

    next_x = x
    next_y = y
    if direction == "^":
        next_x -= 1
    elif direction == "v":
        next_x += 1

    nextItemLeft = board[next_x][next_y]
    nextItemRight = board[next_x][next_y + 1]

    hasBoxLeft = nextItemLeft == "]"
    hasBoxRight = nextItemRight == "["
    hasBoxInfront = nextItemLeft == "["

    if nextItemLeft == "#" or nextItemRight == "#":
        return False

    if nextItemLeft == "." and nextItemRight == ".":
        if moveIt:
            board[next_x][next_y] = "["
            board[next_x][next_y + 1] = "]"
            board[x][y] = "."
            board[x][y + 1] = "."
        return True

    ok1 = True
    ok2 = True

    if hasBoxLeft or hasBoxInfront:
        if moveBox(direction, next_x, next_y, moveIt):
            ok1 = True
        else:
            ok1 = False

    if hasBoxRight:
        if moveBox(direction, next_x, next_y + 1, moveIt):
            ok2 = True
        else:
            ok2 = False

    ok = ok1 and ok2

    if moveIt and ok:
        board[next_x][next_y] = itemLeft
        board[next_x][next_y + 1] = itemRight
        board[x][y] = "."
        board[x][y + 1] = "."
    return ok

    return False


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

    if direction in ["^", "v"] and nextItem in ["[", "]"]:
        if moveBox(direction, next_x, next_y, False):

            moveBox(direction, next_x, next_y, True)

            board[next_x][next_y] = item
            board[x][y] = "."
            start_x = next_x
            start_y = next_y

            return True
        else:
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

    # pprint(board)

    # for row in board:
    #     print("".join(row))


for row in board:
    print("".join(row))
ans = 0

for x, row in enumerate(board):
    for y, item in enumerate(row):
        if item == "[":
            ans += 100 * x + y

print("Answer: ", ans)
