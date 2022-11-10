import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 4
Date: 10/26/2022
Description: Program uses APIs to get information from two different APIs
I ATTEMPTED THE BONUS
"""

def get_user_input():
    user_city = input('Please Enter a Large City: ')
    for letter in user_city:
        if letter == ' ':
            fixed_city = user_city.replace(' ', '+')
            return fixed_city
            break
    return user_city

def fix_city(user_city):
    for letter in user_city:
        if letter == '+':
            fixed_city = user_city.replace('+', '_')
            return fixed_city
            break
    return user_city

def lattitude_longitude(api_key, url, user_city):
    url += '?key=' + api_key
    url += '&location=' + user_city
    response = requests.get(url= url)
    json_obj = json.loads(response.text)
    results_obj = json_obj['results']
    for data_obj in results_obj:
        data_obj = data_obj['locations']
        for location_obj in data_obj:
            lat_lng_obj = location_obj['latLng']
            lat = lat_lng_obj['lat']
            lng = lat_lng_obj['lng']
    return lat, lng

def get_weather_station_ID(headers, url, lat, lng, limit):
    url += '?lat=' + lat
    url += '&lon=' + lng
    url += '&limit=' + limit
    response = requests.get(url=url, headers=headers)
    json_obj = json.loads(response.text)
    data_obj = json_obj['data']
    for id_obj in data_obj:
        station_ID = id_obj['id']
        break
    return station_ID

def get_daily_data(headers, url, start, end, station_ID):
    url += '?station=' + station_ID
    url += '&start=' + start
    url += '&end=' + end
    url += '&units=imperial'
    response = requests.get(url=url, headers=headers, )
    list_for_df = []
    json_obj = json.loads(response.text)
    for meta_obj in json_obj:
        meta_obj = json_obj['data']
        for data_obj in meta_obj:
            list_for_df.append(data_obj)
    df = pd.DataFrame(list_for_df)
    # df = df.set_index('date')
    return df

def delete_missing_data(df):
    for i in range(len(df.index)):
        df.dropna(thresh= half_of_data, inplace=True, axis=1)
    df.reset_index(inplace=True, drop=True)
    return df

def fill_missing_values(df):
    clean_df = df.interpolate(method='linear')
    clean_df = df.fillna(method='bfill')
    clean_df = df.fillna(method='ffill')
    return clean_df

def get_user_attributes():
    print()
    print('tavg','tmin','tmax','prcp','wdir','wspd','pres')
    user_attribute = input('Please enter attribute: ')
    return user_attribute

def plot_chart(df,filename, user_attribute, city_name):
    x = df['date']
    y = df[user_attribute]
    graph_title =city_name + ' Daily ' + user_attribute + ' Data'
    plt.bar(x,y)
    plt.xlabel('Months')
    plt.ylabel(user_attribute)
    plt.title(graph_title)
    plt.tight_layout()
    # labels = ['high', 'low', 730]
    # plt.xticks(x, labels, rotation='vertical')
    plt.savefig(filename)