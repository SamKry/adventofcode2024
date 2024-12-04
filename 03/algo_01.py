import re

dafaFile = "03/data.txt"
dafaFile = "03/data_small01.txt"

# data example:
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

pattern = r"mul\(\d{1,3},\d{1,3}\)"


def getMulAns(seq):
    numbers = list(map(int, re.findall(r"\d{1,3}", seq)))
    return numbers[0] * numbers[1]

ans = 0



# read line by line
with open(dafaFile) as f:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", f.read())
    for match in matches:
        ans += getMulAns(match)





print("Answer: ", ans)
