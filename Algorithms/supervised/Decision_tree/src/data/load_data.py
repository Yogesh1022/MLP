import pandas as pd

# Column names for Adult Income dataset
COLUMNS = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income"
]

def load_data(path: str) -> pd.DataFrame:
    """Load Adult dataset file into a DataFrame with canonical columns."""
    return pd.read_csv(
        path,
        header=None,
        names=COLUMNS,
        skipinitialspace=True,
        na_values=["?"],
    )


def load_train_test(train_path: str, test_path: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load train and test files and normalize test target labels."""
    train_df = load_data(train_path)
    test_df = load_data(test_path)

    # Adult test labels can appear as '<=50K.' or '>50K.'
    test_df["income"] = test_df["income"].astype(str).str.rstrip(".")

    return train_df, test_df

