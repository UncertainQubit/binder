import pandas as pd

def check_1(df):
    if 'https://raw.githubusercontent.com/UncertainQubit/binder/master/ramen-ratings.csv' in df
        print('Correct!')
    else:
        print('Incorrect')
        
def hint_1():
    print('Remember to use the read_csv function')
    
def soln_1():
    print('df = pd.read_csv(\'https://raw.githubusercontent.com/UncertainQubit/binder/master/ramen-ratings.csv\')')