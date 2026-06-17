# 📡 Signal Disturbance Detection and Adaptive Restoration System

## 🎯 Project Overview

This project implements a complete **Digital Signal Processing (DSP) pipeline** for detecting, analyzing, and mitigating various types of signal disturbances in communication systems.

It simulates real-world signal degradation scenarios such as:
- Gaussian noise contamination
- Impulse noise (spikes)
- Amplitude distortion
- Phase distortion
- Combined multi-noise environments

and applies adaptive filtering and signal reconstruction techniques to restore signal quality.

---

## 🧠 Key Idea

In real communication systems, transmitted signals are often corrupted by channel noise and distortions.

This project models that process and builds a system capable of:

> **Detecting disturbances → Analyzing them → Restoring the original signal**

---

## ⚙️ Features

### 📊 Signal Processing
- Multi-frequency sinusoidal signal generation
- Time-domain and frequency-domain analysis (FFT)

### 🔊 Noise & Distortion Modeling
- Gaussian noise (AWGN channel model)
- Impulse noise (spike interference)
- Amplitude distortion (gain variation per frequency)
- Phase distortion (phase shifting per component)

### 🧪 Detection System
- Time-domain noise estimation
- Frequency-domain spectral deviation analysis
- Z-score based impulse detection
- Distortion classification logic

### 🔧 Signal Restoration
- Low-pass filtering (Gaussian noise reduction)
- Median filtering (impulse noise removal)
- FFT-based correction for distortions

### 📈 Evaluation Metrics
- SNR (Signal-to-Noise Ratio)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- Correlation Coefficient

---

## 🧪 Experiments

The system is evaluated through five structured experiments:

1. **Gaussian Noise Analysis**
2. **Impulse Noise Detection & Removal**
3. **Amplitude Distortion Analysis**
4. **Phase Distortion Analysis**
5. **Combined Real-World Disturbance Scenario**

Each experiment includes:
- Signal corruption simulation
- Disturbance detection
- Signal restoration
- Performance evaluation

---

## 📊 Example Output

The system compares:

- Clean Signal
- Corrupted Signal
- Processed (Restored) Signal

and evaluates improvements using quantitative metrics like SNR and correlation.

---

## 🧩 Project Structure
project/
│
├── config.py
├── signal_generator.py
├── noise_adder.py
├── distortion.py
├── filters.py
├── metrics.py
├── detectors.py
├── plots.py
│
├── experiments/
│ ├── exp1_gaussian.py
│ ├── exp2_impulse.py
│ ├── exp3_amplitude.py
│ ├── exp4_phase.py
│ └── exp5_combined.py
│ 
│
└── final_demo.py


---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python final_demo.py

📌 Technologies Used
Python 3
NumPy
SciPy
Matplotlib
Digital Signal Processing (DSP) concepts
🧠 What This Project Demonstrates

This project demonstrates:

Understanding of DSP fundamentals
Noise modeling in communication systems
Frequency-domain signal analysis
Adaptive filtering techniques
Performance evaluation of signal restoration systems
📈 Conclusion

This system simulates a simplified communication channel and demonstrates how digital signal processing techniques can be used to detect and mitigate real-world signal disturbances.

While idealized, it provides a strong foundation for understanding practical DSP systems used in modern communication engineering.

👨‍💻 Author

Student Project – Signal Processing Course
Focus: Signal Disturbance Detection & Restoration