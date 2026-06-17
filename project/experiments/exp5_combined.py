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

t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

noisy_signal, _ = add_combined_noise(
    clean_signal, GAUSSIAN_SNR, IMPULSE_PROBABILITY, IMPULSE_AMPLITUDE
)

distorted = apply_amplitude_distortion(
    noisy_signal, SAMPLE_RATE, AMPLITUDE_DISTORTION_FREQS, AMPLITUDE_DISTORTION_GAINS
)

distorted = apply_phase_distortion(
    distorted, SAMPLE_RATE, PHASE_DISTORTION_FREQS, PHASE_DISTORTION_SHIFTS
)

# Detection
detection = detect_comprehensive(clean_signal, distorted)
print("Detection:", detection)

# FIX PIPELINE (Adaptive)
signal = distorted

if detection["impulses_count"] > 0:
    signal = median_filter(signal)

if detection["is_gaussian"]:
    signal = lowpass_filter(signal, 15, SAMPLE_RATE)

# Metrics
before = calculate_all_metrics(clean_signal, distorted)
after = calculate_all_metrics(clean_signal, signal)

print("BEFORE:", before)
print("AFTER:", after)

show_time_plots(
    "Combined Distortion (FULL SYSTEM)",
    [
        ("Clean", t, clean_signal),
        ("Corrupted", t, distorted),
        ("Recovered", t, signal),
    ],
)

show_fft_plots(
    "FFT Comparison",
    [clean_signal, distorted, signal],
    SAMPLE_RATE,
    ["Clean", "Corrupted", "Recovered"],
)

compare_signals(t, clean_signal, signal)
