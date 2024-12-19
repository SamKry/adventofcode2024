from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor


dataFile = "python/19/data.txt"
# dataFile = "python/19/data_small.txt"


with open(dataFile) as f:
    d1, d2 = f.read().split("\n\n")
    towels = [x.strip() for x in d1.split(",") if x.strip()]
    instructions = sorted(d2.split("\n"))

towel_dict = {"r": [], "g": [], "u": [], "w": [], "b": []}
towel_length_dict = defaultdict(lambda: defaultdict(list))

for towel in towels:
    if towel[0] in towel_dict:
        towel_dict[towel[0]].append(towel)
        towel_length_dict[towel[0]][len(towel)].append(towel)


memo = {}


def isPossible(instruction: str):
    if instruction in memo:
        return memo[instruction]

    possibilities = 0
    possibleStarts = []

    # Filter candidates by length
    for length in towel_length_dict[instruction[0]]:
        if length <= len(instruction):
            possibleStarts.extend(towel_length_dict[instruction[0]][length])

    if not possibleStarts:
        memo[instruction] = 0
        return 0

    # Check possible starts
    for start in possibleStarts:
        if instruction.startswith(start):
            if len(start) == len(instruction):
                possibilities += 1
            else:
                possibilities += isPossible(instruction[len(start) :])

    memo[instruction] = possibilities
    return possibilities


def process_instruction(instruction):
    return isPossible(instruction)


# Use ThreadPoolExecutor for parallelism
with ThreadPoolExecutor() as executor:
    results = list(executor.map(process_instruction, instructions))

# Compute the final answer
ans = sum(results)
print("Answer:", ans)
