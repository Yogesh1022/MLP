from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


def evaluate_model(y_test, y_pred):
    """Return and print common classification metrics."""

    acc = accuracy_score(y_test, y_pred)
    clf_report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("Accuracy:", acc)
    print("\nClassification Report:\n")
    print(clf_report)

    print("\nConfusion Matrix:\n")
    print(cm)

    return {
        "accuracy": acc,
        "classification_report": clf_report,
        "confusion_matrix": cm,
    }