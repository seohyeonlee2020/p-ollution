import pandas as pd
import os
import numpy as np
from sklearn.preprocessing import MinMaxScaler

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


def cleanData(df):
    all_floats = df.map(lambda x: isinstance(x, float)).all().all()
   # non_float_indices = df.map(lambda x: not isinstance(x, float)).any(axis=1)
    non_numeric_columns = df.select_dtypes(exclude='number').columns
   # print(non_numeric_columns)
    #print(df.isna().any().any())
   # print()
   # print(df[non_numeric_columns])
    count_dash = (df == '-').sum().sum()
   # print(count_dash)
    if count_dash > 0:
        #replace missing value ('-') with previous value
        #only one '-' in entire dataset so far
        idxs = list(np.where(df == "-"))
        print(idxs)
        df.iloc[idxs[0][0], idxs[1][0]]
        prev_idx = df.iloc[idxs[0][0], idxs[1][0]-1]
        df.iat[idxs[0][0], idxs[1][0]] = prev_idx
    df = df.apply(lambda x: x.str.replace('*', '') if x.dtype == 'O' else x)
    # e: 추정치, p: 잠정치, -: 자료없음, ...: 미상자료, x: 비밀보호, ▽: 시계열 불연속
    # If you want to convert the columns to numeric after removing asterisks
    cleaned_df = df.apply(pd.to_numeric, errors='ignore')
    return cleaned_df

def scaleData(df, idx):
    scaler = MinMaxScaler()
    df_scaled = scaler.fit_transform(df.to_numpy())
    df_scaled = pd.DataFrame(df_scaled, columns=df.columns)
    #add index back
    df_scaled = df_scaled.set_index(idx, drop = True)
    return df_scaled

def avgOfColumns(df):
    return df.mean()





