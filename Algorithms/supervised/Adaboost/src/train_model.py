from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

def split_data(df):
    """
    Split the dataset into training and testing sets.
    
    """
    X = df.drop("Exited", axis=1)
    y = df["Exited"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train the AdaBoost model using the training data.
    
    """
    base_model = DecisionTreeClassifier(max_depth=3)
    model = AdaBoostClassifier(
        estimator=base_model,
        n_estimators=300,
        learning_rate=0.1,
        random_state=42
    )
    model.fit(X_train, y_train)
    

    return model