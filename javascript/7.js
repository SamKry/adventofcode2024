export function solve1(input) {
    const buildPossibleOperators = (length) => {
        // Return a list of all possible operator combinations of the given length
        const operators = ["+", "*"];
        const product = (arr, n) => {
            if (n === 1) return arr.map(el => [el]);
            return arr.flatMap(el => product(arr, n - 1).map(comb => [el, ...comb]));
        };
        return product(operators, length);
    };

    const checkLine = (sol, numbers) => {
        const possibleOperators = buildPossibleOperators(numbers.length - 1);
        for (const op of possibleOperators) {
            let temp = numbers[0];
            for (let i = 0; i < numbers.length - 1; i++) {
                if (op[i] === "+") temp += numbers[i + 1];
                else if (op[i] === "*") temp *= numbers[i + 1];
            }
            if (temp === sol) return true;
        }
        return false;
    };

    let ans = 0;
    const lines = input.trim().split("\n");
    for (const line of lines) {
        const numbers = line.match(/\d+/g).map(Number);
        const sol = numbers.shift();
        if (checkLine(sol, numbers)) ans += sol;
    }
    return ans;
}

export function solve2(input) {
    const buildPossibleOperators = (length) => {
        // Return a list of all possible operator combinations of the given length
        const operators = ["+", "*", "||"];
        const product = (arr, n) => {
            if (n === 1) return arr.map(el => [el]);
            return arr.flatMap(el => product(arr, n - 1).map(comb => [el, ...comb]));
        };
        return product(operators, length);
    };

    const checkLine = (sol, numbers) => {
        const possibleOperators = buildPossibleOperators(numbers.length - 1);
        for (const op of possibleOperators) {
            let temp = numbers[0];
            for (let i = 0; i < numbers.length - 1; i++) {
                if (op[i] === "+") temp += numbers[i + 1];
                else if (op[i] === "*") temp *= numbers[i + 1];
                else if (op[i] === "||") temp = parseInt(temp.toString() + numbers[i + 1].toString(), 10);
            }
            if (temp === sol) return true;
        }
        return false;
    };

    let ans = 0;
    const lines = input.trim().split("\n");
    for (const line of lines) {
        const numbers = line.match(/\d+/g).map(Number);
        const sol = numbers.shift();
        if (checkLine(sol, numbers)) ans += sol;
    }
    return ans;
}
