import matplotlib.pyplot as plt
import numpy as np


# ----------------------------
# Time plot (single)
# ----------------------------
def plot_time_signal(t, signal, title="Signal"):
    plt.figure()
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


# ----------------------------
# FFT plot (single)
# ----------------------------
def plot_fft(signal, fs, title="FFT"):
    n = len(signal)
    freq = np.fft.fftfreq(n, 1 / fs)
    spectrum = np.abs(np.fft.fft(signal))

    plt.figure()
    plt.plot(freq[: n // 2], spectrum[: n // 2])
    plt.title(title)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.grid()
    plt.show()


# ----------------------------
# Compare signals
# ----------------------------
def compare_signals(t, clean, processed):
    plt.figure()
    plt.plot(t, clean, label="Clean")
    plt.plot(t, processed, label="Processed")
    plt.legend()
    plt.title("Comparison")
    plt.grid()
    plt.show()


# ----------------------------
# multi-signal time plot
# ----------------------------
def show_time_plots(title, signals):
    plt.figure()
    for label, t, sig in signals:
        plt.plot(t, sig, label=label)

    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid()
    plt.show()


# ----------------------------
# multi FFT plot
# ----------------------------
def show_fft_plots(title, signals, fs, labels):
    plt.figure()

    for sig, label in zip(signals, labels):
        n = len(sig)
        freq = np.fft.fftfreq(n, 1 / fs)
        spectrum = np.abs(np.fft.fft(sig))
        plt.plot(freq[: n // 2], spectrum[: n // 2], label=label)

    plt.title(title)
    plt.xlabel("Frequency")
    plt.ylabel("Magnitude")
    plt.legend()
    plt.grid()
    plt.show()
