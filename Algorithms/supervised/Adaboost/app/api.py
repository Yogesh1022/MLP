import os
import sys
import joblib
import pandas as pd
from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel

# Add project root to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# -----------------------------------
# Load trained model
# -----------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "models" / "adaboost_model.joblib"

model = joblib.load(MODEL_PATH)


# -----------------------------------
# FastAPI app initialization
# -----------------------------------

app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict whether a bank customer will churn",
    version="1.0"
)


# -----------------------------------
# Input schema
# -----------------------------------

class CustomerData(BaseModel):

    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float


# -----------------------------------
# Home route
# -----------------------------------

@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API is running"
    }


# -----------------------------------
# Prediction route
# -----------------------------------

@app.post("/predict")
def predict(data: CustomerData):

    # Convert input to dataframe
    input_data = pd.DataFrame([data.dict()])


    # Feature Engineering (same as training)

    input_data["Avgspending"] = (
        input_data["Balance"] /
        (input_data["NumOfProducts"] + 1)
    )


    input_data["tenure_group"] = pd.cut(
        input_data["Tenure"],
        bins=[0,2,5,10],
        labels=["new","mid","loyal"]
    )


    # Encoding

    input_data = pd.get_dummies(input_data)

    # Align with training columns
    model_features = model.feature_names_in_

    input_data = input_data.reindex(columns=model_features, fill_value=0)


    # Prediction

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0][1]


    result = "Customer will churn" if prediction == 1 else "Customer will stay"


    return {

        "prediction": result,
        "churn_probability": float(probability)

    }
    