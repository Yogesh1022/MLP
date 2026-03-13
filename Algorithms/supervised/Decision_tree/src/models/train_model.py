def train_model(pipeline, X_train, y_train):
    """Fit training pipeline and return fitted model."""
    pipeline.fit(X_train, y_train)
    return pipeline
