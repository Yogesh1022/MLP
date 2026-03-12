from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

import seaborn as sns
import matplotlib.pyplot as plt



def evaluate_model(model, X_test, y_test):

    """
    Evaluate trained model
    """

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Accuracy:", accuracy)

    print("\nClassification Report:\n")

    print(classification_report(y_test, predictions))

    cm = confusion_matrix(y_test, predictions)

    plt.figure(figsize=(6,4))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title("Confusion Matrix")

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    plt.show()