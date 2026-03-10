"""
Pipeline Module
===============

This module contains scikit-learn pipeline definitions for flight price prediction.
"""

import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from typing import List, Optional


class FlightPricePipeline:
    """Scikit-learn pipeline for flight price prediction."""
    
    def __init__(self, numeric_features: List[str], categorical_features: List[str]):
        """
        Initialize the pipeline.
        
        Parameters:
        -----------
        numeric_features : List[str]
            List of numeric feature column names
        categorical_features : List[str]
            List of categorical feature column names
        """
        self.numeric_features = numeric_features
        self.categorical_features = categorical_features
        self.pipeline = None
        self._build_pipeline()
    
    def _build_pipeline(self):
        """Build the preprocessing pipeline."""
        # Numeric transformer
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ])
        
        # Categorical transformer
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])
        
        # Combine transformers
        self.pipeline = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, self.numeric_features),
                ('cat', categorical_transformer, self.categorical_features)
            ],
            remainder='drop'
        )
    
    def fit(self, X: pd.DataFrame, y: Optional[pd.Series] = None):
        """
        Fit the pipeline.
        
        Parameters:
        -----------
        X : pd.DataFrame
            Input features
        y : pd.Series, optional
            Target variable
            
        Returns:
        --------
        self
        """
        self.pipeline.fit(X, y)
        return self
    
    def transform(self, X: pd.DataFrame) -> np.ndarray:
        """
        Transform the data.
        
        Parameters:
        -----------
        X : pd.DataFrame
            Input features
            
        Returns:
        --------
        np.ndarray
            Transformed features
        """
        return self.pipeline.transform(X)
    
    def fit_transform(self, X: pd.DataFrame, y: Optional[pd.Series] = None) -> np.ndarray:
        """
        Fit and transform the data.
        
        Parameters:
        -----------
        X : pd.DataFrame
            Input features
        y : pd.Series, optional
            Target variable
            
        Returns:
        --------
        np.ndarray
            Transformed features
        """
        return self.pipeline.fit_transform(X, y)
    
    def get_feature_names_out(self) -> List[str]:
        """
        Get output feature names.
        
        Returns:
        --------
        List[str]
            List of feature names after transformation
        """
        return self.pipeline.get_feature_names_out().tolist()


def create_preprocessing_pipeline(
    numeric_features: Optional[List[str]] = None,
    categorical_features: Optional[List[str]] = None,
    numeric_strategy: str = 'median',
    categorical_strategy: str = 'constant'
) -> ColumnTransformer:
    """
    Create a flexible preprocessing pipeline.
    
    Parameters:
    -----------
    numeric_features : List[str], optional
        List of numeric feature names
    categorical_features : List[str], optional
        List of categorical feature names
    numeric_strategy : str
        Imputation strategy for numeric features ('mean', 'median', 'most_frequent')
    categorical_strategy : str
        Imputation strategy for categorical features ('constant', 'most_frequent')
        
    Returns:
    --------
    ColumnTransformer
        Configured preprocessing pipeline
    """
    transformers = []
    
    if numeric_features:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy=numeric_strategy)),
            ('scaler', StandardScaler())
        ])
        transformers.append(('num', numeric_transformer, numeric_features))
    
    if categorical_features:
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy=categorical_strategy, fill_value='missing')),
            ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
        ])
        transformers.append(('cat', categorical_transformer, categorical_features))
    
    return ColumnTransformer(transformers=transformers, remainder='drop')


class CustomTransformer:
    """Base class for custom transformers."""
    
    def fit(self, X, y=None):
        """Fit the transformer."""
        return self
    
    def transform(self, X):
        """Transform the data."""
        raise NotImplementedError("Transform method must be implemented")
    
    def fit_transform(self, X, y=None):
        """Fit and transform the data."""
        return self.fit(X, y).transform(X)
