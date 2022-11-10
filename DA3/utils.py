"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 3
Date: 10/10/2022
Description: Program uses Pandas to work with csv files
"""

import pandas as pd 
import math

def load_into_dataframe(file_name):
    func_df = pd.read_csv(file_name, index_col=0)
    return func_df

def determine_user_col():
    print('List of columns:\n')
    print(' Views\n','Average percentage viewed (%)\n', 
        'Unique viewers\n', 'Subscribers\n', 'Watch time (hours)\n',
        'Average view duration\n', 'Shares\n', 'Likes\n', 'Dislikes\n'
        , 'Comments added\n', 'Impressions\n', 'Impressions click-through rate (%)\n')
    user_col = input('Please enter your desired column: ')
    return user_col

def slice_youtube(start_date, end_date, youtube_df):
    sliced_df = youtube_df.loc[start_date:end_date]
    return sliced_df

def math_function(youtube_sliced_df, user_col):
    math_col =  youtube_sliced_df.loc[:,user_col]
    sum_of_col = math_col.sum()
    mean_of_col = math_col.mean()
    std_dev_of_col = math_col.std()
    median_of_col = math_col.median()
    min_of_col = min(math_col)
    max_of_col = max(math_col)
    return sum_of_col, mean_of_col, std_dev_of_col, median_of_col, min_of_col, max_of_col

def split_combine_apply(merged_df, user_col):
    grouped_by_day = merged_df.groupby('Day of Week')
    mean_merged_series = grouped_by_day[user_col].mean()
    return mean_merged_series