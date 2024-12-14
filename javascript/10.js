export function solve1(input) {
    const dataArr = input.split('\n').map(line => line.split('').map(Number));

    function search(row, col, dataArr, start = 0) {
        if (row < 0 || row >= dataArr.length) return 0;
        if (col < 0 || col >= dataArr[row].length) return 0;

        if (dataArr[row][col] === start && start === 9) {
            dataArr[row][col] = -1;
            return 1;
        }

        let ends = 0;
        if (dataArr[row][col] === start) {
            ends += search(row, col + 1, dataArr, start + 1);
            ends += search(row, col - 1, dataArr, start + 1);
            ends += search(row + 1, col, dataArr, start + 1);
            ends += search(row - 1, col, dataArr, start + 1);
        }

        return ends;
    }

    let ans = 0;

    for (let row = 0; row < dataArr.length; row++) {
        for (let col = 0; col < dataArr[row].length; col++) {
            if (dataArr[row][col] === 0) {
                const _dataArrCopy = JSON.parse(JSON.stringify(dataArr));
                ans += search(row, col, _dataArrCopy);
            }
        }
    }

    return ans;
}

export function solve2(input) {
    const dataArr = input.split('\n').map(line => line.split('').map(Number));

    function search(row, col, dataArr, start = 0) {
        if (row < 0 || row >= dataArr.length) return 0;
        if (col < 0 || col >= dataArr[row].length) return 0;

        if (dataArr[row][col] === start && start === 9) {
            return 1;
        }

        let ends = 0;
        if (dataArr[row][col] === start) {
            ends += search(row, col + 1, dataArr, start + 1);
            ends += search(row, col - 1, dataArr, start + 1);
            ends += search(row + 1, col, dataArr, start + 1);
            ends += search(row - 1, col, dataArr, start + 1);
        }

        return ends;
    }

    let ans = 0;

    for (let row = 0; row < dataArr.length; row++) {
        for (let col = 0; col < dataArr[row].length; col++) {
            if (dataArr[row][col] === 0) {
                const _dataArrCopy = JSON.parse(JSON.stringify(dataArr));
                ans += search(row, col, _dataArrCopy);
            }
        }
    }

    return ans;
}
