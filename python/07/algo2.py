import re
from itertools import product

dafaFile = "07/data.txt"
dafaFile = "07/data_small.txt"


"""
example:
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

# operators: +, *, ||

# || is a concatenation operator

ans = 0

def buildPossibleOperators(length):
    # return a list of all possible operators of length length
    # e.g. length = 2 -> return [["+", "*"], ["*", "+"], ["+", "+"], ["*", "*"]]

    operators = ["+", "*", "||"]
    possibleOperators = []
    possibleOperators = list(product(["+", "*", "||"], repeat=length))
    return [list(op) for op in possibleOperators]

def checkLine(sol, numbers):
    possibleOperators = buildPossibleOperators(len(numbers) - 1)
    # solve it from left to right
    for op in possibleOperators:
        temp = numbers[0]
        for i in range(len(numbers) - 1):
            if op[i] == "+":
                temp += numbers[i + 1]
            elif op[i] == "*":
                temp *= numbers[i + 1]
            elif op[i] == "||":
                temp = int(str(temp) + str(numbers[i + 1]))
        if temp == sol:
            return True
    return False
    
    

with open(dafaFile) as f1:
    dataf = f1.readlines()
    # convert to solution and numbers []
    for line in dataf:
        print(line)
        numbers = list(map(int, re.findall(r"\d+", line)))
        sol = numbers.pop(0)
        if checkLine(sol, numbers):
            ans += sol


print("Answer: ", ans)
