from statistics import linear_regression

import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
import numpy as np
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

    df["avg_word_length"] = df["Excerpt"].astype(str).apply(lambda x: np.mean([len(word) for word in x.split()]) if x.split() else 0)

    def count_vowels(word):
        """Counts vowels in a given word."""
        return sum(1 for char in word if char.lower() in "aeiouy")

    def avg_vowels_per_word(text):
        """Computes the average number of vowels per word in a text."""
        words = text.split()
        if not words:  # Handle empty text
            return 0
        vowel_counts = [count_vowels(word) for word in words]
        return np.mean(vowel_counts)

    df["avg_vowels_per_word"] = df["Excerpt"].astype(str).apply(avg_vowels_per_word)

    avg_word_length = df["avg_word_length"]
    print(avg_word_length)

    df["num_commas"] = df["Excerpt"].astype(str).str.count(",")

    df["num_colons"] = df["Excerpt"].astype(str).str.count(":")


    num_semicolons_sorted = num_semicolons.sort_values(ascending=False)
    print(num_semicolons_sorted)
    print(df.loc[2856])

    X = df[["num_semicolons", "avg_word_length", "num_words", "num_commas", "num_colons", "avg_vowels_per_word"]]
    Y = df["BT Easiness"]

    # split the data into training data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.2, random_state=42)



    model = LinearRegression()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    print('Linear Regression Score: ' + str(score))


    #print(excerpt)
    num_words = len(df['Excerpt'])
    #print(num_words)




make_model()