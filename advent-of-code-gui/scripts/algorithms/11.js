// JavaScript implementation of the efficient frequency-based approach
function countStones(input, blinks) {
    // Parse input and initialize frequency map
    let stones = input.split(" ");
    let stoneCounts = {};

    // Initialize the frequency map with the initial stones
    stones.forEach(stone => {
        stoneCounts[stone] = (stoneCounts[stone] || 0) + 1;
    });

    // Perform transformations for each blink
    for (let i = 0; i < blinks; i++) {
        let newStones = {};

        for (let [stone, count] of Object.entries(stoneCounts)) {
            let stoneInt = parseInt(stone, 10);

            if (stoneInt === 0) {
                newStones["1"] = (newStones["1"] || 0) + count;
            } else if (stone.length % 2 === 0) {
                let mid = stone.length / 2;
                let left = stone.slice(0, mid);
                let right = stone.slice(mid);

                newStones[left] = (newStones[left] || 0) + count;
                newStones[String(parseInt(right, 10))] = (newStones[String(parseInt(right, 10))] || 0) + count;
            } else {
                let newStone = String(stoneInt * 2024);
                newStones[newStone] = (newStones[newStone] || 0) + count;
            }
        }

        stoneCounts = newStones;
    }

    // Sum up the total number of stones
    return Object.values(stoneCounts).reduce((sum, count) => sum + count, 0);
}

export function solve1(input) {
    return countStones(input, 25);
}

export function solve2(input) {
    return countStones(input, 75);
}