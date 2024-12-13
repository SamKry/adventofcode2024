import numpy as np
import pandas as pd

dafaFile = "python/03/data.txt"
# dafaFile = "python/03/data_small.txt"

import re

def parse_memory(memory):
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    control_pattern = re.compile(r'(do|don\'t)\(\)')

    mul_matches = [(m.start(), m.end(), int(m.group(1)), int(m.group(2))) for m in mul_pattern.finditer(memory)]
    control_matches = [(m.start(), m.group(1)) for m in control_pattern.finditer(memory)]

    events = sorted([(pos, "mul", x, y) for pos, _, x, y in mul_matches] +
                    [(pos, "control", ctrl) for pos, ctrl in control_matches])

    enabled = True
    total = 0

    print(events)

    for event in events:
        if event[1] == "control":
            if event[2] == "do":
                enabled = True
            elif event[2] == "don't":
                enabled = False
        elif event[1] == "mul":
            if enabled:
                total += event[2] * event[3]

    return total

with open(dafaFile) as f:
    memory = f.read()
    result = parse_memory(memory)
    print(result)

