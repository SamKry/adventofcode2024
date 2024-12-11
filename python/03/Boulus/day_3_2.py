import numpy as np
import pandas as pd
import sys
import os
import re

# Data Location
data_folder_path = r'C:\Code\Personal\adventofcode2024\03\Boulus'
file_1 = 'example.txt'
file_2 = 'data.txt'
file_3 = 'example_2.txt'
file_4 = 'data_reduced.txt'
file_5 = 'data_2.txt'
pattern_1 = re.compile("(mul\([0-9]{1,3}\,[0-9]{1,3}\))")
pattern_2 = re.compile("mul\(([0-9]{1,3})\,([0-9]{1,3})\)")
pattern_3 = re.compile("don\'t\(\).{1,10000000}do\(\)") # wrong approach
pattern_4 = re.compile("don\'t\(\).{1,}?do\(\)") 
pattern_dont = re.compile("don\'t\(\)")
pattern_do = re.compile("do\(\)")
array_g1 = np.array([]);
array_g2 = np.array([]);

data = os.path.join(data_folder_path, file_5)
with open(data, 'r') as file:
    file_text = file.read()
file_text_no_newlines = file_text.strip()

line_reduced = pattern_4.sub('', file_text_no_newlines)
print(line_reduced)
for match in re.finditer(pattern_2, line_reduced):
    #print(match.group())
    #print(match.group(1), match.group(2))
    array_g1 = np.append(array_g1, int(match.group(1)))
    array_g2 = np.append(array_g2, int(match.group(2)))

#print(array_g1)
#print(array_g2)
result_multiply = np.multiply(array_g1, array_g2)
result_dot = np.dot(array_g1, array_g2)
#result_add = np.add(result_multiply)
print(int(result_dot))
