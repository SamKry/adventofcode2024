export function solve1(input) {
    // Define the word sequence to search
    const word = ["X", "M", "A", "S"];

    // Helper function to perform directional search
    const search = (matrix, startX, startY, directionX, directionY) => {
        for (let i = 0; i < word.length; i++) {
            if (
                startX < 0 ||
                startY < 0 ||
                startX >= matrix.length ||
                startY >= matrix[startX].length ||
                matrix[startX][startY] !== word[i]
            ) {
                return 0;
            }
            startX += directionX;
            startY += directionY;
        }
        return 1;
    };

    // Parse the input into a matrix
    const matrix = input.trim().split("\n").map(line => line.split(""));

    let foundCount = 0;

    // Perform the search in all 8 directions
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            foundCount += search(matrix, i, j, 1, 0);  // Down
            foundCount += search(matrix, i, j, 0, 1);  // Right
            foundCount += search(matrix, i, j, 1, 1);  // Down-Right
            foundCount += search(matrix, i, j, -1, 1); // Up-Right
            foundCount += search(matrix, i, j, 1, -1); // Down-Left
            foundCount += search(matrix, i, j, -1, -1); // Up-Left
            foundCount += search(matrix, i, j, -1, 0);  // Up
            foundCount += search(matrix, i, j, 0, -1);  // Left
        }
    }

    return foundCount;
}

export function solve2(input) {
    // Define the word sequence to search
    const word = ["M", "A", "S"];

    // Helper function to perform directional search
    const search = (matrix, startX, startY, directionX, directionY) => {
        for (let i = 0; i < word.length; i++) {
            if (
                startX < 0 || startY < 0 || startX >= matrix.length || startY >= matrix[startX].length ||
                matrix[startX][startY] !== word[i]
            ) {
                return 0;
            }
            startX += directionX;
            startY += directionY;
        }
        return 1; // Return center of the word
    };

    // Count overlapping pairs of center points
    const countPairs = (centers) => {
        let count = 0;
        for (let i = 0; i < centers.length; i++) {
            for (let j = i + 1; j < centers.length; j++) {
                if (centers[i][0] === centers[j][0] && centers[i][1] === centers[j][1]) {
                    count++;
                }
            }
        }
        return count;
    };

    // Parse the input into a matrix
    const matrix = input.trim().split("\n").map(line => line.split(""));

    const foundAtCenters = [];

    // Perform the search in diagonal directions
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (search(matrix, i, j, 1, 1))
                foundAtCenters.push([i + 1, j + 1]);
            if (search(matrix, i, j, -1, 1))
                foundAtCenters.push([i - 1, j + 1]);
            if (search(matrix, i, j, 1, -1))
                foundAtCenters.push([i + 1, j - 1]);
            if (search(matrix, i, j, -1, -1))
                foundAtCenters.push([i - 1, j - 1]);
        }
    }


    return countPairs(foundAtCenters);
}
