# Essential Machine Learning Terms with Examples

## Evaluation Metrics

- **Accuracy**  
  Measure of overall correctness: the portion of correct predictions.  
  Example: If a model predicts 80 out of 100 emails correctly as spam or not spam, accuracy = 80%.

- **Precision**  
  Proportion of predicted positives that are actually positive.  
  Example: If 70 emails are predicted as spam but only 60 actually are, precision = 60/70 = 85.7%.

- **Recall (Sensitivity)**  
  Proportion of actual positives correctly identified.  
  Example: If 100 emails are actually spam and the model identifies 60, recall = 60/100 = 60%.

- **F1 Score**  
  Harmonic mean of precision and recall, balancing both.  
  Example: For precision 85.7% and recall 60%,  
  \( F1 = 2 \times \frac{0.857 \times 0.6}{0.857 + 0.6} \approx 70.6\% \).

- **Specificity**  
  Proportion of actual negatives correctly identified.  
  Example: Of 200 non-spam emails, if 190 are correctly predicted as not spam, specificity = 190/200 = 95%.

- **ROC Curve**  
  Graph showing True Positive Rate (TPR) vs. False Positive Rate (FPR) at different thresholds to evaluate classifiers.

- **AUC (Area Under Curve)**  
  Scalar measure of ROC curve performance; closer to 1 means better classification.

- **Confusion Matrix**  
  Table showing True Positives, False Positives, True Negatives, False Negatives.  
  Example:  
  |             | Predicted Spam | Predicted Not Spam |  
  |-------------|----------------|--------------------|  
  | Actual Spam | 60 (TP)        | 40 (FN)            |  
  | Actual Not Spam | 10 (FP)     | 190 (TN)          |

====================================================================================

## Data Concepts

- **Feature**  
  Input variable used by the model.  
  Example: Email length, number of links in email body.

- **Label (Target)**  
  The output the model predicts.  
  Example: Spam or Not-Spam.

- **Training Set**  
  Dataset used to train the model.  
  Example: 70% of the labeled emails.

- **Test Set**  
  Dataset used to evaluate model performance.  
  Example: The remaining 30% of emails.

- **Validation Set**  
  Dataset for tuning parameters during training.

- **Overfitting**  
  Model learning noise too well, poor generalization.  
  Example: Model predicts training emails perfectly but fails on new emails.

- **Underfitting**  
  Model too simple to capture the pattern.

====================================================================================

## Algorithm Concepts

- **Supervised Learning**  
  Learning from labeled data.  
  Example: Email classifier trained on labeled spam/not-spam emails.

- **Unsupervised Learning**  
  Learning without labeled data.  
  Example: Clustering customer purchase histories.

- **Reinforcement Learning**  
  Learning with feedback from interaction.  
  Example: A robot learning to navigate a maze.

- **Classification**  
  Predicting categories.  
  Example: Spam or not spam.

- **Regression**  
  Predicting continuous values.  
  Example: House price prediction.

- **Clustering**  
  Grouping similar data points.  
  Example: Market segmentation.

- **Feature Engineering**  
  Creating or transforming features to improve models.  
  Example: Extracting keyword counts from email text.

====================================================================================

## Model & Training Terms

- **Epoch**  
  One full pass through the training data.  
  Example: 10 epochs means dataset passed 10 times.

- **Batch Size**  
  Number of samples processed before updating model.  
  Example: Batch size of 32.

- **Learning Rate**  
  Step size for weight updates.  
  Example: 0.01.

- **Gradient Descent**  
  Optimization algorithm to minimize loss.

- **Loss Function**  
  Quantifies error between predictions and true labels.

- **Hyperparameter**  
  Settings chosen before training.  
  Example: Number of trees in a forest.

- **Regularization**  
  Penalties to reduce overfitting.

====================================================================================

## Miscellaneous Terms

- **Bias-Variance Tradeoff**  
  Balancing simplicity and complexity to prevent over/underfitting.

- **Cross-Validation**  
  Method to evaluate model stability.

- **PCA (Principal Component Analysis)**  
  Dimensionality reduction technique.

- **Confounding Variable**  
  Variable that affects both input and output, confusing analysis.

- **Feature Scaling**  
  Normalizing features to similar scales.

- **Model Drift**  
  Decline in model performance over time.

- **Transfer Learning**  
  Using a pre-trained model on a new task.

- **Ensemble Learning**  
  Combining multiple models for better performance.

