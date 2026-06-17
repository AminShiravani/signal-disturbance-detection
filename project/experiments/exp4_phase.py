import numpy as np

from config import (
    SAMPLE_RATE,
    DURATION,
    FREQUENCIES,
    AMPLITUDES,
    PHASES,
    PHASE_DISTORTION_FREQS,
    PHASE_DISTORTION_SHIFTS,
)

from signal_generator import generate_multitone
from distortion import apply_phase_distortion
from metrics import calculate_all_metrics
from detectors import detect_phase_distortion
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
# 3. Apply phase distortion
# -------------------------
distorted_signal = apply_phase_distortion(
    clean_signal, SAMPLE_RATE, PHASE_DISTORTION_FREQS, PHASE_DISTORTION_SHIFTS
)

# -------------------------
# 4. Detection
# -------------------------
detection = detect_phase_distortion(clean_signal, distorted_signal)

print("\nPhase Distortion Detection:")
print(detection)

# -------------------------
# 5. Metrics
# -------------------------
metrics = calculate_all_metrics(clean_signal, distorted_signal)

print("\nMetrics:")
print(metrics)

# -------------------------
# 6. Plots
# -------------------------
plot_time_signal(t, clean_signal, "Clean Signal")

plot_time_signal(t, distorted_signal, "Phase Distorted Signal")

plot_fft(clean_signal, SAMPLE_RATE, "FFT - Clean Signal")
plot_fft(distorted_signal, SAMPLE_RATE, "FFT - Phase Distorted Signal")

compare_signals(t, clean_signal, distorted_signal)
