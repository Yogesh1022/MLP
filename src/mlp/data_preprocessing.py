"""
Data Preprocessing Module
=========================

This module contains utilities for cleaning and preprocessing flight pricing data.
"""

import pandas as pd
import numpy as np
from typing import Optional, Union, List


class DataCleaner:
    """Clean and validate flight pricing data."""
    
    def __init__(self):
        """Initialize DataCleaner."""
        self.cleaning_log = []
    
    def clean_additional_info(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize Additional_Info column by replacing variants of 'No info'.
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input dataframe with Additional_Info column
            
        Returns:
        --------
        pd.DataFrame
            Cleaned dataframe
        """
        df = df.copy()
        df['Additional_Info'] = df['Additional_Info'].replace(
            [' NO info', 'No Info', ' No info'], 'No info'
        )
        self.cleaning_log.append("Standardized Additional_Info values")
        return df
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: str = 'drop') -> pd.DataFrame:
        """
        Handle missing values in the dataset.
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input dataframe
        strategy : str
            Strategy to handle missing values ('drop', 'fill_mean', 'fill_median')
            
        Returns:
        --------
        pd.DataFrame
            Dataframe with handled missing values
        """
        df = df.copy()
        
        if strategy == 'drop':
            df = df.dropna()
            self.cleaning_log.append(f"Dropped rows with missing values")
        elif strategy == 'fill_mean':
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
            self.cleaning_log.append(f"Filled missing values with mean")
        elif strategy == 'fill_median':
            numeric_cols = df.select_dtypes(include=[np.number]).columns
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
            self.cleaning_log.append(f"Filled missing values with median")
            
        return df
    
    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicate rows from the dataset.
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input dataframe
            
        Returns:
        --------
        pd.DataFrame
            Dataframe without duplicates
        """
        df = df.copy()
        initial_rows = len(df)
        df = df.drop_duplicates()
        removed_rows = initial_rows - len(df)
        self.cleaning_log.append(f"Removed {removed_rows} duplicate rows")
        return df


class FeatureEngineer:
    """Engineer features from raw flight pricing data."""
    
    def __init__(self):
        """Initialize FeatureEngineer."""
        pass
    
    def create_weekend_flag(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Create a binary flag for weekend flights.
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input dataframe with WeekDay column
            
        Returns:
        --------
        pd.DataFrame
            Dataframe with is_weekend column
        """
        df = df.copy()
        weekend_days = ['saturday', 'sunday']
        df['is_weekend'] = df['WeekDay'].str.lower().isin(weekend_days).astype(int)
        return df
    
    def extract_time_features(self, df: pd.DataFrame, datetime_col: str) -> pd.DataFrame:
        """
        Extract time-based features from datetime column.
        
        Parameters:
        -----------
        df : pd.DataFrame
            Input dataframe
        datetime_col : str
            Name of the datetime column
            
        Returns:
        --------
        pd.DataFrame
            Dataframe with extracted time features
        """
        df = df.copy()
        df[datetime_col] = pd.to_datetime(df[datetime_col])
        df['hour'] = df[datetime_col].dt.hour
        df['day_of_week'] = df[datetime_col].dt.dayofweek
        df['is_weekend_time'] = (df['day_of_week'] >= 5).astype(int)
        return df


def load_data(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Load dataset from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
    **kwargs
        Additional arguments to pass to pd.read_csv
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    return pd.read_csv(filepath, **kwargs)


def get_data_summary(df: pd.DataFrame) -> dict:
    """
    Get comprehensive summary of the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    dict
        Dictionary containing dataset summary statistics
    """
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_summary': df.describe().to_dict() if len(df.select_dtypes(include=[np.number]).columns) > 0 else {},
        'duplicates': df.duplicated().sum()
    }
    return summary
