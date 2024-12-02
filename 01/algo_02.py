import numpy as np
import pandas as pd

data = "01/dataBoulus.csv"

# data format:
# number1a  number2a
# number1b  number2b
# number1c  number2c


# Split the data into two arrays


# split date into two different arrays [number1a, number1b, ...], [number2a, number2b, ...]
def split_data(data):
    data_table = pd.read_csv(data, sep="   ", header=None)
    a = data_table[0].values
    b = data_table[1].values
    return a, b

a, b = split_data(data)


# Sort the arrays
a = np.sort(a)
b = np.sort(b)

# print(a)

# print(b)

similarity  = 0
for i in range(len(a)):
    number = a[i]
    count = np.count_nonzero(b == number)
    similarity += number * count
    
print(similarity)