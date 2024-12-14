export function solve1(input) {
    const dataArr = input.trim().split("\n").map(line => line.split(""));
    const size_y = dataArr.length;
    const size_x = dataArr[0].length;

    const getAntinodes = (pointA, pointB) => {
        if (pointA[0] === pointB[0] && pointA[1] === pointB[1]) return [];
        const diffX = pointB[0] - pointA[0];
        const diffY = pointB[1] - pointA[1];
        const antinodes = [];
        const antinode1 = [pointB[0] + diffX, pointB[1] + diffY];
        if (antinode1[0] >= 0 && antinode1[0] < size_x && antinode1[1] >= 0 && antinode1[1] < size_y) {
            antinodes.push(antinode1);
        }
        const antinode2 = [pointA[0] - diffX, pointA[1] - diffY];
        if (antinode2[0] >= 0 && antinode2[0] < size_x && antinode2[1] >= 0 && antinode2[1] < size_y) {
            antinodes.push(antinode2);
        }
        return antinodes;
    };

    const antiniodes = Array.from({ length: size_y }, () => Array(size_x).fill("."));
    
    for (let y1 = 0; y1 < size_y; y1++) {
        for (let x1 = 0; x1 < size_x; x1++) {
            if (dataArr[y1][x1] !== ".") {
                for (let y2 = 0; y2 < size_y; y2++) {
                    for (let x2 = 0; x2 < size_x; x2++) {
                        if (dataArr[y2][x2] !== "." && dataArr[y1][x1] === dataArr[y2][x2]) {
                            const antinodes = getAntinodes([x1, y1], [x2, y2]);
                            for (const antinode of antinodes) {
                                antiniodes[antinode[1]][antinode[0]] = "#";
                            }
                        }
                    }
                }
            }
        }
    }

    const findNumAnodes = (antiniodes) => antiniodes.flat().filter(cell => cell === "#").length;

    return findNumAnodes(antiniodes);
}

export function solve2(input) {
    const dataArr = input.trim().split("\n").map(line => line.split(""));
    const size_y = dataArr.length;
    const size_x = dataArr[0].length;

    const getAllAntinodesOnLine = (pointA, pointB) => {
        if (pointA[0] === pointB[0] && pointA[1] === pointB[1]) return [];
        const diffX = pointB[0] - pointA[0];
        const diffY = pointB[1] - pointA[1];
        const antinodes = [pointA, pointB];

        let antinode = [pointA[0] + diffX, pointA[1] + diffY];
        while (antinode[0] >= 0 && antinode[0] < size_x && antinode[1] >= 0 && antinode[1] < size_y) {
            antinodes.push(antinode);
            antinode = [antinode[0] + diffX, antinode[1] + diffY];
        }

        antinode = [pointA[0] - diffX, pointA[1] - diffY];
        while (antinode[0] >= 0 && antinode[0] < size_x && antinode[1] >= 0 && antinode[1] < size_y) {
            antinodes.push(antinode);
            antinode = [antinode[0] - diffX, antinode[1] - diffY];
        }

        return antinodes;
    };

    const antiniodes = Array.from({ length: size_y }, () => Array(size_x).fill("."));

    for (let y1 = 0; y1 < size_y; y1++) {
        for (let x1 = 0; x1 < size_x; x1++) {
            if (dataArr[y1][x1] !== ".") {
                for (let y2 = 0; y2 < size_y; y2++) {
                    for (let x2 = 0; x2 < size_x; x2++) {
                        if (dataArr[y2][x2] !== "." && dataArr[y1][x1] === dataArr[y2][x2]) {
                            const antinodes = getAllAntinodesOnLine([x1, y1], [x2, y2]);
                            for (const antinode of antinodes) {
                                antiniodes[antinode[1]][antinode[0]] = "#";
                            }
                        }
                    }
                }
            }
        }
    }

    const findNumAnodes = (antiniodes) => antiniodes.flat().filter(cell => cell === "#").length;

    return findNumAnodes(antiniodes);
}
