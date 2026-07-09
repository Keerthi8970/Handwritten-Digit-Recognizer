# ============================================================
# Handwritten Digit Recognizer using CNN and MNIST Dataset
# File: train.py
# ============================================================

# ----------------------------
# Step 1: Import Libraries
# ----------------------------

import tensorflow as tf
import numpy as np
import matplotlib

# Use a non-GUI backend to avoid Tkinter errors
matplotlib.use('Agg')

import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# ----------------------------
# Step 2: Load the MNIST Dataset
# ----------------------------

print("Loading MNIST Dataset...")

(X_train, y_train), (X_test, y_test) = mnist.load_data()

print("\n========== DATASET INFORMATION ==========")
print("Training Images :", X_train.shape)
print("Training Labels :", y_train.shape)
print("Testing Images  :", X_test.shape)
print("Testing Labels  :", y_test.shape)

# ----------------------------
# Step 3: Save Sample Images
# ----------------------------

plt.figure(figsize=(8,8))

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(str(y_train[i]))
    plt.axis('off')

plt.tight_layout()
plt.savefig("screenshots/mnist_samples.png")
plt.close()

print("\nSample images saved in screenshots folder.")

# ----------------------------
# Step 4: Normalize Images
# ----------------------------

print("\nNormalizing Images...")

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

print("Maximum Pixel Value :", X_train.max())
print("Minimum Pixel Value :", X_train.min())

# ----------------------------
# Step 5: Reshape Images
# ----------------------------

print("\nReshaping Images...")

X_train = X_train.reshape((60000,28,28,1))
X_test = X_test.reshape((10000,28,28,1))

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# ----------------------------
# Step 6: Build CNN Model
# ----------------------------

print("\nBuilding CNN Model...")

model = Sequential()

model.add(Conv2D(
    filters=32,
    kernel_size=(3,3),
    activation='relu',
    input_shape=(28,28,1)
))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(
    filters=64,
    kernel_size=(3,3),
    activation='relu'
))

model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(
    units=64,
    activation='relu'
))

model.add(Dense(
    units=10,
    activation='softmax'
))

print("\nCNN Model Summary\n")
model.summary()

# ----------------------------
# Step 7: Compile Model
# ----------------------------

print("\nCompiling Model...")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("Model Compiled Successfully.")

# ----------------------------
# Step 8: Train Model
# ----------------------------

print("\nTraining Started...\n")

history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_data=(X_test,y_test)
)

print("\nTraining Completed Successfully.")

# ----------------------------
# Step 9: Evaluate Model
# ----------------------------

print("\nEvaluating Model...")

loss, accuracy = model.evaluate(X_test,y_test)

print("\nTest Loss :", loss)
print("Test Accuracy :", accuracy)

# ----------------------------
# Step 10: Save Model
# ----------------------------

model.save("models/digit_model.h5")

print("\nModel saved successfully.")
print("Location : models/digit_model.h5")

# ----------------------------
# Step 11: Plot Accuracy Graph
# ----------------------------

plt.figure(figsize=(8,5))

plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training vs Validation Accuracy")

plt.legend()

plt.savefig("output/accuracy_graph.png")
plt.close()

print("\nAccuracy graph saved in output folder.")

print("\nProject Training Completed Successfully.")