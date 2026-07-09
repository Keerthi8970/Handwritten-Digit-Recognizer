# ============================================================
# Handwritten Digit Recognizer using CNN
# File : predict.py
# ============================================================

# ----------------------------
# Step 1 : Import Libraries
# ----------------------------

import tensorflow as tf
import numpy as np
import cv2
import matplotlib

# Prevent Tkinter error
matplotlib.use('Agg')

import matplotlib.pyplot as plt

# ----------------------------
# Step 2 : Load Saved Model
# ----------------------------

print("Loading Trained Model...")

model = tf.keras.models.load_model("models/digit_model.h5")

print("Model Loaded Successfully.")

# ----------------------------
# Step 3 : Read Image
# ----------------------------

image = cv2.imread("images/digit.png", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found.")
    print("Please place digit.png inside the images folder.")
    exit()

print("Image Loaded Successfully.")

# ----------------------------
# Step 4 : Resize Image
# ----------------------------

image = cv2.resize(image, (28,28))

# ----------------------------
# Step 5 : Invert Colors
# ----------------------------

image = 255 - image

# ----------------------------
# Step 6 : Normalize
# ----------------------------

image = image.astype("float32") / 255.0

# ----------------------------
# Step 7 : Reshape
# ----------------------------

image = image.reshape(1,28,28,1)

# ----------------------------
# Step 8 : Predict
# ----------------------------

prediction = model.predict(image)

digit = np.argmax(prediction)

confidence = np.max(prediction) * 100

print("\n==============================")
print("Predicted Digit :", digit)
print("Confidence      : {:.2f}%".format(confidence))
print("==============================")

# ----------------------------
# Step 9 : Save Prediction Image
# ----------------------------

display_image = image.reshape(28,28)

plt.imshow(display_image, cmap="gray")
plt.title(f"Predicted Digit : {digit}")
plt.axis("off")

plt.savefig("output/prediction_result.png")
plt.close()

print("\nPrediction image saved in output folder.")