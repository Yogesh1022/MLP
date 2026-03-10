"""
Test Data Preprocessing Module
==============================

Unit tests for data preprocessing functions.
"""

import pytest
import pandas as pd
import numpy as np
from src.mlp.data_preprocessing import DataCleaner, FeatureEngineer, get_data_summary


class TestDataCleaner:
    """Test cases for DataCleaner class."""
    
    def test_clean_additional_info(self):
        """Test cleaning of Additional_Info column."""
        df = pd.DataFrame({
            'Additional_Info': ['No info', ' NO info', 'No Info', ' No info', 'In-flight meal']
        })
        
        cleaner = DataCleaner()
        result = cleaner.clean_additional_info(df)
        
        # All variants should be standardized to 'No info'
        expected_values = ['No info', 'No info', 'No info', 'No info', 'In-flight meal']
        assert result['Additional_Info'].tolist() == expected_values
    
    def test_remove_duplicates(self):
        """Test duplicate removal."""
        df = pd.DataFrame({
            'A': [1, 2, 2, 3],
            'B': [4, 5, 5, 6]
        })
        
        cleaner = DataCleaner()
        result = cleaner.remove_duplicates(df)
        
        assert len(result) == 3
        assert cleaner.cleaning_log[-1].startswith("Removed 1 duplicate")


class TestFeatureEngineer:
    """Test cases for FeatureEngineer class."""
    
    def test_create_weekend_flag(self):
        """Test weekend flag creation."""
        df = pd.DataFrame({
            'WeekDay': ['Monday', 'Saturday', 'Sunday', 'Tuesday']
        })
        
        engineer = FeatureEngineer()
        result = engineer.create_weekend_flag(df)
        
        expected = [0, 1, 1, 0]
        assert result['is_weekend'].tolist() == expected


def test_get_data_summary():
    """Test data summary function."""
    df = pd.DataFrame({
        'A': [1, 2, 3, None],
        'B': ['x', 'y', 'z', 'x']
    })
    
    summary = get_data_summary(df)
    
    assert summary['shape'] == (4, 2)
    assert 'A' in summary['columns']
    assert summary['missing_values']['A'] == 1
    assert summary['duplicates'] == 0
