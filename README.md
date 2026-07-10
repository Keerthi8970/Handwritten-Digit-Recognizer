# 🧠 Handwritten Digit Recognizer using CNN

A Deep Learning project that recognizes handwritten digits (0–9) using a **Convolutional Neural Network (CNN)** trained on the **MNIST dataset**. The trained model can accurately predict handwritten digits from custom images provided by the user.

---

## 📌 Project Overview

The **Handwritten Digit Recognizer** is an image classification project developed using **TensorFlow** and **Keras**. It uses a Convolutional Neural Network (CNN) to learn patterns from handwritten digits in the MNIST dataset and predict digits from new handwritten images.

This project demonstrates the complete Deep Learning workflow including:

- Loading and preprocessing image data
- Building a CNN model
- Training the model
- Evaluating model performance
- Saving the trained model
- Predicting handwritten digits from custom images

---

## 🎯 Objectives

- Learn image classification using Deep Learning.
- Understand the working of Convolutional Neural Networks (CNNs).
- Train a CNN model using the MNIST dataset.
- Predict handwritten digits from custom images.
- Gain practical experience with TensorFlow and Keras.

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- OpenCV
- Visual Studio Code
- Git & GitHub

---

## 📂 Dataset

### MNIST Dataset

The MNIST dataset contains grayscale images of handwritten digits.

| Feature | Details |
|---------|---------|
| Training Images | 60,000 |
| Testing Images | 10,000 |
| Image Size | 28 × 28 pixels |
| Number of Classes | 10 (Digits 0–9) |

---

# 📁 Project Structure

```text
Handwritten-Digit-Recognizer/
│
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
```

---

# ✨ Features

- 📥 Load the MNIST dataset
- 🖼️ Display sample handwritten digits
- 🔄 Preprocess image data
- 📊 Normalize pixel values
- 🧠 Build a CNN model
- 🎯 Train the CNN model
- 📈 Evaluate model accuracy
- 💾 Save the trained model
- 🔍 Predict custom handwritten digits
- 📉 Generate an accuracy graph
- 🖼️ Save prediction results

---

# 🧠 CNN Architecture

```
Input Layer
(28 × 28 × 1)
        │
        ▼
Conv2D (32 Filters)
        │
        ▼
MaxPooling2D
        │
        ▼
Conv2D (64 Filters)
        │
        ▼
MaxPooling2D
        │
        ▼
Flatten
        │
        ▼
Dense (64 Neurons)
        │
        ▼
Output Layer (10 Neurons - Softmax)
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Keerthi8970/Handwritten-Digit-Recognizer.git
```

### Navigate to the Project Folder

```bash
cd Handwritten-Digit-Recognizer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 How to Run

## Step 1: Train the CNN Model

Run the following command:

```bash
python train.py
```

### During training, the program will:

- Load the MNIST dataset
- Preprocess the images
- Build the CNN model
- Train the model
- Evaluate model accuracy
- Save the trained model
- Generate the accuracy graph

---

## Step 2: Predict a Handwritten Digit

Place your handwritten image inside the **images** folder.

Rename the image as:

```text
digit.png
```

Then run:

```bash
python predict.py
```

The program will:

- Load the trained model
- Read the handwritten image
- Predict the digit
- Display the confidence score
- Save the prediction result

---

# 📷 Sample Output

```
==============================

Predicted Digit : 1

Confidence : 99.78%

==============================
```

---

# 📊 Applications

- 🏦 Bank cheque digit recognition
- 📮 Postal ZIP code recognition
- 📄 Optical Character Recognition (OCR)
- 🤖 AI and Machine Learning projects
- 🎓 Educational Deep Learning projects
- ✍️ Digit recognition systems

---

# 🚀 Future Enhancements

- 📷 Real-time webcam digit recognition
- 📱 Mobile camera digit recognition
- 🌐 Deploy using Flask
- 🌐 Deploy using Streamlit
- 🔤 Alphabet recognition (A–Z)
- 🔢 Multi-digit recognition
- ☁️ Cloud deployment

---
Installed 

<img width="1917" height="1012" alt="Screenshot 2026-07-09 214644" src="https://github.com/user-attachments/assets/6e082ed7-1ee4-416b-b9e4-2a50f4470878" />


# 📚 Learning Outcomes

Through this project, I learned:

- Image preprocessing
- CNN architecture
- TensorFlow & Keras
- Image classification
- Model evaluation
- Deep Learning workflow
- OpenCV image processing
- GitHub project management

---

# 👨‍💻 Author

**Keerthi K R**

🎓 B.Tech Information Technology Student

💻 AI & Machine Learning Enthusiast

📧 Email: **keerthiranganath08@gmail.com**

🔗 LinkedIn: **https://www.linkedin.com/in/keerthi-k-r-2371773a7**

🐙 GitHub: **https://github.com/Keerthi8970**

---



## 📜 License

This project is developed for **educational and learning purposes** as part of an **AI Internship Project**.
