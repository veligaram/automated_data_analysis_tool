import pandas as pd

def clean_data(df):
    df = df.dropna()  # Drop missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df
