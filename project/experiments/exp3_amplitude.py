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
    AMPLITUDE_DISTORTION_FREQS,
    AMPLITUDE_DISTORTION_GAINS,
)

from signal_generator import generate_multitone
from distortion import apply_amplitude_distortion
from metrics import calculate_all_metrics
from detectors import detect_amplitude_distortion
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
# 3. Apply amplitude distortion (Channel effect)
# -------------------------
distorted_signal = apply_amplitude_distortion(
    clean_signal, SAMPLE_RATE, AMPLITUDE_DISTORTION_FREQS, AMPLITUDE_DISTORTION_GAINS
)

# -------------------------
# 4. Detection
# -------------------------
detection = detect_amplitude_distortion(clean_signal, distorted_signal)

print("\nAmplitude Distortion Detection:")
print(detection)

# -------------------------
# 5. Metrics
# -------------------------
metrics = calculate_all_metrics(clean_signal, distorted_signal)

print("\nMetrics:")
print(metrics)

# -------------------------
# 6. Plots (VERY important for report)
# -------------------------
plot_time_signal(t, clean_signal, "Clean Signal")

plot_time_signal(t, distorted_signal, "Amplitude Distorted Signal")

plot_fft(clean_signal, SAMPLE_RATE, "FFT - Clean Signal")
plot_fft(distorted_signal, SAMPLE_RATE, "FFT - Distorted Signal")

compare_signals(t, clean_signal, distorted_signal)
