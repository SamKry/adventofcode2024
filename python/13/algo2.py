
# this aproach is copyed from https://github.com/Grecil/ElegantAoC24


dafaFile = "python/13/data.txt"
# dafaFile = "python/13/data_small.txt"
import sys
    
with open(dafaFile, 'r') as file:
    arr = [i.split("\n") for i in file.read().split("\n\n")]

ans = 0
for a, b, c in arr:
    a1, a2 = map(int, a[12:].split(", Y+"))
    b1, b2 = map(int, b[12:].split(", Y+"))
    c1, c2 = [int(i) + 10000000000000 for i in c[9:].split(", Y=")]
    denom = a2 * b1 - a1 * b2
    x = (b1 * c2 - b2 * c1) // denom
    y = (c1 * a2 - c2 * a1) // denom
    if x >= 0 and y >= 0 and x * a1 + y * b1 == c1 and x * a2 + y * b2 == c2:
        ans += 3 * x + y
print(ans)
