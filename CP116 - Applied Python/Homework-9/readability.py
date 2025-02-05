from statistics import linear_regression

import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
from matplotlib import pyplot as plt



def make_model():
    df = pd.read_csv('readability_corpus.csv')
    df.dropna(inplace=True)
    excerpt = df['Excerpt']


    df["num_words"] = df["Excerpt"].astype(str).str.split().str.len()
    num_words = df["num_words"]
    #print(num_words)

    df["num_semicolons"] = df["Excerpt"].astype(str).str.count(";")
    num_semicolons = df["num_semicolons"]
    #print(num_semicolons)


    num_semicolons_sorted = num_semicolons.sort_values(ascending=False)
    print(num_semicolons_sorted)
    print(df.loc[2853])

    X = df[["num_semicolons"]]
    Y = df["BT Easiness"]

    # split the data into training data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=42)



    model = LinearRegression()
    model.fit(X_train, Y_train)


    #print(excerpt)
    num_words = len(df['Excerpt'])
    #print(num_words)




make_model()