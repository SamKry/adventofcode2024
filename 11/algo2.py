import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array

dafaFile = "11/data.txt"
# dafaFile = "11/data_small.txt"




dataArr = int2Array.toOneLineArray2(dafaFile, sepator=" ")


from functools import lru_cache

def count_stones(initial_stones, blinks):
    """
    Calculate the total number of stones after a given number of blinks.

    :param initial_stones: List of initial stone numbers.
    :param blinks: Number of blinks.
    :return: Total number of stones.
    """
    @lru_cache(None)
    def stones_after_blinks(number, remaining_blinks):
        if remaining_blinks == 0:
            return 1  # Each stone is counted as 1.

        if number == 0:
            return stones_after_blinks(1, remaining_blinks - 1)

        if len(str(number)) % 2 == 0:
            # Split the number into left and right parts.
            str_num = str(number)
            mid = len(str_num) // 2
            left = int(str_num[:mid])
            right = int(str_num[mid:])
            return (
                stones_after_blinks(left, remaining_blinks - 1)
                + stones_after_blinks(right, remaining_blinks - 1)
            )

        # Default case: multiply by 2024 and count resulting stones.
        new_number = number * 2024
        return stones_after_blinks(new_number, remaining_blinks - 1)

    # Calculate the total number of stones.
    total_stones = 0
    for stone in initial_stones:
        total_stones += stones_after_blinks(stone, blinks)

    return total_stones

# Example usage:
initial_stones = dataArr
blinks = 75
result = count_stones(initial_stones, blinks)
print(f"Total number of stones after {blinks} blinks: {result}")

# 339840465275456 too high