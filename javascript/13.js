export function solve1(input) {
    const machines = parseInput(input);
    let totalPrizes = 0;
    let totalTokens = 0;

    for (const machine of machines) {
        const solution = solveMachineBruteForce(...machine);
        if (solution !== null) {
            totalPrizes++;
            totalTokens += solution;
        }
    }

    return totalTokens;
}

export function solve2(input) {
    const arr = input.split("\n\n").map(block => block.split("\n"));
    let ans = 0;

    for (const [a, b, c] of arr) {
        const [a1, a2] = a.slice(12).split(", Y+").map(Number);
        const [b1, b2] = b.slice(12).split(", Y+").map(Number);
        const [c1, c2] = c.slice(9).split(", Y=").map(num => parseInt(num) + 10000000000000);

        const denom = a2 * b1 - a1 * b2;
        const x = Math.floor((b1 * c2 - b2 * c1) / denom);
        const y = Math.floor((c1 * a2 - c2 * a1) / denom);

        if (
            x >= 0 && y >= 0 &&
            x * a1 + y * b1 === c1 &&
            x * a2 + y * b2 === c2
        ) {
            ans += 3 * x + y;
        }
    }

    return ans;
}

function solveMachineBruteForce(X_A, Y_A, X_B, Y_B, X, Y) {
    let minCost = Infinity;
    let foundSolution = false;

    for (let a = 0; a <= 100; a++) {
        for (let b = 0; b <= 100; b++) {
            const currentX = a * X_A + b * X_B;
            const currentY = a * Y_A + b * Y_B;

            if (currentX === X && currentY === Y) {
                foundSolution = true;
                const cost = 3 * a + b;
                minCost = Math.min(minCost, cost);
            }
        }
    }

    return foundSolution ? minCost : null;
}

function parseInput(input) {
    const machines = [];
    const blocks = input.trim().split("\n\n");

    for (const block of blocks) {
        const lines = block.split("\n");

        const aMatch = lines[0].match(/Button A: X\+(\d+), Y\+(\d+)/);
        const bMatch = lines[1].match(/Button B: X\+(\d+), Y\+(\d+)/);
        const prizeMatch = lines[2].match(/Prize: X=(\d+), Y=(\d+)/);

        if (aMatch && bMatch && prizeMatch) {
            const [xA, yA] = aMatch.slice(1).map(Number);
            const [xB, yB] = bMatch.slice(1).map(Number);
            const [xPrize, yPrize] = prizeMatch.slice(1).map(Number);
            machines.push([xA, yA, xB, yB, xPrize, yPrize]);
        }
    }

    return machines;
}
