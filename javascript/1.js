
export function solve1(input) {
    // Parse input data into two arrays
    const rows = input.trim().split('\n');
    const [a, b] = rows.reduce(
        ([arr1, arr2], row) => {
            const [num1, num2] = row.trim().split(/\s+/).map(Number);
            arr1.push(num1);
            arr2.push(num2);
            return [arr1, arr2];
        },
        [[], []]
    );

    // Sort the arrays
    a.sort((x, y) => x - y);
    b.sort((x, y) => x - y);

    // Calculate the absolute difference sum
    let diff = 0;
    for (let i = 0; i < a.length; i++) {
        diff += Math.abs(a[i] - b[i]);
    }

    return diff;
}

export function solve2(input) {
    // Parse input data into two arrays
    const rows = input.trim().split('\n');
    const [a, b] = rows.reduce(
        ([arr1, arr2], row) => {
            const [num1, num2] = row.trim().split(/\s+/).map(Number);
            arr1.push(num1);
            arr2.push(num2);
            return [arr1, arr2];
        },
        [[], []]
    );

    // Sort the arrays
    a.sort((x, y) => x - y);
    b.sort((x, y) => x - y);

    // Calculate similarity
    let similarity = 0;
    for (const num of a) {
        const count = b.filter((x) => x === num).length;
        similarity += num * count;
    }

    return similarity;
}
