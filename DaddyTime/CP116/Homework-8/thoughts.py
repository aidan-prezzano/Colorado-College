import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
from matplotlib import pyplot as plt
import seaborn as sns

# **************************************************************************


TRAIN_TEST_SPLIT_TEST_SIZE = 0.25

TRAIN_TEST_SPLIT_RANDOM_STATE = 42


# **************************************************************************


def run_thoughts():

    # set the CSV file into dataframe, and drop all rows with null values
    df = pd.read_csv('happiness.csv')
    df.dropna(inplace=True)

    # define the target (Life Ladder) and its inputs, which is all columns BUT country, year, and the target - Life Ladded
    Y = df['Life Ladder']
    X = df.drop(columns=['Country', 'year', 'Life Ladder'])

    # split the data into training and test data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=TRAIN_TEST_SPLIT_TEST_SIZE, random_state=TRAIN_TEST_SPLIT_RANDOM_STATE)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    # predicting on the X_test data set
    print(model.predict(X_test))

    # summary of the model
    print('model intercept :', model.intercept_)
    print('model coefficients : ', model.coef_)
    print('Model score : ', model.score(X, Y))

    Y_pred = model.predict(X_test)

    #print(Y_test)
    #print(Y_pred)

    residuals = Y_test - Y_pred
    plt.scatter(Y_pred, residuals)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.title("Residual Plot")
    plt.show()



# **************************************************************************


run_thoughts()


# **************************************************************************