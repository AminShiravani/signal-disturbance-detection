import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import SAMPLE_RATE, DURATION, FREQUENCIES, AMPLITUDES, PHASES, GAUSSIAN_SNR

from signal_generator import generate_multitone
from noise_adder import add_gaussian_noise
from filters import lowpass_filter
from metrics import calculate_all_metrics
from detectors import detect_gaussian_noise
from plots import show_time_plots, show_fft_plots, compare_signals

# -------------------------
# 1. Time
# -------------------------
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

# -------------------------
# 2. Clean signal
# -------------------------
clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

# -------------------------
# 3. Noise
# -------------------------
noisy_signal, noise, snr = add_gaussian_noise(clean_signal, GAUSSIAN_SNR)

print("Input SNR:", snr)

# -------------------------
# 4. Detection
# -------------------------
detection = detect_gaussian_noise(clean_signal, noisy_signal)
print("Detection:", detection)

# -------------------------
# 5. Fix (Filter)
# -------------------------
filtered_signal = lowpass_filter(noisy_signal, cutoff=15, fs=SAMPLE_RATE)

# -------------------------
# 6. Metrics
# -------------------------
before = calculate_all_metrics(clean_signal, noisy_signal)
after = calculate_all_metrics(clean_signal, filtered_signal)

print("BEFORE:", before)
print("AFTER:", after)

# -------------------------
# 7. Visualization
# -------------------------
show_time_plots(
    "Gaussian Noise Analysis",
    [
        ("Clean", t, clean_signal),
        ("Noisy", t, noisy_signal),
        ("Filtered", t, filtered_signal),
    ],
)

show_fft_plots(
    "FFT Comparison", [clean_signal, noisy_signal], SAMPLE_RATE, ["Clean", "Noisy"]
)

compare_signals(t, clean_signal, filtered_signal)
