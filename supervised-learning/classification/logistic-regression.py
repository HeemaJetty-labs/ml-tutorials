from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

def main():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = (iris.target == 0).astype(int)  # Binary target: setosa vs others

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize Logistic Regression model
    model = LogisticRegression(max_iter=200)

    # Train the model
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")

    # Print detailed classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Predict class for a sample
    sample = [[5.1, 3.5, 1.4, 0.2]]
    pred_class = model.predict(sample)
    #print(pred_class)
    class_name = iris.target_names[pred_class] if pred_class == 0 else "not setosa"
    print(f"Predicted class for sample {sample}: {class_name}")

if __name__ == "__main__":
    main()
