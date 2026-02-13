# EyeDrive: AI-Powered Hybrid Eye-Tracking & Voice Interface

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![AI Framework](https://img.shields.io/badge/AI-MediaPipe-green)](https://mediapipe.dev/)

## Project Overview
**EyeDrive** is an advanced assistive technology designed for individuals with severe motor impairments. It enables full computer control through a combination of **eye-tracking** and **voice commands**. By leveraging deep learning, EyeDrive provides a free, software-based alternative to expensive hardware such as Tobii Eye Trackers.

## 🚀 Key Features
- **Hybrid Control:** Combine gaze-based navigation with voice commands for maximum productivity.
- **Voice Integration:** Launch applications like **Microsoft Word** ("Open Word") and dictate text via voice.
- **Smart Text Injection:** Automated text input using **Clipboard Injection** to ensure 100% accuracy in any language (including Cyrillic).
- **Multithreading:** The voice engine runs in a background thread to ensure zero lag in cursor movement.
- **Blink-to-Click:** Intelligent left-click emulation through eyelid distance analysis.
- **No Extra Hardware:** Works with any standard built-in laptop webcam (640x480+).

## 🛠 Tech Stack
- **Language:** Python
- **Computer Vision:** OpenCV & MediaPipe Face Mesh (468 landmarks + Iris tracking).
- **Speech Recognition:** Google Speech API (SpeechRecognition library).
- **System Automation:** PyAutoGUI & Pyperclip.

## 🧠 How It Works
1. **Iris Localization:** The system tracks landmarks (474–478) to find the exact center of the pupil.
2. **Coordinate Mapping:** A custom **Gain Factor** algorithm translates micro-eye movements into full-screen cursor coordinates.
3. **Jitter Mitigation:** Software smoothing filters eliminate "shaking" caused by webcam sensor noise.
4. **Voice Processing:** A concurrent thread listens for commands. For text input, it copies recognized speech to the clipboard and performs a `Ctrl+V` injection at the gaze point.

## 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/nastyabatu-cpu/EyeDrive-AI-Control.git](https://github.com/nastyabatu-cpu/EyeDrive-AI-Control.git)
   cd EyeDrive-AI-Control
