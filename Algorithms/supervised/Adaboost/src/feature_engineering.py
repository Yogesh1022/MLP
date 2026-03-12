import pandas as pd

def create_features(df):
    """
    Create new feature from existing feature if necessary.
    
    """
    # average spending featuere
    df["Avgspending"] = df["Balance"] / (df["NumOfProducts"] + 1)  # add 1 to avoid division by zero

    #tenure group
    df["tenure_group"] = pd.cut(
        df["Tenure"],
        bins=[0,2,5,10],
        labels=["new","mid","loyal"]
    )

    return df

def encode_features(df):
    """
    
    Encode categorical features using one-hot encoding or label encoding as appropriate.
    
    """

    # convert the target variable
    df["Exited"] = df["Exited"].astype(int)

    # one-hot encode the categorical features
    df = pd.get_dummies(df, drop_first=True)

    return df