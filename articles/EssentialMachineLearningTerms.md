# Essential Machine Learning Terms Every Engineer Should Know

## Evaluation Metrics

- **Accuracy**  
  The ratio of correctly predicted observations to the total observations.  
  $$
  \text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Samples}}
  $$

- **Precision**  
  The ratio of correctly predicted positive observations to the total predicted positives.  
  $$
  \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
  $$

- **Recall (Sensitivity or True Positive Rate)**  
  The ratio of correctly predicted positive observations to all actual positives.  
  $$
  \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
  $$

- **F1 Score**  
  The harmonic mean of precision and recall, balancing both.  
  $$
  \text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  $$

- **Specificity (True Negative Rate)**  
  The ratio of correctly predicted negative observations to all actual negatives.  
  $$
  \text{Specificity} = \frac{\text{True Negatives}}{\text{True Negatives} + \text{False Positives}}
  $$

- **ROC Curve (Receiver Operating Characteristic curve)**  
  A graph showing the trade-off between true positive rate (Recall) and false positive rate at various threshold settings.

- **AUC (Area Under the ROC Curve)**  
  A single scalar value summarizing the ROC curve's performance; closer to 1 means better model performance.

- **Confusion Matrix**  
  A table layout showing true positives, false positives, true negatives, and false negatives used for classification evaluation.

==========================================================================================================================

## Data Concepts

- **Feature**  
  An individual measurable property or characteristic used as input for the model.

- **Label (Target)**  
  The output variable that the model aims to predict.

- **Training Set**  
  The dataset used to train the machine learning model.

- **Test Set**  
  The dataset for evaluating the model's performance on unseen data.

- **Validation Set**  
  A dataset used to tune model parameters and prevent overfitting.

- **Overfitting**  
  When a model learns the training data too well including noise, causing poor generalization to new data.

- **Underfitting**  
  When a model is too simple and can't capture the underlying pattern of data.

==========================================================================================================================

## Algorithm Concepts

- **Supervised Learning**  
  Machine learning tasks where the model learns from labeled data.

- **Unsupervised Learning**  
  Tasks where the model learns patterns from unlabeled data.

- **Reinforcement Learning**  
  Training an agent to make decisions by rewarding desired behavior and/or punishing undesired ones.

- **Classification**  
  Predicting discrete categories or classes.

- **Regression**  
  Predicting continuous numeric values.

- **Clustering**  
  Grouping data points into clusters based on similarity.

- **Feature Engineering**  
  Creating new input features from raw data to improve model performance.

==========================================================================================================================

## Model & Training Terms

- **Epoch**  
  One complete pass of the training dataset through the learning algorithm.

- **Batch Size**  
  The number of training samples used in one iteration during training.

- **Learning Rate**  
  A hyperparameter controlling how much the model updates weights during training.

- **Gradient Descent**  
  A method to minimize loss by updating model parameters iteratively in the direction of the steepest descent.

- **Loss Function**  
  A function representing the error between predicted and true values used to train the model.

- **Hyperparameter**  
  Parameters set before training that control the learning process (e.g., learning rate, number of trees).

- **Regularization**  
  Techniques (like L1, L2) to prevent overfitting by adding a penalty on larger weights.

==========================================================================================================================

## Miscellaneous Terms

- **Bias-Variance Tradeoff**  
  The balance between a model’s ability to generalize (low variance) and its accuracy on training data (low bias).

- **Cross-Validation**  
  A technique for assessing how the results of a model will generalize to an independent dataset, commonly K-Fold.

- **Principal Component Analysis (PCA)**  
  A dimensionality reduction technique that transforms features into a smaller set of uncorrelated components.

- **Confounding Variable**  
  An external influence that can affect both independent and dependent variables, potentially misleading analysis.

- **Feature Scaling**  
  The process of normalizing/standardizing features to a common scale.

- **Model Drift**  
  The degradation of a model’s predictive performance over time due to changes in data patterns.

- **Transfer Learning**  
  Using a pre-trained model on a new, but related, task to save training time and improve performance.

- **Ensemble Learning**  
  Combining multiple models to improve overall performance, e.g., Random Forest, Gradient Boosting.

