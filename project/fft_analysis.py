import numpy as np


# ----------------------------
# Spectral SNR
# ----------------------------
def spectral_snr(clean, noisy):
    clean_fft = np.fft.fft(clean)
    noisy_fft = np.fft.fft(noisy)

    signal_power = np.mean(np.abs(clean_fft) ** 2)
    noise_power = np.mean(np.abs(noisy_fft - clean_fft) ** 2)

    return 10 * np.log10(signal_power / (noise_power + 1e-12))


# ----------------------------
# FFT-based Gaussian detection
# ----------------------------
def fft_gaussian_detector(clean, noisy):
    clean_fft = np.fft.fft(clean)
    noisy_fft = np.fft.fft(noisy)

    # normalization (IMPORTANT FIX)
    diff = np.abs(noisy_fft - clean_fft)
    denom = np.abs(clean_fft) + 1e-12

    deviation = np.mean(diff / denom)

    is_noisy = deviation > 0.5

    return {"spectral_deviation": float(deviation), "is_noisy_fft": bool(is_noisy)}
