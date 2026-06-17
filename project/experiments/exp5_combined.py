import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import *
from signal_generator import generate_multitone
from noise_adder import add_combined_noise
from distortion import apply_amplitude_distortion, apply_phase_distortion
from filters import median_filter, lowpass_filter
from detectors import detect_comprehensive
from metrics import calculate_all_metrics
from plots import show_time_plots, show_fft_plots, compare_signals
from fft_analysis import spectral_snr, fft_gaussian_detector

# -------------------------
# 1. Time vector
# -------------------------
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

# -------------------------
# 2. Clean signal
# -------------------------
clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

# -------------------------
# 3. Add noise (channel impairment)
# -------------------------
corrupted_signal, _ = add_combined_noise(
    clean_signal, GAUSSIAN_SNR, IMPULSE_PROBABILITY, IMPULSE_AMPLITUDE
)

# -------------------------
# 4. Apply channel distortions
# -------------------------
distorted_signal = apply_amplitude_distortion(
    corrupted_signal,
    SAMPLE_RATE,
    AMPLITUDE_DISTORTION_FREQS,
    AMPLITUDE_DISTORTION_GAINS,
)

distorted_signal = apply_phase_distortion(
    distorted_signal, SAMPLE_RATE, PHASE_DISTORTION_FREQS, PHASE_DISTORTION_SHIFTS
)

# -------------------------
# 5. Detection stage
# -------------------------
detection = detect_comprehensive(clean_signal, distorted_signal)

print("\n=== Detection Result ===")
print(detection)

# -------------------------
# 6. Adaptive filtering (NO reconstruction)
# -------------------------
processed_signal = distorted_signal

# impulse noise handling
if detection.get("impulses_count", 0) > 0:
    processed_signal = median_filter(processed_signal)

# gaussian noise handling
if detection.get("is_gaussian", False):
    processed_signal = lowpass_filter(processed_signal, cutoff=15, fs=SAMPLE_RATE)

fft_det = fft_gaussian_detector(clean_signal, distorted_signal)
spec_snr = spectral_snr(clean_signal, distorted_signal)
print("\nFFT Detection:", fft_det)
print("Spectral SNR:", spec_snr)

# -------------------------
# 7. Metrics comparison
# -------------------------
before = calculate_all_metrics(clean_signal, distorted_signal)
after = calculate_all_metrics(clean_signal, processed_signal)

print("\n=== BEFORE ===")
print(before)

print("\n=== AFTER ===")
print(after)

# -------------------------
# 8. Visualization
# -------------------------
show_time_plots(
    "Experiment 5 - Adaptive DSP Disturbance Detection",
    [
        ("Clean Signal", t, clean_signal),
        ("Corrupted Signal", t, distorted_signal),
        ("Processed Signal", t, processed_signal),
    ],
)

show_fft_plots(
    "Frequency Domain Analysis",
    [clean_signal, distorted_signal, processed_signal],
    SAMPLE_RATE,
    ["Clean", "Corrupted", "Processed"],
)

compare_signals(t, clean_signal, processed_signal)
