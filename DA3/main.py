"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 3
Date: 10/10/2022
Description: Program uses Pandas to work with csv files
"""
import pandas as pd 
import math
import utils

def main():
    # Exercise 1
    youtube_df = utils.load_into_dataframe('youtube_analytics_9-29-21_9-28-22.csv')
    days_df = utils.load_into_dataframe('days_of_week_9-29-21_9-28-22.csv')

    # Exercise 2
    start_date = input('Enter a start date(inclusive): ')
    end_date = input('Enter a end date(inclusive): ')
    youtube_sliced_df =  utils.slice_youtube(start_date, end_date, youtube_df)
    user_col = utils.determine_user_col()
    sliced_series = pd.Series(dtype=int)
    sliced_series = youtube_sliced_df.loc[:,user_col]

    # Exercise 3
    math_list = []
    math_headers = ['Sum', 'Mean', 'Std_Dev', 'Median', 'Min', 'Max']
    math_list = utils.math_function(youtube_sliced_df, user_col)
    math_series = pd.Series(math_list, index= math_headers)
    math_series.to_csv('math.csv', header = False)

    # Exercise 4
    merged_df = youtube_df.merge(days_df, on = 'Date')
    merged_df.to_csv('merged.csv')

    # Exercise 5
    mean_merged_series = utils.split_combine_apply(merged_df, user_col)
    mean_merged_series.to_csv('split_combine_apply.csv', header = False)


if __name__ == '__main__':
    main()