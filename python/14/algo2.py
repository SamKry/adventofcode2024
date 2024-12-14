import time
import numpy as np
import array
from pprint import pprint
import re
import matplotlib.pyplot as plt
import numpy as np

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

max_seconds_to_run = 100000


# pprint(board)

board = np.zeros((board_y_size, board_x_size), dtype=int)


def runAndMustContinue(instructions, secs, __board):
    p_x, p_y, v_x, v_y = instructions

    dest_x = p_x + v_x * secs
    dest_y = p_y + v_y * secs
    dest_x = dest_x % board_x_size
    dest_y = dest_y % board_y_size
    if __board[dest_y, dest_x] > 0:
        return True
    __board[dest_y, dest_x] += 1
    return False


def save_array_as_image(array, filename_int):
    # Convert array to binary: 0 -> white, >0 -> black
    binary_array = np.where(array > 0, 0, 1)  # 0 for black, 1 for white

    # Create the image plot
    plt.imshow(binary_array, cmap="gray", interpolation="nearest")
    plt.axis("off")  # Remove axes for a clean image

    # Save the image
    filename = f"img/{filename_int}.png"
    plt.savefig(filename, bbox_inches="tight", pad_inches=0)
    plt.close()


def processSecAndMustContinue(input, __sec):
    board = np.zeros((board_y_size, board_x_size), dtype=int)

    for i in input:

        if runAndMustContinue(i, __sec, board):
            return True

    save_array_as_image(board, sec)
    pprint(sec)
    return False


dataArr = []

# track time
start = time.time()

with open(dafaFile) as f:
    for line in f:
        p_x, p_y, v_x, v_y = map(int, re.findall(r"-?\d+", line))
        dataArr.append([p_x, p_y, v_x, v_y])
    for sec in range(max_seconds_to_run):
        # print("Sec: ", sec)
        if not processSecAndMustContinue(dataArr, sec):
            print("Took: ", time.time() - start)
            exit(0)
