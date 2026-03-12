import os
import sys
import joblib

# add project rooot to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_preprocessing import load_data, clean_data, handling_missing_values
from src.feature_engineering import create_features, encode_features
from src.train_model import split_data, train_model
from src.evaluate_model import evaluate_model

def run_training_pipeline():
    print("========== TRAINING PIPELINE STARTED ==========")

    # ----------------------------------
    # 1 Load Data
    # ---------------------------------
    print("Loading data...")

    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "Churn_Modelling.csv")

    df = load_data(data_path)
    print("Data loaded successfully.")
    
    # ----------------------------------
    # 2 Data Cleaning
    # ----------------------------------
    print("\nCleaning data...")

    df = clean_data(df)

    print("Data cleaned")
    # ----------------------------------
    # 3 Handling Missing Values
    # ----------------------------------
    print("\nHandling missing values...")
    df = handling_missing_values(df)
    print("Missing values handled.")

    # ----------------------------------
    # 4 Feature Engineering
    # ----------------------------------
    print("\nCreating features...")
    df = create_features(df)
    print("Features created.")
    print("\nEncoding features...")
    df = encode_features(df)        
    print("Features encoded.")  

    # ----------------------------------
    # 5 Train-Test Split
    # ----------------------------------
    print("\nSplitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = split_data(df)

    print("Data split completed.")
    # ----------------------------------
    # 6 Train Model
    # ----------------------------------
    print("\nTraining model...")
    model = train_model(X_train, y_train)
    print("Model trained successfully.")
    # ----------------------------------
    # 7 Evaluate Model
    # ----------------------------------
    print("\nEvaluating model...")
    evaluate_model(model, X_test, y_test)
    print("Model evaluation completed.")
    # ----------------------------------
    # 8 Save Model
    # ----------------------------------
    print("\nSaving model...")  
    model_path = "../models/adaboost_model.joblib"
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    print("========== TRAINING PIPELINE COMPLETED ==========")
if __name__ == "__main__":
    run_training_pipeline()


 