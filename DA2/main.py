# done
"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 2
Date: 09/18/2022
Description: Program uses a utiity file to display data read in from a csv file
"""

import utils
import math
import csv

def main():
    # adding data to lists
    data = list()
    headers = list()
    headers, data = utils.read_data('fitbit_data.csv')
    utils.display_table(headers, data)
    print('---------------------------------------------')
    # Getting user cols and math ops
    user_col_name = input('Enter what column you want!: ')
    new_data = utils.get_column(headers, user_col_name, data)
    print('Here is the data from the column!:\n', new_data)
    # Count of data
    count_data = len(new_data)

    # Average of data
    avg_data = sum(new_data)/len(new_data)

    # Standard deviation of data
    count = 0
    for item in new_data:
        std_sub = avg_data - item
        std_square = math.pow(std_sub,2)
        count += std_square
        std_square = 0
        std_sub = 0
    std_avg = count/count_data
    std_dev = math.pow(std_avg, 1/2)

    # Median of data
    new_data.sort()
    middle = len(new_data) // 2
    median = (new_data[middle] + new_data[~middle]) // 2

    # Smallest data
    small_data = min(new_data)

    # Largest data
    large_data = max(new_data)
    
    # Printing out all math ops
    print('---------------------------------------------')
    print('Count of numbers:', count_data)
    print('Average of numbers:', f"{avg_data:.2f}")
    print('Standard deviation of numbers:', f"{std_dev:.2f}")
    print('Median of numbers:', median)
    print('Smallest number:', small_data)
    print('Largest number:', large_data)



if __name__ == "__main__":
    main()