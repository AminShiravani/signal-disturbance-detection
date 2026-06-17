import numpy as np


# -------------------------
# Median Filter
# -------------------------
def median_filter(signal, kernel_size=5):
    padded = np.pad(signal, kernel_size // 2, mode="edge")
    result = []

    for i in range(len(signal)):
        window = padded[i : i + kernel_size]
        result.append(np.median(window))

    return np.array(result)


# -------------------------
# Low-pass Filter (FFT based)
# -------------------------
def lowpass_filter(signal, cutoff, fs):
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1 / fs)

    fft[np.abs(freqs) > cutoff] = 0

    return np.real(np.fft.ifft(fft))

