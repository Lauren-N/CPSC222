# done
# Utility file for function use
import csv


# Opens filename for reading and loads the column names into a 1D list called headers and loads the data into a 2D list called data
# Returns headers and data
def read_data(file_name):
    file = open(file_name)
    reader = csv.reader(file)
    headers = []
    headers = next(reader)
    data = list()
    for num in reader:
        data.append(num)
    return headers, data

# Displays the header row and the data in a grid-like table format
def display_table(headers, data):
    for head in headers:
        print(head, end = '  ')
    print()
    for row in data:
        for item in row:
            print(item, end ='\t')
        print()

# Returns a 1D list representing the column named col_name in data
def get_column(headers, col_name, data):
   col_index = find_header_index(headers, col_name)
   new_data = []
   i = 0
   for row in data:
    new_data.append(data[i][col_index])
    i+=1
   int_data = convert_col_to_numeric(new_data)
   return new_data 

# Finds the index of the col name
def find_header_index(headers, col_name):
    i = 0
    while(i < len(headers)):
        if headers[i] == col_name:
            return i
        i+=1

# Converts lists to integers
def convert_col_to_numeric(table):
    i = 0
    for row in table:
        table[i] = int(table[i])
        i+=1