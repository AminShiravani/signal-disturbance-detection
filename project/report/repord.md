# Signal Disturbance Detection and Analysis in Communication Systems

## 1. Introduction
This project investigates different types of signal distortions in communication systems including noise and channel effects.

---

## 2. Signal Model
We use a multi-tone sinusoidal signal:

- 5 Hz
- 12 Hz
- 25 Hz

---

## 3. Types of Disturbances

### 3.1 Gaussian Noise
Additive white Gaussian noise (AWGN) is applied.

### 3.2 Impulse Noise
Sparse high-amplitude spikes are introduced.

### 3.3 Amplitude Distortion
Frequency selective gain changes.

### 3.4 Phase Distortion
Phase shifts applied in frequency domain.

---

## 4. Detection Methods

- Z-score for impulse detection
- SNR estimation for Gaussian noise
- FFT-based spectral analysis
- Phase spectrum comparison

---

## 5. Filtering Techniques

- Median filter (Impulse noise removal)
- Low-pass filter (Gaussian noise reduction)

---

## 6. Results Summary

| Experiment | SNR Before | SNR After | Improvement |
|------------|------------|-----------|-------------|
| Gaussian   | ...        | ...       | ...         |
| Impulse    | ...        | ...       | ...         |
| Combined   | ...        | ...       | ...         |

---

## 7. Conclusion
The system successfully detects and mitigates multiple types of signal distortions using classical DSP techniques.

---

## 8. Figures
All figures are stored in:
