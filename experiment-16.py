# Simple Feed Forward Neural Network in Python (using NumPy)

import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of sigmoid (for training, if needed)
def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (4 samples, 2 features each)
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# Expected output (XOR function for demo)
y = np.array([[0],[1],[1],[0]])

# Set random seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))

# Forward pass function
def forward_pass(X):
    hidden_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_input)

    return final_output

# Test the network
print("Feed Forward Neural Network Output:")
output = forward_pass(X)
print(output)
