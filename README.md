EyeDrive: AI-Powered Assistive Eye-Tracking Interface

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Framework](https://img.shields.io/badge/AI-MediaPipe-green)](https://mediapipe.dev/)

Project Overview
**EyeDrive** is an accessibility tool designed for individuals with motor impairments. It allows users to control the computer cursor using only their eye movements. By leveraging computer vision and deep learning, this project aims to provide a low-cost, software-based alternative to expensive hardware eye-trackers.



Key Features
- **Real-time Tracking:** High-speed iris tracking with minimal latency.
- **Hands-free Navigation:** Complete cursor control (movement and interaction).
- **No Extra Hardware:** Works with any standard 720p/1080p webcam.
- **AI-Driven:** Powered by Google's MediaPipe Face Mesh (468 landmarks).

Tech Stack
- **Language:** Python
- **Computer Vision:** OpenCV
- **AI Engine:** MediaPipe (Face Mesh)
- **System Control:** PyAutoGUI (Mouse automation)

How It Works
1. **Face Mesh Detection:** The system detects 468 facial landmarks.
2. **Iris Localization:** Specific landmarks (IDs 468-473) are tracked to locate the iris.
3. **Screen Mapping:** The program calculates the relative position of the iris within the eye socket and translates it to screen coordinates $(X, Y)$.
4. **Smoothing:** Applying moving average filters to reduce cursor jitter for better UI/UX.

Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nastyabatu-cpu/EyeDrive-AI-Control.git](https://github.com/nastyabatu-cpu/EyeDrive-AI-Control.git)
   cd EyeDrive-AI-Control
