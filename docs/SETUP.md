# ML Pipeline Project - Setup Guide

## Prerequisites

- Python 3.10 or higher
- pip or uv package manager
- Git (optional, for version control)
- Jupyter Notebook (will be installed with dependencies)

## Installation Steps

### 1. Clone or Download the Repository

If using Git:
```bash
git clone <repository-url>
cd MLP
```

Or download and extract the ZIP file.

### 2. Create Virtual Environment (Recommended)

**Using venv:**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

**Using uv (faster):**
```bash
uv venv
.venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

**Option A: Using requirements.txt**
```bash
pip install -r requirements.txt
```

**Option B: Using pyproject.toml (recommended)**
```bash
pip install -e .
```

**Option C: With development dependencies**
```bash
pip install -e ".[dev]"
```

**Option D: Using uv**
```bash
uv pip install -r requirements.txt
```

### 4. Add Your Data Files

Place your CSV data files in the `data/raw/` directory:
- `data/raw/Preprocessing1.csv`
- `data/raw/DataPreprocessingGraded_dataset.csv`

**IMPORTANT**: The original data files were removed during reorganization. 
Make sure to add them back to `data/raw/` before running notebooks.

### 5. Verify Installation

Test that everything is installed correctly:

```bash
# Run Python import test
python -c "import pandas, numpy, sklearn, matplotlib, seaborn; print('All packages imported successfully!')"

# Run tests (if pytest is installed)
pytest tests/

# Check package installation
pip list | findstr "pandas numpy scikit-learn"
```

### 6. Start Jupyter Notebook

```bash
jupyter notebook
```

Navigate to `notebooks/` and open:
- `01_data_exploration.ipynb` - Data exploration and analysis
- `02_pipeline_transformers.ipynb` - Pipeline implementation

## Project Structure Overview

```
MLP/
├── config/                    # Configuration files
├── data/
│   ├── raw/                  # PLACE YOUR CSV FILES HERE
│   └── processed/            # Processed data output
├── notebooks/                # Jupyter notebooks
├── src/mlp/                  # Python package
├── tests/                    # Unit tests
├── models/                   # Saved models
├── docs/                     # Documentation
├── pyproject.toml           # Package configuration
├── requirements.txt         # Dependencies
└── README.md               # Main documentation
```

## Common Issues and Solutions

### Issue: Import errors when running notebooks

**Solution**: Make sure you've installed the package in editable mode:
```bash
pip install -e .
```

### Issue: Data files not found

**Solution**: 
1. Check that CSV files are in `data/raw/`
2. Use relative paths in notebooks: `../data/raw/Preprocessing1.csv`
3. Or use `os.path.join('..', 'data', 'raw', 'filename.csv')`

### Issue: Module not found errors

**Solution**: Install missing packages:
```bash
pip install package-name
```

Or reinstall all dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Kernel not found in Jupyter

**Solution**: Install ipykernel in your virtual environment:
```bash
python -m ipykernel install --user --name=mlp
```

## Development Setup

For contributing to the project:

1. Install with development dependencies:
```bash
pip install -e ".[dev]"
```

2. Set up pre-commit hooks (optional):
```bash
# Install pre-commit
pip install pre-commit

# Set up hooks
pre-commit install
```

3. Run code formatters:
```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/
```

4. Run tests with coverage:
```bash
pytest --cov=src/mlp --cov-report=html
```

## Next Steps

1. ✅ Complete installation
2. ✅ Add data files to `data/raw/`
3. ✅ Open and run `notebooks/01_data_exploration.ipynb`
4. ✅ Explore the data and analysis
5. ✅ Work on pipeline implementation in `notebooks/02_pipeline_transformers.ipynb`
6. ✅ Create your own models and experiments

## Additional Resources

- [README.md](../README.md) - Main project documentation
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Contribution guidelines
- [docs/PROJECT_SUMMARY.md](../docs/PROJECT_SUMMARY.md) - Detailed project summary
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)

## Getting Help

If you encounter issues:

1. Check the [README.md](../README.md)
2. Review error messages carefully
3. Check that all dependencies are installed
4. Verify data files are in the correct location
5. Open an issue on the project repository

## System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum, 8GB recommended
- **Disk Space**: ~500MB for dependencies and virtual environment
- **Python**: 3.10, 3.11, or 3.12

---

**Happy coding! 🚀**
