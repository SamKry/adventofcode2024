dafaFile = "02/data.txt"
# dafaFile = "02/data_small.txt"

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


# remove a level one by one an chech if it is safe if we remove jus tone level
def is_safe(numbers):

    __unsafeCounter = 0

    for i in range(0, len(numbers)):
        newNumbers = numbers.copy()
        newNumbers.pop(i)
        if (
            not is_same_level(newNumbers)
            and not is_diff_too_much(newNumbers)
            and not is_changing_direction(newNumbers)
        ):
            return True


    return False

    # if(is_same_level(numbers)):
    #     return False
    # if(is_diff_too_much(numbers)):
    #     return False
    # if(is_changing_direction(numbers)):
    #     return False
    # return True


saveCounter = 0

# read line by line
with open(dafaFile) as f:
    for line in f:
        # line format: "7 6 4 2 1"

        # make array of integers
        numbers = list(map(int, line.split()))
        saveCounter += is_safe(numbers)
        # print(numbers, is_safe(numbers))

print(saveCounter)
