import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import numpy as np

from config import (
    SAMPLE_RATE,
    DURATION,
    FREQUENCIES,
    AMPLITUDES,
    PHASES,
    GAUSSIAN_SNR,
    IMPULSE_PROBABILITY,
    IMPULSE_AMPLITUDE,
    AMPLITUDE_DISTORTION_FREQS,
    AMPLITUDE_DISTORTION_GAINS,
    PHASE_DISTORTION_FREQS,
    PHASE_DISTORTION_SHIFTS,
)

from signal_generator import generate_multitone
from noise_adder import add_combined_noise
from distortion import apply_amplitude_distortion, apply_phase_distortion
from filters import lowpass_filter, median_filter
from detectors import detect_comprehensive
from metrics import calculate_all_metrics
from plots import plot_time_signal, plot_fft, compare_signals

# -------------------------
# 1. Time vector
# -------------------------
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

# -------------------------
# 2. Clean signal
# -------------------------
clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

# -------------------------
# 3. Step 1: Add Gaussian + Impulse noise
# -------------------------
noisy_signal, noise_info = add_combined_noise(
    clean_signal, GAUSSIAN_SNR, IMPULSE_PROBABILITY, IMPULSE_AMPLITUDE
)

# -------------------------
# 4. Step 2: Apply channel distortions
# -------------------------
distorted_signal = apply_amplitude_distortion(
    noisy_signal, SAMPLE_RATE, AMPLITUDE_DISTORTION_FREQS, AMPLITUDE_DISTORTION_GAINS
)

distorted_signal = apply_phase_distortion(
    distorted_signal, SAMPLE_RATE, PHASE_DISTORTION_FREQS, PHASE_DISTORTION_SHIFTS
)

# -------------------------
# 5. Detection (Comprehensive)
# -------------------------
detection = detect_comprehensive(clean_signal, distorted_signal)

print("\n=== Detection Results ===")
print(detection)

# -------------------------
# 6. Filtering (Hybrid approach)
# -------------------------
# Step 1: remove impulse noise
filtered = median_filter(distorted_signal)

# Step 2: reduce gaussian noise
filtered = lowpass_filter(filtered, cutoff=15, fs=SAMPLE_RATE)

# -------------------------
# 7. Metrics
# -------------------------
metrics_before = calculate_all_metrics(clean_signal, distorted_signal)

metrics_after = calculate_all_metrics(clean_signal, filtered)

print("\n=== Metrics BEFORE ===")
print(metrics_before)

print("\n=== Metrics AFTER ===")
print(metrics_after)

# -------------------------
# 8. Visualization
# -------------------------
plot_time_signal(t, clean_signal, "Clean Signal")

plot_time_signal(t, distorted_signal, "Fully Corrupted Signal")

plot_time_signal(t, filtered, "Recovered Signal")

plot_fft(clean_signal, SAMPLE_RATE, "FFT - Clean Signal")

plot_fft(distorted_signal, SAMPLE_RATE, "FFT - Corrupted Signal")

plot_fft(filtered, SAMPLE_RATE, "FFT - Recovered Signal")

compare_signals(t, clean_signal, filtered)
