import numpy as np
import pandas as pd
import sys
import os

# Data Location
data_folder_path = r'C:\Code\Personal\adventofcode2024\02\Boulus'

# Data files
data_file_test = 'data_file_1_test.txt'
data_file = 'data_file_1.txt'

# Load data
def load_data_table_from_txt(data):
    data_table = pd.read_csv(data, sep=' ', header=None, names=range(10))
    return data_table

# Check if array is safe
def is_safe(array):
    #list_full = array.tolist()
    list = array[np.logical_not(np.isnan(array))]
    print(list)
    return all((val<0 and 1<=abs(val)<=3) for val in list) or all((val>0 and 1<=abs(val)<=3) for val in list)

def main():
    #print(sys.path)
    data = os.path.join(data_folder_path, data_file)
    data_table = load_data_table_from_txt(data)
    data_array = data_table.to_numpy()
    print(data_table.head())
    print(data_array)
    safe_array = [False for i in range(len(data_array))]
    #print(safe_array)

    # loop
    for ii, row in enumerate(data_array):
        row_diff = np.diff(row)
        #print(is_safe(row_diff))
        safe_array[ii] = is_safe(row_diff)

    # Answer
    #print(safe_array)
    print(safe_array.count(True))

if __name__ == "__main__":
    main()