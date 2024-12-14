export function solve1(input) {
    const boardXSize = 101;
    const boardYSize = 103;
    const secondsToRun = 100;

    const board = Array.from({ length: boardYSize }, () => Array(boardXSize).fill(0));

    function mod(n, m) {
        return ((n % m) + m) % m;
    }

    function run(pX, pY, vX, vY, secs, board) {
        const destX = mod(pX + vX * secs, boardXSize);
        const destY = mod(pY + vY * secs, boardYSize);
        board[destY][destX] += 1;
    }

    input.split("\n").forEach(line => {
        const [pX, pY, vX, vY] = line.match(/-?\d+/g).map(Number);
        run(pX, pY, vX, vY, secondsToRun, board);
    });

    const midY = Math.floor(boardYSize / 2);
    const midX = Math.floor(boardXSize / 2);

    const q0 = board.slice(0, midY).reduce((sum, row) => sum + row.slice(0, midX).reduce((a, b) => a + b, 0), 0);
    const q1 = board.slice(0, midY).reduce((sum, row) => sum + row.slice(midX + 1).reduce((a, b) => a + b, 0), 0);
    const q2 = board.slice(midY + 1).reduce((sum, row) => sum + row.slice(0, midX).reduce((a, b) => a + b, 0), 0);
    const q3 = board.slice(midY + 1).reduce((sum, row) => sum + row.slice(midX + 1).reduce((a, b) => a + b, 0), 0);

    return q0 * q1 * q2 * q3;
}

export function solve2(input) {
    const boardXSize = 101;
    const boardYSize = 103;
    const maxSecondsToRun = 100000;

    function mod(n, m) {
        return ((n % m) + m) % m;
    }

    function runAndMustContinue(instruction, secs, board) {
        const [pX, pY, vX, vY] = instruction;
        const destX = mod(pX + vX * secs, boardXSize);
        const destY = mod(pY + vY * secs, boardYSize);

        if (board[destY][destX] > 0) {
            return true;
        }
        board[destY][destX] += 1;
        return false;
    }

    function processSecAndMustContinue(dataArr, sec) {
        const board = Array.from({ length: boardYSize }, () => Array(boardXSize).fill(0));

        for (const instruction of dataArr) {
            if (runAndMustContinue(instruction, sec, board)) {
                return true;
            }
        }

        console.log(`Processed second: ${sec}`);
        return false;
    }

    const dataArr = input.split("\n").map(line =>
        line.match(/-?\d+/g).map(Number)
    );

    for (let sec = 0; sec < maxSecondsToRun; sec++) {
        if (!processSecAndMustContinue(dataArr, sec)) {
            return sec;
        }
    }

    return "Exceeded max seconds to run. Please check your input data.";
}
