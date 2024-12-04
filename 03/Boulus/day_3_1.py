import numpy as np
import pandas as pd
import sys
import os
import re

# Data Location
data_folder_path = r'C:\Code\Personal\adventofcode2024\03\Boulus'
file_1 = 'example.txt'
file_2 = 'data.txt'
pattern_1 = re.compile("(mul\([0-9]{1,3}\,[0-9]{1,3}\))")
pattern_2 = re.compile("mul\(([0-9]{1,3})\,([0-9]{1,3})\)")
array_g1 = np.array([]);
array_g2 = np.array([]);

data = os.path.join(data_folder_path, file_2)
for i, line in enumerate(open(data)):
    for match in re.finditer(pattern_2, line):
        print('Found on line %s: %s' % (i+1, match.group()))
        #print(match.group(1), match.group(2))
        array_g1 = np.append(array_g1, int(match.group(1)))
        array_g2 = np.append(array_g2, int(match.group(2)))

print(array_g2)
print(array_g2)
result_multiply = np.multiply(array_g1, array_g2)
result_dot = np.dot(array_g1, array_g2)
#result_add = np.add(result_multiply)
print(result_dot)
