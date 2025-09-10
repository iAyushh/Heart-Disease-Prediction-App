from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import dump
from .data_preprocessing import preprocess_data
import pandas as pd

def train_and_save_model():
    # Load dataset
    df = pd.read_csv('data/dataset.csv')

   
    X = df.drop('target', axis=1)
    y = df['target']


    X_processed, preprocessor = preprocess_data(X)

    # Train model
    model = LogisticRegression()
    model.fit(X_processed, y)

    
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])


    dump(pipeline, 'models/model.pkl')
