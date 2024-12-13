

dafaFile = "python/02/data.txt"

MAX_DIFF = 3

def is_same_level(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            return True
    return False

def is_diff_too_much(numbers):
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) > MAX_DIFF:
            return True
    return False

# like: 1 2 1 or 3 2 3
def is_changing_direction(numbers):
    direction_up = numbers[1] > numbers[0]
    for i in range(1, len(numbers)):
        if (numbers[i] > numbers[i - 1]) != direction_up:
            return True
    return False

def is_safe(numbers):
    if(is_same_level(numbers)):
        return False
    if(is_diff_too_much(numbers)):
        return False
    if(is_changing_direction(numbers)):
        return False
    return True

saveCounter = 0

# read line by line
with open(dafaFile) as f:
    for line in f:
        # line format: "7 6 4 2 1"

        # make array of integers
        numbers = list(map(int, line.split()))
        saveCounter += is_safe(numbers)

print(saveCounter)