import numpy as np
import array
from pprint import pprint
import re

dafaFile = "python/14/data.txt"
# dafaFile = "python/14/data_small.txt"


"""
example:

p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

board_x_size = 101
board_y_size = 103

# board_x_size = 11
# board_y_size = 17

seconds_to_run = 100

# pprint(board)

board = np.zeros((board_y_size, board_x_size), dtype=int)


def run(p_x, p_y, v_x, v_y, secs, __board):

    dest_x = p_x + v_x * secs
    dest_y = p_y + v_y * secs
    dest_x = dest_x % board_x_size
    dest_y = dest_y % board_y_size
    __board[dest_y, dest_x] += 1




with open(dafaFile) as f:
    board = np.zeros((board_y_size, board_x_size), dtype=int)

    for line in f:
        p_x, p_y, v_x, v_y = map(int, re.findall(r"-?\d+", line))
        run(p_x, p_y, v_x, v_y, seconds_to_run, board)


#  divide board into 4 quadrants
#  0 1
#  2 3
# the numbers on the middle line are ignored
# count nonzeros in each quadrant and then multiply the 4 quadrant counts

q0 = np.sum(board[0 : board_y_size // 2, 0 : board_x_size // 2])
q1 = np.sum(board[0 : board_y_size // 2, board_x_size // 2 + 1 : board_x_size])
q2 = np.sum(board[board_y_size // 2 + 1 : board_y_size, 0 : board_x_size // 2])
q3 = np.sum(
    board[
        board_y_size // 2 + 1 : board_y_size, board_x_size // 2 + 1 : board_x_size + 1
    ]
)

# print(q0, q1, q2, q3)

ans = q0 * q1 * q2 * q3
# pprint(board)

print("Answer: ", ans)
