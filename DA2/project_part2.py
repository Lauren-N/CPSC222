# done
"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 2
Date: 09/18/2022
Description: Program uses a utiity file to display data read in from a personal csv file
"""
import utils
import csv
import math

data = list()
headers = list()
headers, data = utils.read_data('Wordle.csv')
utils.display_table(headers, data)