import numpy as np


def generate_sinusoid(t, freq, amp=1.0, phase=0):
    return amp * np.sin(2 * np.pi * freq * t + phase)


def generate_multitone(t, frequencies, amplitudes, phases):

    signal = np.zeros_like(t)

    for f, a, p in zip(frequencies, amplitudes, phases):

        signal += generate_sinusoid(t, f, a, p)

    return signal


def generate_test_signal(t):

    signal = (
        1.0 * np.sin(2 * np.pi * 5 * t)
        + 0.6 * np.sin(2 * np.pi * 12 * t + np.pi / 4)
        + 0.3 * np.sin(2 * np.pi * 25 * t + np.pi / 3)
    )

    return signal
