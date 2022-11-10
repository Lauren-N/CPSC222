"""
Name: Lauren Nguyen
Course: CPSC 222
Assignment: Data Assignment 5
Date: 11/8/2022
Description: Program uses JupyterNB to play with data and matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

# loading the patient information into a dataframe and returning it
def load_into_df(file_name):
    func_df = pd.read_csv(file_name, index_col=0)
    return func_df

# cleaning our data
def clean_data(df):
    cleaned_df = df.copy() #creating a new df that holds the same data as the df passed in
    for value in cleaned_df.loc[:,"Marital Status"]: #iterates through each value in the marital status column
        if "arrie" in value or "ARRIE" in value: #checking for married in a upper and lower fashion
            cleaned_df.replace(value, "Married", inplace=True) #replacing values into a uniform fashion
        elif "ingl" in value or "INGL" in value: #checking for single in a upper and lower fashion
            cleaned_df.replace(value, "Never Married", inplace=True) #replacing values into a uniform fashion
        elif "idow" in value or "IDOW" in value: #checking for widowed in a upper and lower fashion
            cleaned_df.replace(value, "Widowed", inplace=True) #replacing values into a uniform fashion
        elif "ivorc" in value or "IVORC" in value: #checking for divorced in a upper and lower fashion
            cleaned_df.replace(value, "Divorced", inplace=True) #replacing values into a uniform fashion
        elif "eparat" in value or "EPARAT" in value: #checking for seperated in a upper and lower fashion
            cleaned_df.replace(value, "Separated", inplace=True) #replacing values into a uniform fashion
        else: # else that makes indistinguishable data null
            cleaned_df.replace(value, np.nan, inplace=True)

    ric_decoder = {1: "Stroke", 2: "TBI", 3: "NTBI", 4: "TSCI", 5: "NTSCI"
                    , 6: "Neuro", 7: "FracLE", 8: "ReplLE", 9: "Ortho", 10: "AMPLE"
                    ,11: "AMP-NLE", 12: "OsteoA", 13: "RheumA", 14: "Cardiac", 
                    15: "Pulmonary", 16: "Pain", 17: "MMT-NBSCI", 18: "MMT-BSCI", 19: "GB"
                    ,20: "Misc", 21: "Burns"}
    for key in ric_decoder: # for the corresponding number in the ric decoder, this finds the number in cleaned_df and replaces it with the ric name
        cleaned_df.replace(key, ric_decoder[key], inplace=True)

    return cleaned_df #returning cleaned_df

# computing stats
def aggregate_data(df):
    statistics_list = [] #list to return to put into a series

    patients_total = len(df) # finding amount of patients
    statistics_list.append(patients_total) #appending to end of list

    males_total = df["Gender"].value_counts()["M"] #finding amount of males
    statistics_list.append(males_total)

    females_total = df["Gender"].value_counts()["F"] #finding amount of females
    statistics_list.append(females_total)

    married_total = df["Marital Status"].value_counts()["Married"] #finding amount of married patients
    statistics_list.append(married_total)

    most_common_RIC = df["RIC"].mode().iloc[0] # finding most common ric
    statistics_list.append(most_common_RIC)

    most_common_RIC_total = df["RIC"].value_counts()[most_common_RIC] #finding amount of the most common ric
    statistics_list.append(most_common_RIC_total)

    stroke_df = df.loc[df["RIC"] == "Stroke"] #creating new df with just stroke patients
    cleaned_stroke_df = stroke_df.copy() #making copy of stroke_df
    for item in stroke_df.loc[:,"Age"]: #iterating thgough each input and replacing string values with null
        if type(item) == str:
            cleaned_stroke_df.replace(item, np.nan, inplace=True)
    stroke_age_avg = cleaned_stroke_df["Age"].mean() #finding mean of the age in the stroke patients
    statistics_list.append(stroke_age_avg)

    stroke_age_std = np.std(cleaned_stroke_df["Age"]) #finding stdev of the age in the stroke patients
    statistics_list.append(stroke_age_std)

    gender_stroke_M_df = cleaned_stroke_df.loc[cleaned_stroke_df["Gender"]=="M"] # slicing new df to just stroke male patients
    stroke_age_male_avg = gender_stroke_M_df["Age"].mean() #finding mean of the age in the male stroke patients
    statistics_list.append(stroke_age_male_avg)

    stroke_age_male_std = gender_stroke_M_df["Age"].std() #finding stdev of the stdev in the stroke patients
    statistics_list.append(stroke_age_male_std)

    gender_stroke_F_df = cleaned_stroke_df.loc[cleaned_stroke_df["Gender"]=="F"] # slicing new df to just stroke female patients
    stroke_age_female_avg = gender_stroke_F_df["Age"].mean()#finding mean of the age in the female stroke patients
    statistics_list.append(stroke_age_female_avg)

    stroke_age_female_std = np.std(gender_stroke_F_df["Age"]) #finding stdev of the age in the male stroke patients
    statistics_list.append(stroke_age_female_std)

    return statistics_list

#creating histograms
def visualized_hist_data(df, ric_name):
    graph_df = df.copy() #making copy of df passed in
    for item in df.loc[:,"Age"]: #iterating thgough each input and replacing string values with null
        if type(item) == str:
            graph_df.replace(item, np.nan, inplace=True)
    
    # FOR GRAPH TITLE
    ric_count = graph_df["RIC"].value_counts()[ric_name]  #getting count of patients
    str_ric_count = str(ric_count) #turning number into to string to concatenate title together later

    ric_df = graph_df.loc[df["RIC"] == ric_name] # new df to slice the graph_loc to just the specified ric col
    ric_mean = ric_df["Age"].mean() #getting mean of the specified ric
    str_ric_mean = str(round(ric_mean, 2)) #turning number into to string to concatenate title together later

    ric_stdev = ric_df["Age"].std() #getting stdev of the specified ric
    str_ric_stdev = str(round(ric_stdev, 2)) #turning number into to string to concatenate title together later

    plt.figure()
    plt.hist(graph_df["Age"], bins=30) # graphing the histogram with bins set to 30 and sending in graph_df Age column
    title_name = ric_name + " Age(N=" + str_ric_count + "), Mean:" + str_ric_mean + ", StdDev:" + str_ric_stdev #creating title
    plt.title(title_name)
    plt.xlabel("Age(years)") #setting x label
    plt.ylabel("Frequency") #setting y label
    plt.show()

def visualized_scatter_data(df, ric_name):
    f_df = df.loc[df["Gender"] == "F"] #splicing to just female patients
    m_df = df.loc[df["Gender"] == "M"] #splicing to just male patients

    ric_count = df["RIC"].value_counts()[ric_name] #finding count of all patients for the title
    str_ric_count = str(round(ric_count, 2))  #turning number into to string to concatenate title together later

    f_admit_df = check_for_str(f_df, "Admission Total FIM Score") #a new dataframe to truncate through the female admit scores and checking for invalid data
    f_discharge_df = check_for_str(f_df,"Discharge Total FIM Score")  #a new dataframe to truncate through the female discharge scores and checking for invalid data
    f_a_plot_df = f_admit_df.loc[f_admit_df["RIC"] == ric_name] #new female admit dataframe to use for actual plotting, spliced from checked df above
    f_d_plot_df = f_discharge_df.loc[f_discharge_df["RIC"] == ric_name] #new female discharge dataframe to use for actual plotting, spliced from checked df above

    m_admit_df = check_for_str(m_df, "Admission Total FIM Score") #a new dataframe to truncate through the male admit scores and checking for invalid data
    m_discharge_df = check_for_str(m_df,"Discharge Total FIM Score") #a new dataframe to truncate through the male discharge scores and checking for invalid data
    m_a_plot_df = m_admit_df.loc[m_admit_df["RIC"] == ric_name] #new male admit dataframe to use for actual plotting, spliced from checked df above
    m_d_plot_df = m_discharge_df.loc[m_discharge_df["RIC"] == ric_name] #new male discharge dataframe to use for actual plotting, spliced from checked df above
    
    #  FOR LEGEND CONSTRUCTION
    count_female = len(f_df) # getting total female lengths
    str_count_female = str(count_female) #turning to str to concat later
    count_male = len(m_df) # getting total male lengths
    str_count_male = str(count_male) #turning to str to concat later
    female_label = 'Female(N=' + str_count_female +")" #concat female label
    male_label = 'Male(N=' + str_count_male +")" #concat male label

    plt.figure()
    #plotting the female data
    plt.scatter(f_a_plot_df.loc[:,"Admission Total FIM Score"], f_d_plot_df.loc[:,"Discharge Total FIM Score"], marker='+', c='red', label=female_label) 
    #plotting the male data
    plt.scatter(m_a_plot_df.loc[:,"Admission Total FIM Score"], m_d_plot_df.loc[:,"Discharge Total FIM Score"], marker='.', c='blue', label=male_label)
    #plotting the no change line
    plt.plot([0,140], [0,140], c='black', linestyle='dashed', label='No Change')
    graph_title = ric_name + " (N=" + str_ric_count + ")" #constructing the title
    plt.xlabel("Admission Total FIM Score") #xlabel
    plt.ylabel("Discharge Total FIM Score") #ylabel
    plt.title(graph_title)
    plt.legend(loc="lower right") #creating legend and setting location
    plt.show()

#iterating thgough each input and replacing string values with null
def check_for_str(df, ric_name):
    copy_df = df.copy()
    for item in df.loc[:,ric_name]:
        if type(item) == str:
            copy_df.replace(item, np.nan, inplace=True) 
    return copy_df
    

