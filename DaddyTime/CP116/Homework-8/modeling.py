import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR


# **************************************************************************


# https://www.simplilearn.com/tutorials/scikit-learn-tutorial/sklearn-regression-models
#
# Linear Regression: https://en.wikipedia.org/wiki/Linear_regression
#
# Gradient Boosting: https://en.wikipedia.org/wiki/Gradient_boosting
#
# Support Vector Machine: https://en.wikipedia.org/wiki/Support_vector_machine


# **************************************************************************


TRAIN_TEST_SPLIT_TEST_SIZE = 0.25

TRAIN_TEST_SPLIT_RANDOM_STATE = 42


# **************************************************************************


def linear_regression(X_train, X_test, Y_train, Y_test):
    model = LinearRegression()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    print('Linear Regression Score: ' + str(score))


# **************************************************************************


def gradient_boosting_regressor(X_train, X_test, Y_train, Y_test):
    model = GradientBoostingRegressor()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    print('Gradient Boosting Regressor Score: ' + str(score))


# **************************************************************************


def support_vector_machine(X_train, X_test, Y_train, Y_test):
    model = SVR()
    model.fit(X_train, Y_train)
    score = model.score(X_test, Y_test)
    print('Support Vector Machine Score: ' + str(score))


# **************************************************************************


def run_modeling():

    # set the CSV file into dataframe, and drop all rows with null values
    df = pd.read_csv('happiness.csv')
    df.dropna(inplace=True)

    # define the target (Life Ladder) and its inputs, which is all columns BUT country, year, and the target - Life Ladded
    Y = df['Life Ladder']
    X = df.drop(columns=['Country', 'year', 'Life Ladder'])

    # split the data into training and test data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=TRAIN_TEST_SPLIT_TEST_SIZE, random_state=TRAIN_TEST_SPLIT_RANDOM_STATE)

    # test three different models
    linear_regression(X_train, X_test, Y_train, Y_test)
    gradient_boosting_regressor(X_train, X_test, Y_train, Y_test)
    support_vector_machine(X_train, X_test, Y_train, Y_test)


# **************************************************************************


run_modeling()


# **************************************************************************
