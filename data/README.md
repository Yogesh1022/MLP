# Data Directory

This directory contains all data files for the ML Pipeline project.

## Structure

- `raw/`: Original, immutable data files
  - Place your CSV datasets here (e.g., `Preprocessing1.csv`, `DataPreprocessingGraded_dataset.csv`)
  - These files should never be modified directly
  
- `processed/`: Cleaned and processed data files
  - Output from preprocessing scripts
  - Ready for model training

## Data Files

### Expected Raw Data Files:
1. **Preprocessing1.csv**: Flight pricing dataset with features:
   - Airline
   - Source, Destination
   - Duration_seconds
   - Price (target variable)
   - Month, WeekDay
   - Additional_Info

2. **DataPreprocessingGraded_dataset.csv**: Graded dataset for preprocessing tasks

## Usage

To load data in notebooks:
```python
import pandas as pd
import os

# Load from notebooks directory
data_path = os.path.join('..', 'data', 'raw', 'Preprocessing1.csv')
df = pd.read_csv(data_path)
```

To load data in Python scripts:
```python
from mlp.data_preprocessing import load_data

df = load_data('data/raw/Preprocessing1.csv')
```

## Notes

- Raw data files are NOT tracked by git (see .gitignore)
- To use this project, place your CSV files in the `raw/` directory
- Processed files are also gitignored by default
- Add `.gitkeep` files to track empty directories in git

## Data Source

[Add information about where the data comes from]
