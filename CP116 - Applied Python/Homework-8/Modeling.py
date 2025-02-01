import pandas as pd  # For data manipulation
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.linear_model import LinearRegression  # Model 1: Linear Regression
from sklearn.tree import DecisionTreeRegressor  # Model 2: Decision Tree
from sklearn.ensemble import RandomForestRegressor  # Model 3: Random Forest
from sklearn.metrics import r2_score, mean_absolute_error  # For evaluating model performance


# Read the CSV file into a pandas DataFrame
df = pd.read_csv('happiness.csv')


print(df.head())  # Displays the first 5 rows of the dataset
print(df.info())  # Shows data types and non-null counts for each column

# Define the target variable (Y) and input features (X)
# Select relevant quantitative features as X
# Select the happiness score (or another appropriate column) as Y
Y = df['Life Ladder']
X = df.drop(columns=['Life Ladder'])

X = pd.get_dummies(X, drop_first=True)


# Use train_test_split to divide data into training and testing sets
# Split the dataset into 80% training and 20% testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Print the shapes to verify the split
print("X_train shape:", X_train.shape)  # Should be 80% of the original data
print("X_test shape:", X_test.shape)    # Should be 20% of the original data
print("Y_train shape:", Y_train.shape)  # Matches X_train in rows
print("Y_test shape:", Y_test.shape)    # Matches X_test in rows
# Step 6: Instantiate three different models
# Choose at least three different models (e.g., Linear Regression, Decision Tree, Random Forest)

# Instantiate the models
linear_model = LinearRegression()  # Linear Regression model
tree_model = DecisionTreeRegressor(random_state=42)  # Decision Tree model
forest_model = RandomForestRegressor(n_estimators=100, random_state=42)  # Random Forest model

# Step 7: Train each model
# Fit the models using the training data
# Step 7: Train each model
linear_model.fit(X_train, Y_train)
tree_model.fit(X_train, Y_train)
forest_model.fit(X_train, Y_train)


# Step 8: Evaluate each model
# Predict using the testing data
# Compute the performance score (e.g., R-squared for regression, accuracy for classification)


# Compute R-squared scores for regression models

# Step 9: Compare results
# Print and compare the scores for each model
# Identify the best-performing model

# Step 10: Interpret results
# Briefly analyze which factors contribute most to happiness
# Discuss findings based on model performance