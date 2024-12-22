from collections import defaultdict
from itertools import pairwise
import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array

dataFile = "python/22/data.txt"
dataFile = "python/22/data_small.txt"


dataArr = int2Array.toArray(dataFile)

pprint(dataArr)


def mix(secretnumber, value):
    return secretnumber ^ value


def prune(secretnumber):
    return secretnumber % 16777216


def getOnesDigit(secretnumber):
    return secretnumber % 10


def findFirstOccurance(sequence: array, searchedSequence: array):
    for i in range(len(sequence)):
        if sequence[i : i + len(searchedSequence)] == searchedSequence:
            if i + len(searchedSequence) < len(sequence):
                return sequence[i + len(searchedSequence)]
    return -1


def calcSecretNumberSequence(code, times):
    secretNumber = code
    sequence = []
    for i in range(times):
        secretNumber = mix(secretNumber, secretNumber * 64)
        secretNumber = prune(secretNumber)

        secretNumber = mix(secretNumber, secretNumber // 32)
        secretNumber = prune(secretNumber)

        secretNumber = mix(secretNumber, secretNumber * 2048)
        secretNumber = prune(secretNumber)

        sequence.append(getOnesDigit(secretNumber))

    return sequence


def findPatterns(seeds):
    pattern_scores = defaultdict(int)

    for seed in seeds:
        seen_patterns = set()
        prices = []
        for s in seed:
            prices.append(getOnesDigit(s))

        deltas = []
        for a, b in pairwise(prices):
            deltas.append(b - a)

        for i, quad in enumerate(
            zip(deltas, deltas[1:], deltas[2:], deltas[3:]), start=4
        ):
            if quad not in seen_patterns:
                pattern_scores[quad] += prices[i]
                seen_patterns.add(quad)

    return max(pattern_scores.values(), default=0)


times = 2000

seeds = []

for code in dataArr:
    seeds.append(calcSecretNumberSequence(code, times))

answer = findPatterns(seeds)

print("Answer:", answer)
print(answer == 24)
