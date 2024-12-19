import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array
import heapq

dataFile = "python/18/data.txt"
grid_size = 71


# dataFile = "python/18/data_small.txt"
# grid_size = 7


def parse_input(file_name):
    with open(file_name, "r") as f:
        lines = f.read().strip().split("\n")
    return [tuple(map(int, line.split(","))) for line in lines]

def path_exists(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return True

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == "." and (nx, ny) not in visited:
                heapq.heappush(priority_queue, (0, (nx, ny)))

    return False  # No path found

def main():
    byte_positions = parse_input(dataFile)
    
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)
    
    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = "#"
        if not path_exists(grid, start, end):
            print(f"{x},{y}")
            return

if __name__ == "__main__":
    main()
