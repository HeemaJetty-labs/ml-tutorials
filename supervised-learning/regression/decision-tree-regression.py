from sklearn.datasets import fetch_california_housing
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Load California Housing dataset
    housing = fetch_california_housing()
    X = housing.data
    y = housing.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize Decision Tree Regressor
    model = DecisionTreeRegressor(random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Calculate and print evaluation metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R^2 Score: {r2:.4f}")

    # Predict example input
    sample = X_test[0].reshape(1, -1) #Take the first test example
    pred_value = model.predict(sample)[0]
    print(f"Predicted value for sample {sample.tolist()}: {pred_value:.4f}")

if __name__ == "__main__":
    main()
