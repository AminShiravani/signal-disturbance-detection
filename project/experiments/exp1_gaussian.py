import os
import sys
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import *
from signal_generator import generate_multitone
from noise_adder import add_gaussian_noise
from filters import lowpass_filter
from metrics import calculate_all_metrics
from detectors import detect_gaussian_noise
from fft_analysis import spectral_snr, fft_gaussian_detector
from plots import plot_time_signal, plot_fft, compare_signals

t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

clean = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

noisy, _, snr = add_gaussian_noise(clean, GAUSSIAN_SNR)

print("TIME SNR:", snr)

# ---------------- FFT detection ----------------
fft_result = fft_gaussian_detector(clean, noisy)
spec_snr = spectral_snr(clean, noisy)

print("\nFFT Detection:", fft_result)
print("Spectral SNR:", spec_snr)

# ---------------- time detection ----------------
time_det = detect_gaussian_noise(clean, noisy)
print("\nTime Detection:", time_det)

# ---------------- filtering ----------------
filtered = lowpass_filter(noisy, 15, SAMPLE_RATE)

before = calculate_all_metrics(clean, noisy)
after = calculate_all_metrics(clean, filtered)

print("\nBEFORE:", before)
print("AFTER:", after)

# ---------------- plots ----------------
plot_time_signal(t, clean, "Clean")
plot_time_signal(t, noisy, "Noisy")
plot_time_signal(t, filtered, "Filtered")

plot_fft(clean, SAMPLE_RATE, "FFT Clean")
plot_fft(noisy, SAMPLE_RATE, "FFT Noisy")

compare_signals(t, clean, filtered)
