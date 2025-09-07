from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

#Load dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Initialize SVM classifier with RBF kernel
model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)

#Train the model
model.fit(X_train, y_train)

#Predict on test set
y_pred = model.predict(X_test)

#Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:')
print(classification_report(y_test, y_pred))

#Predict on a sample
sample = X_test[0].reshape(1, -1)
predicted_class = model.predict(sample)
class_name = iris.target_names[predicted_class]
print(f'Predicted class for sample {sample.tolist()}: {class_name}')