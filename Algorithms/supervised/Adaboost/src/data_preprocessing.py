import pandas as pd
from pandas.api.types import is_numeric_dtype

def load_data(path):
    """
    Load the dataset from the specified path.
    
    """
    df=pd.read_csv(path)
    return df

def clean_data(df):
    """
    
    Clean the dataset by droping irrelevant columns and handling missing values if any.
    
    """
     # remove duplicates
    df = df.drop_duplicates()

    # drop useless columns
    drop_cols = ["RowNumber", "CustomerId", "Surname"]

    df = df.drop(columns=drop_cols)

    return df

def handling_missing_values(df):
    """
    handle missing values if any.
    """
    for col in df.columns:
        if is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())
            continue

        mode = df[col].mode(dropna=True)
        fill_value = mode.iloc[0] if not mode.empty else "Unknown"
        df[col] = df[col].fillna(fill_value)

    return df