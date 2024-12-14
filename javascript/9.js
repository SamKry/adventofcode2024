
export function solve1(input) {
    let diskmap = input.trim().split('').map(n => parseInt(n));

    let space_map = [];
    let compressed = [];

    diskmap.forEach((n, i) => {
        if (i % 2 === 0) {
            compressed.push(Array(n).fill(i / 2));
        } else {
            compressed.push([]);
            space_map.push(n);
        }
    });

    let l = 1;
    let r = compressed.length - 1;

    while (l < r) {
        while (compressed[l].length < space_map[(l - 1) / 2]) {
            if (compressed[r].length == 0) {
                r -= 2;
                if (r < l)
                    break;
            }
            compressed[l].push(compressed[r].pop());
        }
        l += 2;
    }

    const checksum = compressed
        .flat()
        .map((n, i) => i * parseInt(n))
        .reduce((acc, n) => acc + n, 0);

    return checksum;
}

export function solve2(input) {
    let diskmap = input
        .trim()
        .split('')
        .map(n => parseInt(n));

    let space_map = [];
    let compressed = [];

    diskmap.forEach((n, i) => {
        if (i % 2 === 0) {
            compressed.push(Array(n).fill(i / 2));
        } else {
            compressed.push([]);
            space_map.push(n);
        }
    });

    let l = 1;
    let r = compressed.length - 1;
    let m = (l - 1) / 2 // index of the space_map

    _1: while (m < space_map.length) {
        // look for big enough space to fill
        while (compressed[r].length > space_map[m] || compressed[r].every(n => n == null)) {
            r -= 2;
            // could not find space to fill, let's try the next one
            if (r < l) {
                l += 2;
                r = compressed.length - 1;
                m = (l - 1) / 2;
            }
            // if we have filled all the blocks
            if (m >= space_map.length)
                break _1;
        }
        compressed[l].push(...compressed[r]);          // fill the block
        space_map[m] -= compressed[r].length;          // update the space map
        compressed[r] = compressed[r].map(n => null);  // clear the block
        r = compressed.length - 1;                     // reset the pointer
    }

    // fill the remaining space with nulls
    for (let i = 1; i < compressed.length; i += 2)
        compressed[i].push(...Array(space_map[(i - 1) / 2]).fill(null));

    const checksum = compressed
        .filter(a => a.length > 0)
        .map(a => a.length == 0 ? [0] : a)
        .flat()
        .map((n, i) => n == null ? 0 : i * parseInt(n))
        .reduce((acc, n) => acc + n, 0);

    return checksum;
}
