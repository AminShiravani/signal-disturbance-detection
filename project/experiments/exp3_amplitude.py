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
    AMPLITUDE_DISTORTION_FREQS,
    AMPLITUDE_DISTORTION_GAINS,
)

from signal_generator import generate_multitone
from distortion import apply_amplitude_distortion
from metrics import calculate_all_metrics
from detectors import detect_amplitude_distortion
from plots import show_time_plots, show_fft_plots, compare_signals
from fft_analysis import spectral_snr

t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)

clean_signal = generate_multitone(t, FREQUENCIES, AMPLITUDES, PHASES)

distorted_signal = apply_amplitude_distortion(
    clean_signal, SAMPLE_RATE, AMPLITUDE_DISTORTION_FREQS, AMPLITUDE_DISTORTION_GAINS
)

detection = detect_amplitude_distortion(clean_signal, distorted_signal)
print("Detection:", detection)

before = calculate_all_metrics(clean_signal, distorted_signal)
print("Metrics:", before)

spec_snr = spectral_snr(clean_signal, distorted_signal)
print("Spectral SNR:", spec_snr)

show_time_plots(
    "Amplitude Distortion",
    [
        ("Clean", t, clean_signal),
        ("Distorted", t, distorted_signal),
    ],
)

show_fft_plots(
    "FFT Comparison",
    [clean_signal, distorted_signal],
    SAMPLE_RATE,
    ["Clean", "Distorted"],
)

compare_signals(t, clean_signal, distorted_signal)
