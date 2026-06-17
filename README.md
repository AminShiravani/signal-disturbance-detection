# 📡 Signal Disturbance Detection and Adaptive Restoration System

---

## 🎯 Project Overview

This project implements a complete **Digital Signal Processing (DSP) pipeline** for detecting, analyzing, and mitigating different types of signal disturbances in communication systems.

It simulates real-world channel impairments and evaluates how well signal processing techniques can restore degraded signals.

---

## 🧠 Core Idea

In real-world communication systems, transmitted signals are affected by noise and distortions.

This project models the full pipeline:

> **Clean Signal → Disturbance Injection → Detection → Restoration → Evaluation**

---

## ⚙️ Features

### 📊 Signal Processing
- Multi-frequency sinusoidal signal generation
- Time-domain analysis
- Frequency-domain analysis using FFT

### 🔊 Noise & Distortion Models
- Gaussian noise (AWGN)
- Impulse noise (spikes)
- Amplitude distortion
- Phase distortion
- Combined real-world disturbances

### 🧪 Detection System
- Time-domain noise estimation
- FFT-based spectral deviation detection
- Z-score based impulse detection
- Distortion classification logic

### 🔧 Signal Restoration
- Low-pass filtering (Gaussian noise reduction)
- Median filtering (impulse removal)
- Frequency-domain correction techniques

### 📈 Evaluation Metrics
- Signal-to-Noise Ratio (SNR)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Correlation coefficient

---

## 🧪 Experiments

The system evaluates five main scenarios:

1. Gaussian noise analysis  
2. Impulse noise detection & removal  
3. Amplitude distortion analysis  
4. Phase distortion analysis  
5. Combined real-world disturbance scenario  

Each experiment includes:
- Signal corruption
- Disturbance detection
- Signal restoration
- Performance evaluation

---

## 📊 Results Interpretation

The system compares:

- 🔵 Clean Signal (reference)
- 🟠 Corrupted Signal (noisy/distorted)
- 🟢 Processed Signal (restored)

and evaluates performance using:
- SNR improvement
- Error reduction (MSE / RMSE)
- Signal similarity (Correlation)

---

## 🧩 Project Structure

project/

├── config.py  
├── signal_generator.py  
├── noise_adder.py  
├── distortion.py  
├── filters.py  
├── metrics.py  
├── detectors.py  
├── plots.py  

├── experiments/  
│   ├── exp1_gaussian.py  
│   ├── exp2_impulse.py  
│   ├── exp3_amplitude.py  
│   ├── exp4_phase.py  
│   └── exp5_combined.py  

└── final_demo.py  

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python final_demo.py
```


## 🛠 Technologies Used

- Python 3  
- NumPy  
- SciPy  
- Matplotlib  
- Digital Signal Processing (DSP)

---

## 🧠 Key Concepts Demonstrated

- Signal modeling and synthesis  
- Noise modeling in communication systems  
- Frequency-domain analysis (FFT)  
- Adaptive filtering techniques  
- Signal quality evaluation metrics  

---

## 📌 Conclusion

This project simulates a simplified communication channel with realistic disturbances and demonstrates how DSP techniques can be used to detect and reduce signal degradation.

While simplified, it provides a strong foundation for understanding practical signal processing systems used in modern communications.

---

## 👨‍💻 Author

Student Project – Signal Processing Course  
Focus: Signal Disturbance Detection & Restoration