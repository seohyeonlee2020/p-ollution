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

def loadKoreanMap():
    korea_provinces = gpd.read_file('/Users/seohyeonlee/p-ollution/data/korea_provinces.json')
    province_fullname = korea_provinces['name_eng']
    #print(province_fullname)
    province_short = ['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Sejong', 'Gyeonggi', 'Gangwon', 'Choongbuk', 'Choongnam', 'Jeonbuk', 'Jeonnam', 'Gyeongbuk', 'Gyeongnam', 'Jeju' ]
    province_name_conversion = dict(zip(province_fullname, province_short))
    
    #id for base and choropleth map
    korea_provinces['province'] = pd.Series(province_short)
    korea_province_map = korea_provinces[["province", "geometry"]].set_index("province")
    print(korea_province_map.index)

    return korea_province_map

def add_choropleth_to_basemap(base_map, pollutant_data, pollutant_name, your_map):
    # 망원시장 37.5560° N, 126.9064° E
    #print(data_dict[pollutant])
    Choropleth(geo_data=your_map.__geo_interface__, 
            data=pollutant_data, 
            key_on="feature.id", 
            fill_color='YlGnBu', 
            legend_name=pollutant_name,
            ).add_to(base_map)
    base_map
    return base_map





