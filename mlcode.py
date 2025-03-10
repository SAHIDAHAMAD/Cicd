import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split   
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

sns.set(style='white')

data = pd.read_csv(r'code-1/iris.csv')
X = data.drop('Species', axis=1)  # Features
y = data['Species']  # Target


# Print the first few rows to check the data
print(data.head())

# Check for any missing values
print("Missing values in the dataset:\n", data.isnull().sum())

# Ensure that the data types are correct (convert to numeric if necessary)
data = data.apply(pd.to_numeric, errors='coerce')  # Convert to numeric, non-numeric will become NaN

# Drop rows with NaN values
data = data.dropna()


# Check the shape of the dataset
print(f"Dataset shape: {data.shape}")
print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")

# Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.80,test_size=0.20, random_state=0)

# Check the sizes of the train/test sets
print(f"Training set size: {X_train.shape}")
print(f"Test set size: {X_test.shape}")

# Initialize Logistic Regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.4f}")

bias = model.score(X_train, y_train)
variance = model.score(X_test, y_test)

print(bias)
print(variance)

# Save the results to a text file
with open('results.txt', 'w') as f:
    f.write(f"Model accuracy: {accuracy:.4f}\n")

# Calculate precision, recall, and F1 score
precision = precision_score(y_test, y_pred, average='micro')
recall = recall_score(y_test, y_pred, average='micro')
f1 = f1_score(y_test, y_pred, average='micro')

# Write the metrics to the results file
with open('results.txt', 'a') as f:
    f.write(f"Precision: {precision:.4f}\n")
    f.write(f"Recall: {recall:.4f}\n")
    f.write(f"F1 Score: {f1:.4f}\n")

# Plot and save the confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.tight_layout()
plt.savefig('confusion_matrix.png')

# Plot and save feature importance (coefficients for Logistic Regression)
plt.figure(figsize=(10, 6))
plt.barh(X.columns, model.coef_[0])
plt.xlabel('Importance')
plt.title('Feature Importance - Logistic Regression')
plt.tight_layout()
plt.savefig('feature_importance.png')
