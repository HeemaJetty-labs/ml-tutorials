# Decision Tree Classifier

Decision Trees are a popular supervised learning algorithm used for both classification and regression tasks. They work by splitting the data into subsets based on feature values, creating a tree-like model of decisions.

## How It Works

A decision tree splits the dataset on the feature that results in the highest information gain or lowest impurity (such as Gini impurity or entropy). The process continues recursively on each subset until stopping criteria are met (e.g., maximum depth or minimum samples).

## When to Use

- Classification tasks with interpretable decision rules.
- When you want to visualize the decision process.
- Good for handling both categorical and numerical data.

## Implementation in Python

The example below demonstrates a Decision Tree classifier using scikit-learn on the Iris dataset.
supervised-learning/classification/decision-tree.py


## Summary

Decision Trees provide an interpretable and powerful way to classify data by hierarchical splitting of features and are widely used in machine learning tasks.

