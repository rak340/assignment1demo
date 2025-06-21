

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
class_names = iris.target_names

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Define a custom input (e.g., new flower sample)
# Format: [sepal length, sepal width, petal length, petal width]
sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])

# Predict the species
predicted_class = model.predict(sample_input)[0]
predicted_species = class_names[predicted_class]

print("🌸 Iris Species Prediction 🌸")
print(f"Given flower data: {sample_input[0]}")
print(f"Predicted Species: {predicted_species.capitalize()}")
