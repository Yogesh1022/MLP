from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier


def create_training_pipeline(categorical_features, numerical_features, model_params=None):
    """Create preprocessing + Decision Tree pipeline."""

    if model_params is None:
        model_params = {
            "criterion": "gini",
            "max_depth": 8,
            "min_samples_split": 20,
            "min_samples_leaf": 10,
            "random_state": 42,
        }

    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", categorical_transformer, categorical_features),
            ("num", "passthrough", numerical_features)
        ]
    )

    model = DecisionTreeClassifier(**model_params)

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    return pipeline