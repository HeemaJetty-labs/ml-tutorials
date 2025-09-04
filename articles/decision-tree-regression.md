# Decision Tree Regression

Decision Tree Regression is a non-parametric supervised learning method used for predicting continuous outcomes. It splits the input space into regions and fits simple models within these regions to predict the target variable.

## How It Works

- The model splits the dataset recursively based on feature values, creating a tree of decision rules.
- Each leaf node predicts a constant value (often the mean of the target in that region).
- The tree continues splitting until a stopping condition is met (e.g., maximum depth, minimum samples per leaf).

## When to Use

- For regression problems with non-linear relationships.
- When model interpretability and easy visualization are important.
- Suitable as a foundational algorithm before moving to ensemble methods like Random Forest.

## Implementation in Python

The example below demonstrates Decision Tree Regression using scikit-learn on the California Housing dataset.

/supervised-learning/regression/decision-tree-regression.py


## Summary

Decision Tree Regression provides an interpretable and effective way to model non-linear relationships, serving as a fundamental algorithm before exploring ensemble methods.



