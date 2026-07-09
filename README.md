Handwritten Digit Recognizer using CNN
Project Overview

The Handwritten Digit Recognizer is a Deep Learning project that uses a Convolutional Neural Network (CNN) to recognize handwritten digits from images. The model is trained using the MNIST dataset, which contains thousands of handwritten digit images (0–9).

After training, the model can predict a handwritten digit from a custom image provided by the user.

Objectives
Learn image classification using Deep Learning.
Understand how Convolutional Neural Networks (CNNs) work.
Train a CNN model using the MNIST dataset.
Predict handwritten digits from custom images.
Technologies Used
Python
TensorFlow
Keras
NumPy
Matplotlib
OpenCV
Visual Studio Code
Dataset

MNIST Dataset

Training Images: 60,000
Testing Images: 10,000
Image Size: 28 × 28 pixels
Number of Classes: 10 (Digits 0–9)
Project Structure
Handwritten_Digit_Recognizer/
│
├── dataset/
├── images/
│   └── digit.png
│
├── models/
│   └── digit_model.h5
│
├── output/
│   ├── accuracy_graph.png
│   └── prediction_result.png
│
├── screenshots/
│   └── mnist_samples.png
│
├── train.py
├── predict.py
├── requirements.txt
├── README.md
└── .gitignore
Features
Load the MNIST dataset.
Preprocess image data.
Normalize pixel values.
Build a CNN model.
Train the model.
Evaluate model accuracy.
Save the trained model.
Predict custom handwritten digits.
Save prediction results and accuracy graph.
CNN Architecture
Input Layer (28 × 28 × 1)
Convolution Layer (32 Filters)
Max Pooling Layer
Convolution Layer (64 Filters)
Max Pooling Layer
Flatten Layer
Dense Layer (64 Neurons)
Output Layer (10 Neurons with Softmax)
Installation

Install the required libraries using:

pip install -r requirements.txt
How to Run
Train the Model
python train.py

This will:

Load the MNIST dataset.
Train the CNN model.
Save the trained model.
Generate an accuracy graph.
Predict a Digit

Place your handwritten digit image inside the images folder with the name:

digit.png

Run:

python predict.py

The program will display the predicted digit and confidence score.

Sample Output

Example:

Predicted Digit : 1
Confidence      : 99.78%
Applications
Bank cheque digit recognition
Postal ZIP code recognition
OCR (Optical Character Recognition)
Educational AI projects
Machine Learning practice
Future Enhancements
Real-time webcam digit recognition
Handwritten digit recognition using a mobile camera
Web application using Flask or Streamlit
Recognition of letters (A–Z)
Recognition of multiple digits in one image
Author

Keerthi K R

Internship Project – Handwritten Digit Recognizer using CNN
