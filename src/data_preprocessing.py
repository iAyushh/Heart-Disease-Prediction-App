import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def preprocess_data(df):
    # Define numerical and categorical columns
    numeric_features = ['age', 'resting bp s', 'cholesterol', 'max heart rate', 'oldpeak']
    categorical_features = ['sex', 'chest pain type', 'fasting blood sugar', 'resting ecg', 
                            'exercise angina', 'ST slope']

    # Preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ]
    )

    # Apply preprocessing
    X = preprocessor.fit_transform(df)
    
    return X, preprocessor
