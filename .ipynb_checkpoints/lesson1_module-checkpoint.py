import pandas as pd

def check_1(df):
    if df.equals(pd.read_csv('https://raw.githubusercontent.com/UncertainQubit/binder/master/Melbourne_housing_FULL.csv')):
        print('Correct!')
    else:
        print('Incorrect')