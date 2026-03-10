# Quick Start Guide

Get up and running with the ML Pipeline project in 5 minutes!

## 🚀 Quick Setup (5 steps)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add Your Data
Place your CSV files in `data/raw/`:
- `Preprocessing1.csv`
- `DataPreprocessingGraded_dataset.csv`

### 3. Install Package
```bash
pip install -e .
```

### 4. Start Jupyter
```bash
jupyter notebook
```

### 5. Open Notebook
Navigate to `notebooks/01_data_exploration.ipynb` and run it!

---

## 📦 What's Included

### Notebooks
- **01_data_exploration.ipynb** - Data analysis and EDA
- **02_pipeline_transformers.ipynb** - ML pipeline demo

### Python Modules
```python
# Import and use
from mlp.data_preprocessing import DataCleaner, FeatureEngineer
from mlp.pipeline import FlightPricePipeline
from mlp.utils import calculate_price_statistics
```

### Example Usage

```python
# Load data
import pandas as pd
df = pd.read_csv('data/raw/Preprocessing1.csv')

# Clean data
from mlp.data_preprocessing import DataCleaner
cleaner = DataCleaner()
df_clean = cleaner.clean_additional_info(df)

# Analyze prices
from mlp.utils import compare_weekend_weekday_prices
stats = compare_weekend_weekday_prices(df_clean)
print(stats)

# Create pipeline
from mlp.pipeline import FlightPricePipeline
pipeline = FlightPricePipeline(
    numeric_features=['Duration_seconds', 'Month'],
    categorical_features=['Airline', 'Source', 'Destination']
)
```

---

## 📁 Project Structure

```
MLP/
├── data/raw/              ← PUT CSV FILES HERE
├── notebooks/             ← Jupyter notebooks
├── src/mlp/              ← Python package
├── tests/                ← Tests
├── config/               ← Configuration
└── docs/                 ← Documentation
```

---

## 🔍 Next Steps

1. ✅ Run the data exploration notebook
2. ✅ Try the example code above
3. ✅ Read [README.md](README.md) for full docs
4. ✅ Check [docs/SETUP.md](docs/SETUP.md) for detailed setup
5. ✅ Start building your own models!

---

## 💡 Helpful Commands

```bash
# Run tests
pytest tests/

# Format code
black src/

# View project structure
tree /F    # Windows
tree       # macOS/Linux

# Install dev dependencies
pip install -e ".[dev]"
```

---

## ❓ Need Help?

- 📖 Read the [README.md](README.md)
- 🔧 Check [docs/SETUP.md](docs/SETUP.md)
- 📝 See [docs/PROJECT_SUMMARY.md](docs/PROJECT_SUMMARY.md)
- 🤝 Read [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Happy coding! 🎉**
