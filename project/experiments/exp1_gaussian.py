import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np

from config import SAMPLE_RATE, DURATION, FREQUENCIES, AMPLITUDES, PHASES, GAUSSIAN_SNR

from signal_generator import generate_multitone
from noise_adder import add_gaussian_noise
from filters import lowpass_filter
from metrics import calculate_all_metrics
from detectors import detect_gaussian_noise
from plots import plot_time_signal, plot_fft, compare_signals

# -------------------------
# 1. Time vector
# -------------------------
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

# -------------------------
# 2. Generate clean signal
# -------------------------
clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

# -------------------------
# 3. Add Gaussian noise
# -------------------------
noisy_signal, noise, snr = add_gaussian_noise(clean_signal, GAUSSIAN_SNR)

print(f"Input SNR: {snr:.2f} dB")

# -------------------------
# 4. Detection
# -------------------------
detection = detect_gaussian_noise(clean_signal, noisy_signal)

print("\nDetection Result:")
print(detection)

# -------------------------
# 5. Filtering
# -------------------------
filtered_signal = lowpass_filter(noisy_signal, cutoff=15, fs=SAMPLE_RATE)

# -------------------------
# 6. Metrics
# -------------------------
metrics_before = calculate_all_metrics(clean_signal, noisy_signal)

metrics_after = calculate_all_metrics(clean_signal, filtered_signal)

print("\nMetrics BEFORE filtering:")
print(metrics_before)

print("\nMetrics AFTER filtering:")
print(metrics_after)

# -------------------------
# 7. Plots (Report Figures)
# -------------------------
plot_time_signal(t, clean_signal, "Clean Signal")
plot_time_signal(t, noisy_signal, "Noisy Signal (Gaussian)")
plot_time_signal(t, filtered_signal, "Filtered Signal")

plot_fft(clean_signal, SAMPLE_RATE, "FFT - Clean Signal")
plot_fft(noisy_signal, SAMPLE_RATE, "FFT - Noisy Signal")

compare_signals(t, clean_signal, filtered_signal)
