import pip
import numpy as np
import pandas as pd

def load_data():
       df = pd.read_csv(r"C:\Users\Sony\Desktop\crypto-markets23.csv")
       return df

def clean_data(df):
    df=df.dropna()
    return df

def analyze_data(df):
    print(df.head()) 
    print(df.describe())    

def main():
    df= load_data()
    df=clean_data(df)
    analyze_data(df)

if __name__ == "__main__":
 main()




