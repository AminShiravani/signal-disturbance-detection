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
    IMPULSE_PROBABILITY,
    IMPULSE_AMPLITUDE,
)

from signal_generator import generate_multitone
from noise_adder import add_impulse_noise
from filters import median_filter
from metrics import calculate_all_metrics
from detectors import detect_impulses
from plots import plot_time_signal, plot_fft, plot_noise_locations, compare_signals

# -------------------------
# 1. Time vector
# -------------------------
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

# -------------------------
# 2. Clean signal
# -------------------------
clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

# -------------------------
# 3. Add impulse noise
# -------------------------
noisy_signal, impulse_locations = add_impulse_noise(
    clean_signal, IMPULSE_PROBABILITY, IMPULSE_AMPLITUDE
)

print(f"Number of impulses: {np.sum(impulse_locations)}")

# -------------------------
# 4. Detection
# -------------------------
detected_impulses = detect_impulses(noisy_signal)

print(f"Detected impulses: {np.sum(detected_impulses)}")

# -------------------------
# 5. Filtering (Median filter best choice for impulse noise)
# -------------------------
filtered_signal = median_filter(noisy_signal, kernel_size=5)

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
# 7. Plots (very important for report)
# -------------------------
plot_time_signal(t, clean_signal, "Clean Signal")
plot_time_signal(t, noisy_signal, "Impulse Noisy Signal")
plot_time_signal(t, filtered_signal, "Filtered Signal (Median)")

plot_fft(clean_signal, SAMPLE_RATE, "FFT - Clean Signal")
plot_fft(noisy_signal, SAMPLE_RATE, "FFT - Impulse Noise")

plot_noise_locations(noisy_signal, impulse_locations, "True Impulses (Ground Truth)")

plot_noise_locations(noisy_signal, detected_impulses, "Detected Impulses (Z-score)")

compare_signals(t, clean_signal, filtered_signal)
