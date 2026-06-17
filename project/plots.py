import matplotlib.pyplot as plt
import numpy as np


# -------------------------
# Time domain plots (MAIN FIX)
# -------------------------
def show_time_plots(title, plots):
    plt.figure(figsize=(12, 3 * len(plots)))
    plt.suptitle(title)

    for i, (name, t, y) in enumerate(plots, 1):
        plt.subplot(len(plots), 1, i)
        plt.plot(t, y)
        plt.title(name)
        plt.grid()

    plt.tight_layout()
    plt.show()


# -------------------------
# FFT comparison
# -------------------------
def show_fft_plots(title, signals, fs, labels):
    plt.figure(figsize=(12, 4))

    for sig, label in zip(signals, labels):
        N = len(sig)
        f = np.fft.fftfreq(N, 1 / fs)
        X = np.abs(np.fft.fft(sig))

        plt.plot(f[: N // 2], X[: N // 2], label=label)

    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()


# -------------------------
# Compare signal
# -------------------------
def compare_signals(t, original, processed):
    plt.figure(figsize=(10, 4))
    plt.plot(t, original, label="Original")
    plt.plot(t, processed, label="Processed")
    plt.legend()
    plt.title("Comparison")
    plt.grid()
    plt.show()
