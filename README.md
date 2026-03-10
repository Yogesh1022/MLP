# ML Pipeline Project

A Machine Learning Pipeline project for flight price prediction and data preprocessing using Scikit-Learn.

## 📋 Project Overview

This project implements a comprehensive machine learning pipeline for analyzing and predicting flight ticket prices. It includes data preprocessing, exploratory data analysis (EDA), and modular transformation pipelines.

## 🗂️ Project Structure

```
MLP/
├── README.md                 # Project documentation
├── pyproject.toml           # Project metadata and dependencies
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
├── LICENSE                 # Project license
│
├── data/                   # Data directory
│   ├── raw/               # Raw, immutable data
│   └── processed/         # Cleaned and processed data
│
├── notebooks/             # Jupyter notebooks
│   ├── 01_data_exploration.ipynb      # Data exploration and EDA
│   └── 02_pipeline_transformers.ipynb # Pipeline implementation
│
├── src/                   # Source code
│   └── mlp/              # Main package
│       ├── __init__.py
│       ├── data_preprocessing.py  # Data preprocessing utilities
│       ├── pipeline.py           # ML pipeline definitions
│       └── utils.py             # Helper functions
│
├── tests/                # Unit tests
│   └── __init__.py
│
├── config/               # Configuration files
│   └── config.yaml      # Project configuration
│
├── models/              # Trained models
│
└── docs/               # Additional documentation
```

## 🚀 Getting Started

### Prerequisites

- Python >= 3.10
- pip or uv package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd MLP
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Or using `uv`:
```bash
uv pip install -r requirements.txt
```

### Using pyproject.toml (recommended)

```bash
pip install -e .
```

## 📊 Dataset

The project uses flight pricing datasets:
- **DataPreprocessingGraded_dataset.csv**: Graded dataset for preprocessing tasks
- **Preprocessing1.csv**: Flight pricing data with features including:
  - Airline
  - Source and Destination
  - Duration
  - Price (target variable)
  - Month, WeekDay
  - Additional_Info

## 🔧 Usage

### Running Notebooks

1. Start Jupyter:
```bash
jupyter notebook
```

2. Navigate to `notebooks/` and open the desired notebook.

### Data Exploration

The `01_data_exploration.ipynb` notebook includes:
- Data loading and inspection
- Statistical analysis
- Price trend analysis by weekday/weekend
- Monthly flight distribution
- Data cleaning operations

### Pipeline Implementation

The `02_pipeline_transformers.ipynb` notebook demonstrates:
- Multiple transformer pipelines
- Feature engineering
- Data preprocessing workflows

## 📦 Dependencies

Core dependencies:
- pandas: Data manipulation
- numpy: Numerical computations
- scikit-learn: Machine learning algorithms
- matplotlib: Plotting
- seaborn: Statistical visualizations
- jupyter: Interactive notebooks

See `requirements.txt` or `pyproject.toml` for complete list with versions.

## 🧪 Testing

Run tests using pytest:
```bash
pytest tests/
```

## 📝 Development

### Code Style

This project follows PEP 8 guidelines. Format code using:
```bash
black src/
```

### Type Checking

```bash
mypy src/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset source: [Add source if applicable]
- Scikit-learn documentation and examples

## 📧 Contact

For questions or feedback, please open an issue in the repository.

---

**Note**: This is an educational project for learning ML pipeline development with Scikit-Learn.
