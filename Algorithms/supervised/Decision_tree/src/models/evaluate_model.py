from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(y_true, y_pred):
    """Return evaluation metrics for classification model."""
    acc = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)
    return {
        "accuracy": acc,
        "classification_report": report,
        "confusion_matrix": cm,
    }
