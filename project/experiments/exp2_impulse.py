import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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
from plots import show_time_plots, show_fft_plots, compare_signals

t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

noisy_signal, impulse_locations = add_impulse_noise(
    clean_signal, IMPULSE_PROBABILITY, IMPULSE_AMPLITUDE
)

print("Impulses:", np.sum(impulse_locations))

detected = detect_impulses(noisy_signal)
print("Detected:", np.sum(detected))

# Fix
filtered_signal = median_filter(noisy_signal)

before = calculate_all_metrics(clean_signal, noisy_signal)
after = calculate_all_metrics(clean_signal, filtered_signal)

print("BEFORE:", before)
print("AFTER:", after)

show_time_plots(
    "Impulse Noise Analysis",
    [
        ("Clean", t, clean_signal),
        ("Impulse Noisy", t, noisy_signal),
        ("Filtered (Median)", t, filtered_signal),
    ],
)

show_fft_plots(
    "FFT Comparison", [clean_signal, noisy_signal], SAMPLE_RATE, ["Clean", "Impulse"]
)

compare_signals(t, clean_signal, filtered_signal)
