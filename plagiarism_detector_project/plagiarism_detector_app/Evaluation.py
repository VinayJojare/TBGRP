
from sklearn.metrics import accuracy_score, classification_report

# Assume y_true is the true labels and y_pred is the predicted labels
y_true = [0, 1]  # 0: non-plagiarized, 1: plagiarized
y_pred = [0.2, 0.8]
 # Example prediction

# Evaluate accuracy
accuracy = accuracy_score(y_true, [1 if pred > 0.5 else 0 for pred in y_pred])
print("Accuracy:", accuracy)

# Evaluate precision, recall, and F1-score
print(classification_report(y_true, [1 if pred > 0.5 else 0 for pred in y_pred]))
