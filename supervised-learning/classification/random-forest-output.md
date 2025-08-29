## Output of random-forest.py. 
## We can create a md format by adding the following in the code - 
report = classification_report(y_true, y_pred, output_dict=True)

df = pd.DataFrame(report).transpose()

markdown_table = df.to_markdown()

print(markdown_table)

=========Output on VScode terminal======== 

Accuracy: 1.00

Classification Report:

| Class | Precision | Recall | F1-score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 1.00   | 1.00     | 10      |
| 1     | 1.00      | 1.00   | 1.00     | 9       |
| 2     | 1.00      | 1.00   | 1.00     | 11      |

| Metric       | Value |
|--------------|-------|
| Accuracy     | 1.00  |
| Macro avg    | 1.00  |
| Weighted avg | 1.00  |

Predicted class for sample `[[5.1, 3.5, 1.4, 0.2]]`: ['setosa']
