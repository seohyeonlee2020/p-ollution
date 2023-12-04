import pandas as pd
import geopandas as gpd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import folium
from folium import Choropleth

def loadDataFromDirectory(directory):
    #open everything in given directory
    directory = directory

    #loop through data folder and open each file as csv.
    df_list = []
    title_list = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # checking if it is a file
        if os.path.isfile(f):
            print(filename)
            title = filename
            print(title)
            title_list.append(title)
            if filename.split('.')[1] == "csv":
                df = pd.read_csv(f) 
                #print(df.head())  
            elif filename.split('.')[1] == "xlsx":
                df = pd.read_excel(f)
                #print(df.head())  
            #append df to df list regardless of f type
            df.rename( columns={'Unnamed: 0' :'year_month'}, inplace=True)
            year_month = df['year_month']
            df = df.drop(['year_month'], axis = 1)
        # set first column as index
            #df = df.set_index(year_month, drop = True)
            print(df.head())
            df_list.append(df)
            #print(title[:4])
    return df_list, title_list

def scaleData(df, idx):
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df.to_numpy())
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
    #add index back
    df_scaled = df_scaled.set_index(idx, drop = True)
    return df_scaled

def avgOfColumns(df):
    return df.mean()





