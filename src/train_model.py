import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

def train_and_save_model():
    df = pd.read_csv("data/dataset.csv")
    
    X = df.drop("target", axis=1)
    y = df["target"]
    
    categorical_cols = ["sex", "chest pain type", "fasting blood sugar", 
                        "resting ecg", "exercise angina", "ST slope"]
    
    numeric_cols = [col for col in X.columns if col not in categorical_cols]
    
    preprocessor = ColumnTransformer(transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(drop='first'), categorical_cols)
    ])
    
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression())
    ])
    
    pipeline.fit(X, y)
    
    joblib.dump(pipeline, "models/model.pkl")
    print("Model trained and saved successfully.")
