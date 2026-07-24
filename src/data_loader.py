import pandas as pd

def load_titanic_data(path='../data/train.csv'):
    return pd.read_csv(path)