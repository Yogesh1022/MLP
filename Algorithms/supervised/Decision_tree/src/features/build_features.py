import pandas as pd

def split_features(df: pd.DataFrame, target_col: str) -> tuple[pd.DataFrame, pd.Series]:
    """Split DataFrame into X features and y target."""
    features_df = df.drop(columns=[target_col])
    target_series = df[target_col]
    return features_df, target_series


def get_feature_types(df: pd.DataFrame):
    """Identify categorical and numerical feature columns."""

    categorical_features = df.select_dtypes(include=["object"]).columns.tolist()
    numerical_features = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

    return categorical_features, numerical_features


def encode_target(y: pd.Series) -> pd.Series:
    """Map Adult income labels to binary target."""
    return y.astype(str).str.strip().map({"<=50K": 0, ">50K": 1})