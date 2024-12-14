export function solve1(input) {
    class Grid {
        constructor(grid) {
            this.grid = grid.map(row => row.split(''));
            this.height = this.grid.length;
            this.width = this.grid[0].length;
            this.visited = Array.from({ length: this.height }, () => Array(this.width).fill(false));
            this.directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]; // up, down, left, right
        }

        onMap(x, y) {
            return x >= 0 && x < this.height && y >= 0 && y < this.width;
        }

        findPlotBFS(startX, startY) {
            const plantType = this.grid[startX][startY];
            const queue = [[startX, startY]];
            this.visited[startX][startY] = true;

            let area = 0, perimeter = 0;
            const cells = new Set([`${startX},${startY}`]);

            while (queue.length) {
                const [x, y] = queue.pop();
                area++;

                for (const [dx, dy] of this.directions) {
                    const nx = x + dx, ny = y + dy;

                    if (this.onMap(nx, ny)) {
                        if (this.grid[nx][ny] === plantType && !this.visited[nx][ny]) {
                            this.visited[nx][ny] = true;
                            queue.push([nx, ny]);
                            cells.add(`${nx},${ny}`);
                        } else if (this.grid[nx][ny] !== plantType) {
                            perimeter++;
                        }
                    } else {
                        perimeter++;
                    }
                }
            }

            const sides = this.calculateCorners(cells);
            return [area, perimeter, sides];
        }

        calculateCorners(cells) {
            const cellSet = new Set(cells);
            let corners = 0;

            for (const cell of cells) {
                const [x, y] = cell.split(',').map(Number);
                const u = `${x - 1},${y}`, d = `${x + 1},${y}`;
                const l = `${x},${y - 1}`, r = `${x},${y + 1}`;
                const ul = `${x - 1},${y - 1}`, ur = `${x - 1},${y + 1}`;
                const dl = `${x + 1},${y - 1}`, dr = `${x + 1},${y + 1}`;

                if (!cellSet.has(u) && !cellSet.has(r)) corners++;
                if (!cellSet.has(r) && !cellSet.has(d)) corners++;
                if (!cellSet.has(d) && !cellSet.has(l)) corners++;
                if (!cellSet.has(l) && !cellSet.has(u)) corners++;

                if (cellSet.has(u) && cellSet.has(r) && !cellSet.has(ur)) corners++;
                if (cellSet.has(r) && cellSet.has(d) && !cellSet.has(dr)) corners++;
                if (cellSet.has(d) && cellSet.has(l) && !cellSet.has(dl)) corners++;
                if (cellSet.has(l) && cellSet.has(u) && !cellSet.has(ul)) corners++;
            }

            return corners;
        }

        calculatePriceAreaPerimeter() {
            let totalPricePerimeter = 0, totalPriceSides = 0;
            this.visited = Array.from({ length: this.height }, () => Array(this.width).fill(false));

            for (let x = 0; x < this.height; x++) {
                for (let y = 0; y < this.width; y++) {
                    if (!this.visited[x][y]) {
                        const [area, perimeter, sides] = this.findPlotBFS(x, y);
                        totalPricePerimeter += area * perimeter;
                        totalPriceSides += area * sides;
                    }
                }
            }

            return [totalPricePerimeter, totalPriceSides];
        }
    }

    const lines = input.trim().split('\n');
    const garden = new Grid(lines);
    const [pricePerimeter, priceSides] = garden.calculatePriceAreaPerimeter();

    return pricePerimeter; // Part 1 solution
}

export function solve2(input) {
    class Grid {
        constructor(grid) {
            this.grid = grid.map(row => row.split(''));
            this.height = this.grid.length;
            this.width = this.grid[0].length;
            this.visited = Array.from({ length: this.height }, () => Array(this.width).fill(false));
            this.directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]; // up, down, left, right
        }

        onMap(x, y) {
            return x >= 0 && x < this.height && y >= 0 && y < this.width;
        }

        findPlotBFS(startX, startY) {
            const plantType = this.grid[startX][startY];
            const queue = [[startX, startY]];
            this.visited[startX][startY] = true;

            let area = 0, perimeter = 0;
            const cells = new Set([`${startX},${startY}`]);

            while (queue.length) {
                const [x, y] = queue.pop();
                area++;

                for (const [dx, dy] of this.directions) {
                    const nx = x + dx, ny = y + dy;

                    if (this.onMap(nx, ny)) {
                        if (this.grid[nx][ny] === plantType && !this.visited[nx][ny]) {
                            this.visited[nx][ny] = true;
                            queue.push([nx, ny]);
                            cells.add(`${nx},${ny}`);
                        } else if (this.grid[nx][ny] !== plantType) {
                            perimeter++;
                        }
                    } else {
                        perimeter++;
                    }
                }
            }

            const sides = this.calculateCorners(cells);
            return [area, perimeter, sides];
        }

        calculateCorners(cells) {
            const cellSet = new Set(cells);
            let corners = 0;

            for (const cell of cells) {
                const [x, y] = cell.split(',').map(Number);
                const u = `${x - 1},${y}`, d = `${x + 1},${y}`;
                const l = `${x},${y - 1}`, r = `${x},${y + 1}`;
                const ul = `${x - 1},${y - 1}`, ur = `${x - 1},${y + 1}`;
                const dl = `${x + 1},${y - 1}`, dr = `${x + 1},${y + 1}`;

                if (!cellSet.has(u) && !cellSet.has(r)) corners++;
                if (!cellSet.has(r) && !cellSet.has(d)) corners++;
                if (!cellSet.has(d) && !cellSet.has(l)) corners++;
                if (!cellSet.has(l) && !cellSet.has(u)) corners++;

                if (cellSet.has(u) && cellSet.has(r) && !cellSet.has(ur)) corners++;
                if (cellSet.has(r) && cellSet.has(d) && !cellSet.has(dr)) corners++;
                if (cellSet.has(d) && cellSet.has(l) && !cellSet.has(dl)) corners++;
                if (cellSet.has(l) && cellSet.has(u) && !cellSet.has(ul)) corners++;
            }

            return corners;
        }

        calculatePriceAreaPerimeter() {
            let totalPricePerimeter = 0, totalPriceSides = 0;
            this.visited = Array.from({ length: this.height }, () => Array(this.width).fill(false));

            for (let x = 0; x < this.height; x++) {
                for (let y = 0; y < this.width; y++) {
                    if (!this.visited[x][y]) {
                        const [area, perimeter, sides] = this.findPlotBFS(x, y);
                        totalPricePerimeter += area * perimeter;
                        totalPriceSides += area * sides;
                    }
                }
            }

            return [totalPricePerimeter, totalPriceSides];
        }
    }

    const lines = input.trim().split('\n');
    const garden = new Grid(lines);
    const [pricePerimeter, priceSides] = garden.calculatePriceAreaPerimeter();

    return priceSides; // Part 2 solution
}
