# src/demand_forecasting.py
import pandas as pd
import matplotlib.pyplot as plt
from data_preparation import load_data

def forecast_demand():
    data = load_data()
    data['Date'] = pd.date_range(start='2024-01-01', periods=len(data), freq='D')
    data.set_index('Date', inplace=True)

    data['SMA_3'] = data['OrderVolume'].rolling(window=3).mean()
    data[['OrderVolume', 'SMA_3']].plot(title="Order Volume and Moving Average", xlabel="Date")
    plt.show()

if __name__ == "__main__":
    forecast_demand()
