from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Load California housing dataset
    housing = fetch_california_housing()
    X = housing.data
    y = housing.target


    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Measure performance
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared: {r2:.2f}")

    # Predict for first sample in test set
    sample = X_test[0].reshape(1, -1)
    print(sample.shape)
    #print("Shape of X_test[0]:", X_test[0].shape)
    #print("Type of X_test[0]:", type(X_test[0]))
    pred_value = model.predict(sample)
    print(f"Predicted median house value for sample 0: {pred_value[0]:.2f}")

if __name__ == "__main__":
    main()