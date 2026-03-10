# Project Summary
# ===============

## Overview
This is an ML Pipeline project for flight price prediction and data analysis.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
# OR
pip install -e .
```

### 2. Run Notebooks
```bash
jupyter notebook notebooks/
```

### 3. Run Tests
```bash
pytest tests/
```

## Project Structure

```
MLP/
├── README.md                          # Main documentation
├── pyproject.toml                     # Package configuration
├── requirements.txt                   # Dependencies
├── setup.py                          # Setup script
├── LICENSE                           # MIT License
├── .gitignore                        # Git ignore rules
├── CONTRIBUTING.md                   # Contribution guidelines
├── CHANGELOG.md                      # Version history
│
├── config/                           # Configuration files
│   └── config.yaml                   # Main config
│
├── data/                            # Data directory
│   ├── raw/                         # Original datasets
│   │   ├── DataPreprocessingGraded_dataset.csv
│   │   └── Preprocessing1.csv
│   └── processed/                   # Processed data
│       └── .gitkeep
│
├── notebooks/                       # Jupyter notebooks
│   ├── 01_data_exploration.ipynb   # EDA and analysis
│   └── 02_pipeline_transformers.ipynb  # Pipeline demo
│
├── src/                            # Source code
│   └── mlp/                        # Main package
│       ├── __init__.py            # Package init
│       ├── data_preprocessing.py  # Data cleaning
│       ├── pipeline.py            # ML pipelines
│       └── utils.py               # Utilities
│
├── tests/                          # Test suite
│   ├── __init__.py
│   └── test_data_preprocessing.py
│
├── models/                         # Saved models
│   └── .gitkeep
│
└── docs/                           # Documentation
    └── .gitkeep
```

## Features

### Data Preprocessing (`src/mlp/data_preprocessing.py`)
- `DataCleaner`: Clean and standardize data
- `FeatureEngineer`: Create new features
- `load_data()`: Load datasets
- `get_data_summary()`: Get data statistics

### Pipeline (`src/mlp/pipeline.py`)
- `FlightPricePipeline`: End-to-end ML pipeline
- `create_preprocessing_pipeline()`: Flexible preprocessing
- Support for numeric and categorical features

### Utilities (`src/mlp/utils.py`)
- Price statistics calculation
- Weekend vs weekday analysis
- Visualization functions
- Model save/load
- Configuration management

## Development

### Install in Development Mode
```bash
pip install -e ".[dev]"
```

### Format Code
```bash
black src/ tests/
isort src/ tests/
```

### Run Linting
```bash
flake8 src/ tests/
mypy src/
```

### Run Tests with Coverage
```bash
pytest --cov=src/mlp --cov-report=html
```

## Usage Examples

### Load and Clean Data
```python
from mlp.data_preprocessing import load_data, DataCleaner

df = load_data('data/raw/Preprocessing1.csv')
cleaner = DataCleaner()
df_clean = cleaner.clean_additional_info(df)
```

### Create Pipeline
```python
from mlp.pipeline import FlightPricePipeline

numeric_features = ['Duration_seconds', 'Month']
categorical_features = ['Airline', 'Source', 'Destination']

pipeline = FlightPricePipeline(numeric_features, categorical_features)
X_transformed = pipeline.fit_transform(X)
```

### Analyze Prices
```python
from mlp.utils import compare_weekend_weekday_prices

stats = compare_weekend_weekday_prices(df)
print(f"Weekend average: {stats['weekend_mean']}")
print(f"Weekday average: {stats['weekday_mean']}")
```

## Configuration

Edit `config/config.yaml` to customize:
- Data paths
- Model parameters
- Feature lists
- Preprocessing settings

## Next Steps

1. Complete the pipeline implementation in `02_pipeline_transformers.ipynb`
2. Add more preprocessing functions
3. Implement model training
4. Add model evaluation metrics
5. Create prediction pipeline
6. Add more comprehensive tests
7. Create documentation

## Notes

- All notebooks use relative paths for portability
- Data files are in `data/raw/`
- Models should be saved to `models/`
- Follow PEP 8 style guidelines
- Write tests for new features

## Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Project README](README.md)
