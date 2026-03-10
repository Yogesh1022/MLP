"""
Utility Functions
=================

Helper functions for the ML pipeline project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Tuple, Optional
import json
from pathlib import Path


def save_model(model, filepath: str):
    """
    Save a trained model to disk.
    
    Parameters:
    -----------
    model : object
        Trained model object
    filepath : str
        Path where to save the model
    """
    import joblib
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")


def load_model(filepath: str):
    """
    Load a trained model from disk.
    
    Parameters:
    -----------
    filepath : str
        Path to the saved model
        
    Returns:
    --------
    object
        Loaded model
    """
    import joblib
    model = joblib.load(filepath)
    print(f"Model loaded from {filepath}")
    return model


def calculate_price_statistics(df: pd.DataFrame, price_col: str = 'Price') -> Dict:
    """
    Calculate comprehensive price statistics.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe with price column
    price_col : str
        Name of the price column
        
    Returns:
    --------
    Dict
        Dictionary with price statistics
    """
    stats = {
        'mean': df[price_col].mean(),
        'median': df[price_col].median(),
        'std': df[price_col].std(),
        'min': df[price_col].min(),
        'max': df[price_col].max(),
        'q25': df[price_col].quantile(0.25),
        'q75': df[price_col].quantile(0.75),
        'count': len(df[price_col])
    }
    return stats


def analyze_price_by_weekday(df: pd.DataFrame, weekday_col: str = 'WeekDay', 
                             price_col: str = 'Price') -> pd.DataFrame:
    """
    Analyze average prices by weekday.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    weekday_col : str
        Name of the weekday column
    price_col : str
        Name of the price column
        
    Returns:
    --------
    pd.DataFrame
        Summary of prices by weekday
    """
    return df.groupby(weekday_col)[price_col].agg(['mean', 'median', 'count']).round(2)


def compare_weekend_weekday_prices(df: pd.DataFrame, weekday_col: str = 'WeekDay',
                                   price_col: str = 'Price') -> Dict:
    """
    Compare average prices between weekends and weekdays.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    weekday_col : str
        Name of the weekday column
    price_col : str
        Name of the price column
        
    Returns:
    --------
    Dict
        Dictionary with weekend and weekday price comparisons
    """
    weekend_days = ['saturday', 'sunday']
    weekend_prices = df[df[weekday_col].str.lower().isin(weekend_days)][price_col]
    weekday_prices = df[~df[weekday_col].str.lower().isin(weekend_days)][price_col]
    
    return {
        'weekend_mean': round(weekend_prices.mean(), 2),
        'weekday_mean': round(weekday_prices.mean(), 2),
        'difference': round(weekend_prices.mean() - weekday_prices.mean(), 2),
        'weekend_count': len(weekend_prices),
        'weekday_count': len(weekday_prices)
    }


def plot_price_distribution(df: pd.DataFrame, price_col: str = 'Price', 
                           figsize: Tuple[int, int] = (10, 6)):
    """
    Plot the distribution of prices.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    price_col : str
        Name of the price column
    figsize : Tuple[int, int]
        Figure size (width, height)
    """
    fig, axes = plt.subplots(1, 2, figsize=figsize)
    
    # Histogram
    axes[0].hist(df[price_col], bins=50, edgecolor='black')
    axes[0].set_xlabel('Price')
    axes[0].set_ylabel('Frequency')
    axes[0].set_title('Price Distribution')
    
    # Box plot
    axes[1].boxplot(df[price_col])
    axes[1].set_ylabel('Price')
    axes[1].set_title('Price Box Plot')
    
    plt.tight_layout()
    plt.show()


def plot_correlation_matrix(df: pd.DataFrame, figsize: Tuple[int, int] = (12, 8)):
    """
    Plot correlation matrix for numeric features.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    figsize : Tuple[int, int]
        Figure size (width, height)
    """
    numeric_df = df.select_dtypes(include=[np.number])
    
    plt.figure(figsize=figsize)
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', center=0,
                fmt='.2f', square=True, linewidths=1)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()


def save_config(config: Dict, filepath: str):
    """
    Save configuration to JSON file.
    
    Parameters:
    -----------
    config : Dict
        Configuration dictionary
    filepath : str
        Path to save the configuration
    """
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)
    print(f"Configuration saved to {filepath}")


def load_config(filepath: str) -> Dict:
    """
    Load configuration from JSON file.
    
    Parameters:
    -----------
    filepath : str
        Path to the configuration file
        
    Returns:
    --------
    Dict
        Configuration dictionary
    """
    with open(filepath, 'r') as f:
        config = json.load(f)
    print(f"Configuration loaded from {filepath}")
    return config


def create_directory_structure(base_path: str):
    """
    Create standard directory structure for ML project.
    
    Parameters:
    -----------
    base_path : str
        Base path for the project
    """
    directories = [
        'data/raw',
        'data/processed',
        'notebooks',
        'src',
        'tests',
        'models',
        'docs',
        'config'
    ]
    
    for directory in directories:
        (Path(base_path) / directory).mkdir(parents=True, exist_ok=True)
    
    print(f"Directory structure created at {base_path}")


def get_month_name(month_num: int) -> str:
    """
    Convert month number to month name.
    
    Parameters:
    -----------
    month_num : int
        Month number (1-12)
        
    Returns:
    --------
    str
        Month name
    """
    months = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }
    return months.get(month_num, 'Unknown')
