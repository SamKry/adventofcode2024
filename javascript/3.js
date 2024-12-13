export function solve1(input) {
    // Regular expression pattern for matching "mul(x,y)"
    const pattern = /mul\(\d{1,3},\d{1,3}\)/g;

    // Extract matches from the input
    const matches = input.match(pattern) || [];

    // Helper function to calculate multiplication results
    const getMulAns = (seq) => {
        const numbers = seq.match(/\d+/g).map(Number);
        return numbers[0] * numbers[1];
    };

    // Sum up all multiplication results
    let ans = 0;
    matches.forEach((match) => {
        ans += getMulAns(match);
    });

    return ans;
}

export function solve2(input) {
    // Regular expressions for parsing "mul(x,y)" and control statements
    const mulPattern = /mul\((\d+),(\d+)\)/g;
    const controlPattern = /(do|don\'t)\(\)/g;

    // Parse memory for events
    const parseMemory = (memory) => {
        const events = [];

        let match;
        while ((match = mulPattern.exec(memory)) !== null) {
            events.push({ type: "mul", pos: match.index, x: Number(match[1]), y: Number(match[2]) });
        }

        while ((match = controlPattern.exec(memory)) !== null) {
            events.push({ type: "control", pos: match.index, action: match[1] });
        }

        return events.sort((a, b) => a.pos - b.pos);
    };

    // Process events
    const processEvents = (events) => {
        let enabled = true;
        let total = 0;

        events.forEach((event) => {
            if (event.type === "control") {
                enabled = event.action === "do";
            } else if (event.type === "mul" && enabled) {
                total += event.x * event.y;
            }
        });

        return total;
    };

    const events = parseMemory(input);
    return processEvents(events);
}
