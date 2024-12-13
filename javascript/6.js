export function solve1(input) {
    const directions = ['^', '>', 'v', '<'];
    const map = input.trim().split('\n').map(line => [...line]);

    let x = 0, y = 0, currentDirection = null;

    // Find the initial position and direction
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (directions.includes(map[i][j])) {
                x = i;
                y = j;
                currentDirection = map[i][j];
            }
        }
    }

    let count = 0, finish = false;
    while (!finish) {
        let lookaheadX = x, lookaheadY = y;

        // Determine the next position
        if (currentDirection === '^') lookaheadX--;
        else if (currentDirection === '>') lookaheadY++;
        else if (currentDirection === 'v') lookaheadX++;
        else if (currentDirection === '<') lookaheadY--;

        // Handle boundary and obstacle cases
        if (lookaheadX >= 0 && lookaheadX < map.length && lookaheadY >= 0 && lookaheadY < map[0].length && map[lookaheadX][lookaheadY] === '#') {
            currentDirection = directions[(directions.indexOf(currentDirection) + 1) % directions.length];
        } else {
            x = lookaheadX;
            y = lookaheadY;
        }

        // Check for finishing conditions
        if (lookaheadX < 0 || lookaheadX >= map.length || lookaheadY < 0 || lookaheadY >= map[0].length) {
            count++;
            finish = true;
        } else if (map[x][y] === '.') {
            count++;
            map[x][y] = 'X';
        }
    }

    return count;
}

export function solve2(input) {
    const directions = ['^', '>', 'v', '<'];
    const map = input.trim().split('\n').map(line => [...line]);

    let x = 0, y = 0, currentDirection = null;

    // Find the initial position and direction
    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (directions.includes(map[i][j])) {
                x = i;
                y = j;
                currentDirection = map[i][j];
            }
        }
    }

    let loops = 0;
    const resetGuardX = x, resetGuardY = y, resetDirection = currentDirection;

    for (let i = 0; i < map.length; i++) {
        for (let j = 0; j < map[i].length; j++) {
            if (map[i][j] !== '#' && !directions.includes(map[i][j])) {
                map[i][j] = '#';

                const directionChangeMap = map.map(line => line.map(() => 0));

                let finish = false;
                while (!finish) {
                    let lookaheadX = x, lookaheadY = y;

                    // Determine the next position
                    if (currentDirection === '^') lookaheadX--;
                    else if (currentDirection === '>') lookaheadY++;
                    else if (currentDirection === 'v') lookaheadX++;
                    else if (currentDirection === '<') lookaheadY--;

                    // Handle boundary and obstacle cases
                    if (lookaheadX >= 0 && lookaheadX < map.length && lookaheadY >= 0 && lookaheadY < map[0].length && map[lookaheadX][lookaheadY] === '#') {
                        currentDirection = directions[(directions.indexOf(currentDirection) + 1) % directions.length];
                        directionChangeMap[x][y]++;
                        if (directionChangeMap[x][y] === 4) {
                            loops++;
                            finish = true;
                        }
                    } else {
                        x = lookaheadX;
                        y = lookaheadY;
                    }

                    // Check for finishing conditions
                    if (lookaheadX < 0 || lookaheadX >= map.length || lookaheadY < 0 || lookaheadY >= map[0].length) {
                        finish = true;
                    }
                }

                map[i][j] = '.';

                // Reset map and variables
                map.forEach((line, k) => {
                    line.forEach((el, l) => {
                        if (directions.includes(el)) {
                            map[k][l] = '.';
                        }
                    });
                });

                map[resetGuardX][resetGuardY] = resetDirection;
                x = resetGuardX;
                y = resetGuardY;
                currentDirection = resetDirection;
            }
        }
    }

    return loops;
}
