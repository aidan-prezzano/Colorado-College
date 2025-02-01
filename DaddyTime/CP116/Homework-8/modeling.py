import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
from sklearn.tree import DecisionTreeRegressor  # Model 2: Decision Tree
from sklearn.ensemble import RandomForestRegressor  # Model 3: Random Forest
from sklearn.metrics import r2_score, mean_absolute_error  # For evaluating model performance


# **************************************************************************


TRAIN_TEST_SPLIT_TEST_SIZE = 0.25

TRAIN_TEST_SPLIT_RANDOM_STATE = 42

# **************************************************************************


def linear_regression(df):

    Y = df['Life Ladder']
    X = df.drop(columns=['Country', 'Life Ladder'])

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=TRAIN_TEST_SPLIT_TEST_SIZE, random_state=TRAIN_TEST_SPLIT_RANDOM_STATE)

    linear_model = LinearRegression()
    linear_model.fit(X_train, Y_train)
    score = linear_model.score(X_train, Y_train)

    print('Linear Regression Score: ' + str(score))

# **************************************************************************


def xyz_model(df):

    Y = df['Life Ladder']
    X = df.drop(columns=['Country', 'Life Ladder'])

# **************************************************************************


def run_modeling():

    # set the CSV file into dataframe, and drop all rows with null values
    df = pd.read_csv('happiness.csv')
    df.dropna(inplace=True)

    linear_regression(df)


# **************************************************************************


run_modeling()


# **************************************************************************
