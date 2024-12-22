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
    """
    To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    """
    return secretnumber ^ value


def prune(secretnumber):
    """
    To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation.
    (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    """
    return secretnumber % 16777216


def calcSecretNumber(code, times):
    """
    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    """
    secretNumber = code
    for i in range(times):
        secretNumber = mix(secretNumber, secretNumber * 64)
        secretNumber = prune(secretNumber)

        secretNumber = mix(secretNumber, secretNumber // 32)
        secretNumber = prune(secretNumber)

        secretNumber = mix(secretNumber, secretNumber * 2048)
        secretNumber = prune(secretNumber)

    return secretNumber


ans = 0

times = 2000

for code in dataArr:
    print(str(code) + ":", end=" ")
    result = calcSecretNumber(code, times)
    print(result)
    ans += result


print("Answer: ", ans)


"""
1: 8685429
10: 4700978
100: 15273692
2024: 8667524
"""
print(ans == 37327623)
