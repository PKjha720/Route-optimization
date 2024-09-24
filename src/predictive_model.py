# src/predictive_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from src.data_preparation import load_data

def build_predictive_model():
    data = load_data()
    X = data[['DistanceToDestination (km)', 'TrafficCondition (1-5)', 'OrderVolume']]
    y = data['DeliveryTime (min)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error: {mae:.2f} minutes')

    return model

if __name__ == "__main__":
    build_predictive_model()
