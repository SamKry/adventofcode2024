self.onmessage = async ({ data }) => {
    const { day, input } = data;

    try {
        // Dynamically import the day module
        const module = await import(`../../javascript/${day}.js`);

        // Perform calculations
        const result1 = module.solve1(input);
        const result2 = module.solve2(input);

        // Send results back to the main thread
        self.postMessage({ result1, result2 });
    } catch (error) {
        // Handle errors gracefully
        self.postMessage({ error: error.message });
    }
};
