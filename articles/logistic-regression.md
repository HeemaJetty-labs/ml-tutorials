# Logistic Regression

Logistic Regression is a supervised learning algorithm used for binary classification problems. It models the probability that a given input belongs to a particular class using the logistic (sigmoid) function.

## How It Works

Logistic regression estimates the probability \(P(y=1|X)\) by fitting a logistic function:

\[
P(y=1|X) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \cdots + \beta_n x_n)}}
\]

where \(\beta\) are the parameters learned during training.

## When to Use

- Binary classification tasks (e.g., spam detection, disease diagnosis).
- When you want probabilistic outputs with interpretable coefficients.

## Implementation in Python

The example below demonstrates Logistic Regression using scikit-learn on the Iris dataset to classify one species vs. others.
/supervised-learning/classification/logistic-regression.py

## Summary

Logistic Regression is a widely used, interpretable classifier ideal for binary classification problems with probabilistic outputs.

