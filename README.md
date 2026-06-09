# AI-RoadVision-Pothole-Detection

## 🚀 Project Overview

AI RoadVision is an intelligent road monitoring system that uses **YOLOv8**, **OpenCV**, and **Deep Learning** to detect potholes on road surfaces in real time. The system analyzes video frames, classifies road conditions, and generates visual and audio alerts whenever a pothole is detected.

This project was developed as a final-year Computer Science engineering project to demonstrate the application of Artificial Intelligence and Computer Vision in improving road safety and reducing vehicle damage caused by potholes.

---

## 🎯 Objectives

* Detect potholes from road images and videos.
* Classify road conditions as Normal Road or Pothole.
* Provide real-time alerts to drivers.
* Improve road safety through intelligent monitoring.
* Demonstrate the use of AI and Computer Vision in transportation systems.

---

## ✨ Features

* Real-time pothole detection using YOLOv8.
* Deep learning-based image classification.
* Video stream processing using OpenCV.
* Audio alert system for pothole detection.
* Visual warning indicators on detected potholes.
* Lightweight model suitable for real-time execution.
* Easy-to-use Python implementation.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries & Frameworks

* OpenCV
* NumPy
* Ultralytics YOLOv8

### Machine Learning

* Deep Learning
* Image Classification
* Computer Vision

### Development Tools

* Visual Studio Code
* Git
* GitHub

---

## 📂 Project Structure

```text
AI-RoadVision-Pothole-Detection/
│
├── baseFolder/
├── normal/
├── potholes/
├── runs/
├── finalAttempt.py
├── train.py
├── training.py
├── practicevideo.mp4
└── yolov8n-cls.pt
```

---

## 🔄 Working Process

### Step 1: Dataset Collection

Road images were collected and divided into two categories:

* Normal Road
* Pothole Road

### Step 2: Data Preparation

The dataset was automatically split into:

* Training Set (80%)
* Validation Set (20%)

### Step 3: Model Training

YOLOv8 Classification Model was trained using the prepared dataset.

Training Parameters:

* Model: YOLOv8 Nano Classification
* Epochs: 10
* Image Size: 224 × 224
* Batch Size: 16

### Step 4: Prediction

The trained model analyzes each video frame and predicts whether the road contains a pothole.

### Step 5: Alert Generation

When a pothole is detected:

* Warning message is displayed.
* Red alert indicator appears.
* Audio buzzer is activated.

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/taufique2001/AI-RoadVision-Pothole-Detection.git
cd AI-RoadVision-Pothole-Detection
```

### Install Dependencies

```bash
pip install ultralytics
pip install opencv-python
pip install numpy
```

Or

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the detection script:

```bash
python finalAttempt.py
```

The application will process the input video and display pothole detection results in real time.

---

## 🧠 Model Information

* Model Architecture: YOLOv8 Classification
* Framework: Ultralytics
* Input Size: 224 × 224
* Output Classes:

  * Normal Road
  * Pothole

---

## 📊 Results

The trained model successfully classifies road conditions and provides real-time alerts for pothole detection.

Key achievements:

* Accurate road surface classification
* Real-time video processing
* Immediate driver warning system
* Lightweight and efficient implementation

---

## 🚧 Future Enhancements

* Real-time webcam integration
* GPS-based pothole mapping
* Mobile application integration
* Cloud-based monitoring dashboard
* Object Detection instead of Classification
* Automatic pothole reporting system
* Smart city infrastructure integration

---

## 🎓 Academic Purpose

This project was developed as a Final Year Major Project for the Bachelor of Engineering (Computer Science) program.

It demonstrates practical implementation of:

* Artificial Intelligence
* Deep Learning
* Computer Vision
* Image Processing
* Real-Time Monitoring Systems

---

## 👨‍💻 Author

**Md Taufique Azam**

Bachelor of Engineering (Computer Science)

Rabindranath Tagore University (RNTU)

GitHub: https://github.com/taufique2001

Email: [taufiqueazam123@gmail.com](mailto:taufiqueazam123@gmail.com)

---

## 📜 License

This project is developed for educational and research purposes.

Feel free to use and modify the code with proper attribution.
