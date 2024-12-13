import numpy as np
from collections import deque

# this code is coped from someone but cant find who :( 
# so if you are the author please let me know

class Grid:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.width, self.height = self.grid.shape
        self.visited = np.zeros((self.height, self.width), dtype=bool)

        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # directions: up, down, left, right

    def on_map(self, x, y):
        # check if x, y coord exist
        return 0 <= x < self.height and 0 <= y < self.width

    def find_plot_BFS(self, start_x, start_y):
        # Use BFS to find the connected plot starting from (start_x, start_y)
        plant_type = self.grid[start_x, start_y]
        queue = deque([(start_x, start_y)])
        self.visited[start_x, start_y] = True

        area = 0
        perimeter = 0
        cells = {(start_x, start_y)}

        while queue:
            x, y = queue.pop()
            area += 1

            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy

                if self.on_map(nx, ny):
                    if self.grid[nx, ny] == plant_type and not self.visited[nx, ny]:
                        self.visited[nx, ny] = True
                        queue.append((nx, ny))
                        cells.add((nx, ny))
                    elif self.grid[nx, ny] != plant_type:
                        perimeter += 1
                else:
                    perimeter += 1  # Out of bounds contributes to perimeter

        # Calculate the number of sides (== corners) for the plot
        sides = self.calculate_corners(cells)
        return area, perimeter, sides

    def calculate_corners(self, cells):
        # Calculate the number of corners (==sides) of the plot
        corners = 0

        for cell in cells:
            # Check for external corners
            u = (cell[0] - 1, cell[1])  # Up
            d = (cell[0] + 1, cell[1])  # Down
            r = (cell[0], cell[1] + 1)  # Right
            l = (cell[0], cell[1] - 1)  # Left
            if u not in cells and r not in cells:
                corners += 1
            if r not in cells and d not in cells:
                corners += 1
            if d not in cells and l not in cells:
                corners += 1
            if l not in cells and u not in cells:
                corners += 1

            # Check for internal corners (diagonals)
            ur = (cell[0] - 1, cell[1] + 1)  # Up-Right (diagonal)
            ul = (cell[0] - 1, cell[1] - 1)  # Up-Left (diagonal)
            dr = (cell[0] + 1, cell[1] + 1)  # Down-Right (diagonal)
            dl = (cell[0] + 1, cell[1] - 1)  # Down-Left (diagonal)
            if u in cells and r in cells and ur not in cells:
                corners += 1
            if r in cells and d in cells and dr not in cells:
                corners += 1
            if d in cells and l in cells and dl not in cells:
                corners += 1
            if l in cells and u in cells and ul not in cells:
                corners += 1

        return corners


    def calculate_price_area_perimeter(self):
        total_price_perimeter, total_price_sides = 0, 0
        self.visited.fill(False)

        for x in range(self.height):
            for y in range(self.width):
                if not self.visited[x, y]:
                    # Calculate area, perimeter, and sides for each plot
                    area, perimeter, sides = self.find_plot_BFS(x, y)
                    total_price_perimeter += area * perimeter
                    total_price_sides += area * sides

        return total_price_perimeter, total_price_sides

with open('12/data.txt') as f:
    lines = [list(row) for row in f.read().splitlines()]
    garden = Grid(lines)
    price_perimeter, price_sides = garden.calculate_price_area_perimeter()
    print("Part 1, price when using perimeter", price_perimeter)
    print("Part 2, price when using sides", price_sides)