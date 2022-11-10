import json
import requests
import utils
import pandas as pd
"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 4
Date: 10/26/2022
Description: Program uses APIs to get information from two different APIs
I ATTEMPTED THE BONUS
"""
api_key = '98oaqAOsvDBo8OBVTgGwbgsWb8oMoAGb'
map_url = 'http://www.mapquestapi.com/geocoding/v1/address'

station_met_url = 'https://meteostat.p.rapidapi.com/stations/nearby'
daily_met_url = 'https://meteostat.p.rapidapi.com/stations/daily'
headers = {'X-RapidAPI-Key': '442e566fdbmsh4fe2ad6e455fcbcp1a5fe9jsn28b4022e2c0d'}

def main():
    # Task 1
    user_city = utils.get_user_input()
    underscore_city = utils.fix_city(user_city)

    # Task 2
    lat, lng = utils.lattitude_longitude(api_key, map_url, user_city)
    str_lat = str(lat)
    str_lng = str(lng)

    # Task 3
    limit = '100'
    station_id = utils.get_weather_station_ID(headers, station_met_url, str_lat, str_lng, limit)
    str_station_id = str(station_id)

    # Task 4
    start = '2021-02-21'
    end = '2022-02-20'
    df = utils.get_daily_data(headers, daily_met_url, start, end, str_station_id)

    # Task 5
    uncleaned_csv_file_name = underscore_city + '_daily_weather.csv'
    df.to_csv(uncleaned_csv_file_name)

    # Task 6
    delete_df = utils.delete_missing_data(df)
    cleaned_df = utils.fill_missing_values(delete_df)

    # Task 7
    cleaned_csv_file_name = underscore_city + '_daily_weather_cleaned.csv'
    cleaned_df.to_csv(cleaned_csv_file_name)

    # BONUS
    user_attribute = utils.get_user_attributes()
    filename = underscore_city + '_daily_' + user_attribute +'.png'
    utils.plot_chart(cleaned_df, filename, user_attribute, user_city)

if __name__ == '__main__':
    main()