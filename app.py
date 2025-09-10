import streamlit as st
import pandas as pd
from src.predict import predict_heart_disease

st.title("Heart Disease Prediction App")

# User Inputs
age = st.number_input("Age", 1, 120, 30)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
chest_pain_type = st.selectbox("Chest Pain Type (0 to 3)", [0, 1, 2, 3])
resting_bp_s = st.number_input("Resting Blood Pressure", 80, 200, 120)
cholesterol = st.number_input("Cholesterol", 100, 600, 200)
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar (0 or 1)", [0, 1])
resting_ecg = st.selectbox("Resting ECG (0 to 2)", [0, 1, 2])
max_heart_rate = st.number_input("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina (0 or 1)", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
st_slope = st.selectbox("ST Slope (0 to 2)", [0, 1, 2])

if st.button("Predict"):
    input_df = pd.DataFrame({
        "age": [age],
        "sex": [sex],
        "chest pain type": [chest_pain_type],
        "resting bp s": [resting_bp_s],
        "cholesterol": [cholesterol],
        "fasting blood sugar": [fasting_blood_sugar],
        "resting ecg": [resting_ecg],
        "max heart rate": [max_heart_rate],
        "exercise angina": [exercise_angina],
        "oldpeak": [oldpeak],
        "ST slope": [st_slope],
    })

    result = predict_heart_disease(input_df)
    st.write(f"Prediction: {'Heart Disease' if result == 1 else 'No Heart Disease'}")


