import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array

dataFile = "python/19/data.txt"
# dataFile = "python/19/data_small.txt"

"""
example: 

r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb

"""
towels = []

with open(dataFile) as f:
    d1, d2 = f.read().split("\n\n")
    for x in d1.split(","):
        towels.append(x.strip())
    instructions = d2.split("\n")

instructions.sort()
pprint(towels)
pprint(instructions)

towel_dict = {'r': [], 'g': [], 'u': [], 'w': [], 'b': []}

for towel in towels:
    if towel and towel[0] in towel_dict:
        towel_dict[towel[0]].append(towel)

print(towel_dict)


# returns 1 if it is possible to make the instruction with the towels,  else 0
# there is an unlimited amount of towels
# it is called recursively to check if the instruction is possible
def isPossible(instruction:str):
    possibleStarts = towel_dict[instruction[0]]
    if not possibleStarts:
        return 0
    for start in possibleStarts:
        if instruction.startswith(start):
            if len(start) == len(instruction):
                return 1
            else:
                if isPossible(instruction[len(start):]):
                    return 1
                
    return 0


ans = 0

for instruction in instructions:
    possible = isPossible(instruction)
    if possible:
        ans += 1
        print("Possible: ", instruction)
    else:
        print("Impossible: ", instruction)

print("Answer: ", ans)


"""
//brwrr can be made with a br towel, then a wr towel, and then finally an r towel.
//bggr can be made with a b towel, two g towels, and then an r towel.
//gbbr can be made with a gb towel and then a br towel.
//rrbgbr can be made with r, rb, g, and br.
//ubwu is impossible.
!bwurrg can be made with bwu, r, r, and g.
//brgr can be made with br, g, and r.
//bbrgwb is impossible

my:
Possible:  brwrr
Possible:  bggr
Possible:  gbbr
Possible:  rrbgbr
Impossible:  ubwu
!Impossible:  bwurrg
Possible:  brgr
Impossible:  bbrgwb
"""