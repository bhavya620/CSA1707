# Decision Tree Example in Python (Classification)

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text

# Load sample dataset (Iris dataset)
iris = load_iris()
X, y = iris.data, iris.target

# Create and train decision tree
clf = DecisionTreeClassifier(criterion="gini", max_depth=3)
clf.fit(X, y)

# Print tree structure
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)

# Test prediction
sample = [[5.1, 3.5, 1.4, 0.2]]  # Example flower
prediction = clf.predict(sample)
print("Prediction for sample:", iris.target_names[prediction][0])
