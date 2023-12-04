import os
import pandas as pd
import numpy as np



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
        # print(idxs)
        if len(idxs) > 0:
            for idx in idxs:
                df.iloc[idxs[0][0], idxs[1][0]]
                prev_idx = df.iloc[idxs[0][0], idxs[1][0]-1]
                df.iat[idxs[0][0], idxs[1][0]] = prev_idx
    df = df.apply(lambda x: x.str.replace('*', '') if x.dtype == 'O' else x)
    # e: 추정치, p: 잠정치, -: 자료없음, ...: 미상자료, x: 비밀보호, ▽: 시계열 불연속
    # If you want to convert the columns to numeric after removing asterisks
    df = df.rename({'Chungbuk':'Choongbuk', 'Chungnam':'Choongnam'}, axis = 1)
    cleaned_df = df.apply(pd.to_numeric, errors='ignore')
    print('cleaned!')
    return cleaned_df

def loadFiles(directory):
    #takes directory to open files from
    #returns df_dict dict of file title and df
    df_dict = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        title = filename.split(".")[0]
        # checking if it is a file
        if os.path.isfile(f):
            df = pd.read_csv(f, header=[0], index_col=[0]) 
            df = cleanData(df)
            df_dict[title] = df
            print(f'added {title} to df_dict')
    
    return df_dict
    
print('running support code')
# dct = loadFiles('data/air_data')
# print(dct.keys())


# for title, item in dct.items():
#     df_item = cleanData(dct['no2'])
# #print(no_c.head())
#     print(df_item.select_dtypes(include='O').sum())



