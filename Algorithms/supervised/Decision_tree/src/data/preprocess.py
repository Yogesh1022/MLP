import pandas as pd
import numpy as np

def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Replace missing markers and drop rows with missing values."""
    df_cleaned = df.replace("?", np.nan)
    return df_cleaned.dropna().reset_index(drop=True)

def strip_spaces(df: pd.DataFrame) -> pd.DataFrame:
    """Strip leading and trailing spaces from object columns."""
    out = df.copy()
    for col in out.select_dtypes(include=["object"]).columns:
        out[col] = out[col].astype(str).str.strip()
    return out

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Run preprocessing steps in a consistent order."""
    df = clean_missing_values(df)
    df = strip_spaces(df)
    return df
