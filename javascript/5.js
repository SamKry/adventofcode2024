export function solve1(input) {
    let data1 = [];

    const parseData1 = (lines) => {
        lines.forEach(line => {
            const numbers = line.match(/\d+/g).map(Number);
            data1.push(numbers);
        });
    };

    const getRight = (number) => {
        let rights = [];
        data1.forEach(pair => {
            if (pair[0] === number) {
                rights.push(pair[1]);
            }
        });
        return rights;
    };

    const getLeft = (number) => {
        let lefts = [];
        data1.forEach(pair => {
            if (pair[1] === number) {
                lefts.push(pair[0]);
            }
        });
        return lefts;
    };

    const checkRow = (row) => {
        const numbers = row.split(',').map(Number);
        for (let i = 0; i < numbers.length; i++) {
            const lefts = getLeft(numbers[i]);
            const rights = getRight(numbers[i]);

            for (let j = i + 1; j < numbers.length; j++) {
                if (lefts.includes(numbers[j])) {
                    return 0;
                }
            }

            for (let j = 0; j < i; j++) {
                if (rights.includes(numbers[j])) {
                    return 0;
                }
            }
        }
        return numbers[Math.floor(numbers.length / 2)];
    };

    let ans = 0;
    const [d1, d2] = input.split('\n\n').map(part => part.split('\n'));
    parseData1(d1);

    d2.forEach(line => {
        ans += checkRow(line);
    });

    return ans;
}

export function solve2(input) {
    let data1 = [];

    const parseData1 = (lines) => {
        lines.forEach(line => {
            const numbers = line.match(/\d+/g).map(Number);
            data1.push(numbers);
        });
    };

    const getRight = (number) => {
        let rights = [];
        data1.forEach(pair => {
            if (pair[0] === number) {
                rights.push(pair[1]);
            }
        });
        return rights;
    };

    const getLeft = (number) => {
        let lefts = [];
        data1.forEach(pair => {
            if (pair[1] === number) {
                lefts.push(pair[0]);
            }
        });
        return lefts;
    };

    const fixRowAndGetMiddle = (row) => {
        const numbers = row.split(',').map(Number);
        for (let n = 0; n < numbers.length; n++) {
            for (let i = 0; i < numbers.length; i++) {
                const lefts = getLeft(numbers[i]);
                const rights = getRight(numbers[i]);

                for (let j = i + 1; j < numbers.length; j++) {
                    if (lefts.includes(numbers[j])) {
                        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
                    }
                }

                for (let j = 0; j < i; j++) {
                    if (rights.includes(numbers[j])) {
                        [numbers[i], numbers[j]] = [numbers[j], numbers[i]];
                    }
                }
            }
        }
        return numbers[Math.floor(numbers.length / 2)];
    };

    const checkRow = (row) => {
        const numbers = row.split(',').map(Number);
        for (let i = 0; i < numbers.length; i++) {
            const lefts = getLeft(numbers[i]);
            const rights = getRight(numbers[i]);

            for (let j = i + 1; j < numbers.length; j++) {
                if (lefts.includes(numbers[j])) {
                    return true;
                }
            }

            for (let j = 0; j < i; j++) {
                if (rights.includes(numbers[j])) {
                    return true;
                }
            }
        }
        return false;
    };

    let ans = 0;
    const [d1, d2] = input.split('\n\n').map(part => part.split('\n'));
    parseData1(d1);

    d2.forEach(line => {
        if (checkRow(line)) {
            ans += fixRowAndGetMiddle(line);
        }
    });

    return ans;
}
