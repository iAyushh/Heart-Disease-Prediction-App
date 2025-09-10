# Heart Disease Prediction App

A simple web application that predicts the likelihood of heart disease based on user-provided health data. Built using **Python**, **scikit-learn**, and **Streamlit**.

---

## 🚀 Features

- User-friendly interface built with **Streamlit**.
- Interactive form to input health parameters.
- Machine learning model (Logistic Regression) trained to predict heart disease risk.
- Preprocessing steps (scaling, encoding) integrated into the pipeline.
- Easy deployment and extensibility.

---

## 🛠️ Tech Stack

- Python
- scikit-learn
- Pandas & NumPy
- Matplotlib & Seaborn
- Joblib
- Streamlit

---

## 📁 Project Structure

heart_disease_project/
│
├── data/ # Raw dataset (heart.csv)
├── models/ # Trained ML model (model.pkl)
├── notebooks/ # Exploratory Data Analysis (EDA)
├── src/ # Source code (data preprocessing, model training, prediction)
│ ├── data_preprocessing.py
│ ├── train_model.py
│ └── predict.py
├── app.py # Streamlit app (User Interface)
├── requirements.txt # Project dependencies
├── .gitignore
└── README.md

---

## ⚡ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/iAyushh/Heart-Disease-Prediction-App.git
   cd Heart-Disease-Prediction-App

2. Set up virtual environment:
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Train the model (optional if model already provided):
   python -c "from src.train_model import train_and_save_model; train_and_save_model()"

5. Run the Streamlit app
   streamlit run app.py

🎯 Sample Input Parameters

Age: 54

Sex: 1

Chest pain type: 2

Resting BP: 140

Cholesterol: 250

Fasting Blood Sugar: 0

Resting ECG: 1

Max Heart Rate: 150

Exercise Angina: 0

Oldpeak: 1.5

ST Slope: 2

2


📊 Outcome

0: No Heart Disease

1: Heart Disease Predicted

Predicted

📄 License

This project is open-source under the MIT License.

✨ Feel free to contribute or provide feedback!
🚀 Connect with me: https://www.linkedin.com/in/iAyushh
