import pandas as pd

def load_data():
    data=pd.read_csv('C:\Users\prabhat.j\Downloads\route optimize\data\delivery_data.csv')
    print(data.head())
    return data

if __name__=="__main__":
    load_data()