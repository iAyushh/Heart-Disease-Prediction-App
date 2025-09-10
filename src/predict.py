import joblib
import pandas as pd

def predict_heart_disease(input_data):
    pipeline = joblib.load("models/model.pkl")
    prediction = pipeline.predict(input_data)
    return prediction[0]
