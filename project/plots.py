import matplotlib.pyplot as plt
import numpy as np


def plot_time_signal(t, signal, title="Signal"):
    plt.figure(figsize=(10, 3))
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


def plot_fft(signal, fs, title="FFT"):
    N = len(signal)
    freq = np.fft.fftfreq(N, 1 / fs)
    spectrum = np.abs(np.fft.fft(signal))

    plt.figure(figsize=(10, 3))
    plt.plot(freq[: N // 2], spectrum[: N // 2])
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()


def plot_noise_locations(signal, locations, title="Impulse Detection"):
    plt.figure(figsize=(10, 3))
    plt.plot(signal)
    plt.scatter(np.where(locations)[0], signal[locations], color="red")
    plt.title(title)
    plt.grid()
    plt.show()


def compare_signals(t, original, processed):
    plt.figure(figsize=(10, 4))
    plt.plot(t, original, label="Original")
    plt.plot(t, processed, label="Processed", alpha=0.7)
    plt.legend()
    plt.title("Comparison")
    plt.grid()
    plt.show()
