import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array
import heapq

dataFile = "python/18/data.txt"
grid_size = 71
bytes = 1024

# dataFile = "python/18/data_small.txt"
# grid_size = 7
# bytes = 12


def parse_input(file_name):
    with open(file_name, "r") as f:
        lines = f.read().strip().split("\n")
    return [tuple(map(int, line.split(","))) for line in lines]


def simulate_falling_bytes(grid_size, byte_positions):
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    for x, y in byte_positions:
        grid[y][x] = "#"
    return grid


def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    priority_queue = [(0, start)]
    visited = set()
    g_cost = {start: 0}

    while priority_queue:
        current_cost, current = heapq.heappop(priority_queue)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return current_cost

        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < cols and 0 <= ny < rows and grid[ny][nx] == ".":
                new_cost = g_cost[current] + 1
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    heapq.heappush(priority_queue, (new_cost, (nx, ny)))

    return float("inf")  # No path found


# Read and parse the input
byte_positions = parse_input(dataFile)

grid = simulate_falling_bytes(grid_size, byte_positions[:bytes])
# pprint(grid)

start = (0, 0)
end = (grid_size - 1, grid_size - 1)
result = shortest_path(grid, start, end)

print(f"The minimum number of steps needed to reach the exit is: {result}")
