import pandas as pd
import os

def get_data(file_path):
    df = pd.read_csv(file_path)
    df.drop('Unnamed: 0',axis= 1, inplace = True)
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year.astype(str)
    df['month'] = df['date'].dt.month.astype(str)
    return df
