import re
import pandas as pd  # For data manipulation
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
from matplotlib import pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# **************************************************************************


# using a regular expression, find all words in a text
def words_in_text(text):
    return re.findall('[a-zA-Z-]+', text)


# **************************************************************************


# find the average length per word in the text
def avg_length_per_word_in_text(text):
    words = words_in_text(text)
    nbr_chars = 0
    for word in words:
        nbr_chars += len(word)
    return nbr_chars / len(words)


# find the average length of the longest 10 words in the text
def avg_length_of_longest_ten_words(text):
    words = words_in_text(text)
    sorted_words_by_length = sorted(words, key=len)[::-1]
    top_ten_sorted_words_by_length = sorted_words_by_length[:10]
    top_ten_sorted_words_by_length_as_text = ' '.join(top_ten_sorted_words_by_length)
    return avg_length_per_word_in_text(top_ten_sorted_words_by_length_as_text)

# **************************************************************************


# count the number of vowels in a word
def nbr_vowels_in_word(word):
    nbr_vowels = 0
    for char in word:
        nbr_vowels = (nbr_vowels + 1) if char.lower() in 'aeiou' else nbr_vowels
    return nbr_vowels


# find the average number of vowels per word in text (a collection of words)
def avg_nbr_vowels_per_word_in_text(text):
    words = words_in_text(text)
    nbr_vowels = 0
    for word in words:
        nbr_vowels += nbr_vowels_in_word(word)
    return nbr_vowels / len(words)


# **************************************************************************


def nbr_non_alpha_numeric_characters(text):
    non_alpha_numeric_chars = re.findall(r'[^a-zA-Z0-9\n]', text.replace(' ', ''))
    return len(non_alpha_numeric_chars)


# **************************************************************************

def run_readability():


    # open the CSV file, then drop any columns where 'Pub Year' does not exist
    df = pd.read_csv('readability_corpus.csv')
    df = df.dropna(subset=['Pub Year'])

    # add additional columns, to assist in modeling
    df['avg_length_per_word'] = df['Excerpt'].astype(str).apply(avg_length_per_word_in_text)
    df['avg_length_of_longest_ten_words'] = df['Excerpt'].astype(str).apply(avg_length_of_longest_ten_words)
    df['avg_nbr_vowels_per_word'] = df['Excerpt'].astype(str).apply(avg_nbr_vowels_per_word_in_text)
    df['nbr_non_alpha_numeric_characters'] = df['Excerpt'].astype(str).apply(nbr_non_alpha_numeric_characters)

    # create the training data sets
    train_df = df[df['split'] == 'Train']
    Y_train = train_df['BT Easiness']
    X_train = train_df[['Pub Year', 'avg_length_per_word', 'avg_length_of_longest_ten_words', 'avg_nbr_vowels_per_word', 'nbr_non_alpha_numeric_characters']]

    # create the testing data sets
    test_df = df[df['split'] == 'Test']
    Y_test = test_df['BT Easiness']
    X_test = test_df[['Pub Year', 'avg_length_per_word', 'avg_length_of_longest_ten_words', 'avg_nbr_vowels_per_word', 'nbr_non_alpha_numeric_characters']]

    # fit the model with the training data, then score it with the test data
    model = LinearRegression()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    print('Model Coefficients : ', model.coef_)
    print('Model Score: ' + str(score))

    # create predictions on test data
    Y_pred = model.predict(X_test)

    # create residuals,
    # if > 0, then prediction was higher than actual
    # if < 0, then prediction was lower than actual
    residuals = Y_pred - Y_test

    # plt out the residuals values
    plt.scatter(Y_pred, residuals)
    plt.axhline(y=0, color='green', linestyle='-')
    plt.axhline(y=-1, color='red', linestyle='-')
    plt.axhline(y=1, color='red', linestyle='-')
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    plt.show()


# **************************************************************************


run_readability()

# **************************************************************************

