# Linear Regression

Linear Regression is a fundamental supervised learning algorithm used for predicting continuous numerical values. It models the relationship between one or more input features and a continuous output variable by fitting a linear equation to observed data.

## How It Works

Linear regression fits a line \( y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n \) that minimizes the sum of squared differences between predicted and actual values (least squares method).

## When to Use

- Predicting continuous outcomes like house prices, temperatures, or sales.
- Modeling linear relationships between variables.

## Assumptions

- Linear relationship between input features and output.
- Residuals (errors) are normally distributed.
- Homoscedasticity: constant variance of errors.
- No or little multicollinearity among features.

## Implementation in Python

The example below demonstrates Linear Regression using scikit-learn on the Boston housing dataset.

supervised-learning/regression/linear-regression.py

## Summary

Linear Regression is a simple yet powerful approach for continuous value prediction and serves as a great starting point for regression problems in machine learning.

