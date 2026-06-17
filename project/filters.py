import numpy as np


# Median Filter (improved)
def median_filter(signal, kernel_size=5):
    padded = np.pad(signal, kernel_size // 2, mode="edge")
    filtered = []

    for i in range(len(signal)):
        window = padded[i : i + kernel_size]
        filtered.append(np.median(window))

    return np.array(filtered)


# Low-pass filter (FFT based - better than simple)
def lowpass_filter(signal, cutoff, fs):
    fft = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1 / fs)

    fft[np.abs(freqs) > cutoff] = 0

    return np.real(np.fft.ifft(fft))


# Adaptive correction for amplitude distortion
def amplitude_correction(signal, gain_estimate=1.0):
    return signal / gain_estimate
