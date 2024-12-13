
export function solve1(input) {
    // Parse input data line by line
    const rows = input.trim().split('\n');

    // Maximum allowed difference
    const MAX_DIFF = 3;

    // Helper functions
    const isSameLevel = (numbers) => {
        for (let i = 1; i < numbers.length; i++) {
            if (numbers[i] === numbers[i - 1]) {
                return true;
            }
        }
        return false;
    };

    const isDiffTooMuch = (numbers) => {
        for (let i = 1; i < numbers.length; i++) {
            if (Math.abs(numbers[i] - numbers[i - 1]) > MAX_DIFF) {
                return true;
            }
        }
        return false;
    };

    const isChangingDirection = (numbers) => {
        const directionUp = numbers[1] > numbers[0];
        for (let i = 1; i < numbers.length; i++) {
            if ((numbers[i] > numbers[i - 1]) !== directionUp) {
                return true;
            }
        }
        return false;
    };

    const isSafe = (numbers) => {
        if (isSameLevel(numbers)) return false;
        if (isDiffTooMuch(numbers)) return false;
        if (isChangingDirection(numbers)) return false;
        return true;
    };

    // Count safe lines
    let safeCounter = 0;
    rows.forEach((line) => {
        const numbers = line.trim().split(/\s+/).map(Number);
        if (isSafe(numbers)) safeCounter++;
    });

    return safeCounter;
}

export function solve2(input) {
    // Parse input data line by line
    const rows = input.trim().split('\n');

    // Maximum allowed difference
    const MAX_DIFF = 3;

    // Helper functions
    const isSameLevel = (numbers) => {
        for (let i = 1; i < numbers.length; i++) {
            if (numbers[i] === numbers[i - 1]) {
                return true;
            }
        }
        return false;
    };

    const isDiffTooMuch = (numbers) => {
        for (let i = 1; i < numbers.length; i++) {
            if (Math.abs(numbers[i] - numbers[i - 1]) > MAX_DIFF) {
                return true;
            }
        }
        return false;
    };

    const isChangingDirection = (numbers) => {
        const directionUp = numbers[1] > numbers[0];
        for (let i = 1; i < numbers.length; i++) {
            if ((numbers[i] > numbers[i - 1]) !== directionUp) {
                return true;
            }
        }
        return false;
    };

    const isSafe = (numbers) => {
        for (let i = 0; i < numbers.length; i++) {
            const newNumbers = [...numbers];
            newNumbers.splice(i, 1);
            if (
                !isSameLevel(newNumbers) &&
                !isDiffTooMuch(newNumbers) &&
                !isChangingDirection(newNumbers)
            ) {
                return true;
            }
        }
        return false;
    };

    // Count safe lines
    let safeCounter = 0;
    rows.forEach((line) => {
        const numbers = line.trim().split(/\s+/).map(Number);
        if (isSafe(numbers)) safeCounter++;
    });

    return safeCounter;
}
