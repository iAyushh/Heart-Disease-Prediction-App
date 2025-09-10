import pandas as pd
from joblib import load


pipeline = load('models/model.pkl')

def predict_heart_disease(input_data):
    
    prediction = pipeline.predict(input_data)
    return prediction[0]
