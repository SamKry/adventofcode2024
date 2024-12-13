import re

dafaFile = "python/05/data.txt"
# dafaFile = "python/05/data_small.txt"


"""
example

47|53
97|13
97|61
97|47

97,61,53,29,13
75,29,13
75,97,47,61,53
"""

data1 = []  # [[47, 97], [],...]


def parseData1(f):
    for line in f:
        numbers = list(map(int, re.findall(r"\d+", line)))
        data1.append(numbers)


# print(data1)


def getRight(number):
    # find number in all [0] of data1 and return all [1]
    rights = []
    for pair in data1:
        if pair[0] == number:
            rights.append(pair[1])
    return rights


def getLeft(number):
    # find number in all [1] of data1 and return all [0]
    lefts = []
    for pair in data1:
        if pair[1] == number:
            lefts.append(pair[0])
    return lefts


def fixRowAndGetMiddle(row):
    # parse into array
    numbers = list(map(int, row.split(",")))
    # bring the number to the correct order using bubble sorr and the rules from data1
    for n in range(len(numbers)):
        for i in range(len(numbers)):
            lefts = getLeft(numbers[i])
            rights = getRight(numbers[i])

            # everything after i cannot be in lefts
            for j in range(i + 1, len(numbers)):
                if numbers[j] in lefts:
                    # swap
                    numbers[i], numbers[j] = numbers[j], numbers[i]

            # everything before i cannot be in rights
            for j in range(i):
                if numbers[j] in rights:
                    # swap
                    numbers[i], numbers[j] = numbers[j], numbers[i]

    # reutrn the middle number
    return numbers[len(numbers) // 2]


def checkRow(row):
    # parse into array
    numbers = list(map(int, row.split(",")))
    for i in range(len(numbers)):
        lefts = getLeft(numbers[i])
        rights = getRight(numbers[i])

        # everything after i cannot be in lefts
        for j in range(i + 1, len(numbers)):
            if numbers[j] in lefts:
                return True

        # everything before i cannot be in rights
        for j in range(i):
            if numbers[j] in rights:
                return True

    # reutrn the middle number
    return False


ans = 0

d1, d2 = [], []
with open(dafaFile) as f1:
    d1, d2 = f1.read().split("\n\n")

d1 = d1.split("\n")
d2 = d2.split("\n")

parseData1(d1)

# read line by line
# loop over lines in f2
for line in d2:
    if checkRow(line):
        ans += fixRowAndGetMiddle(line)


print("Answer: ", ans)


# 4233 too high
# 4148 is wrong

# 4145

# 3852 too low
