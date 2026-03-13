def make_predictions(model, X_test):
    """Generate class predictions from a trained model."""

    predictions = model.predict(X_test)

    return predictions


def make_prediction_probabilities(model, X_test):
    """Generate class probabilities when model supports predict_proba."""
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X_test)
    return None