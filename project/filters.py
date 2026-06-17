from scipy.signal import butter
from scipy.signal import filtfilt
from scipy.signal import medfilt


def lowpass_filter(signal, cutoff, fs, order=4):

    nyquist = fs / 2

    normalized = cutoff / nyquist

    b, a = butter(order, normalized, btype="low")

    return filtfilt(b, a, signal)


def median_filter(signal, kernel_size=5):

    if kernel_size % 2 == 0:
        kernel_size += 1

    return medfilt(signal, kernel_size)
