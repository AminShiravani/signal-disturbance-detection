import numpy as np


def apply_amplitude_distortion(signal, fs, frequencies, gains):

    spectrum = np.fft.fft(signal)

    freq_axis = np.fft.fftfreq(len(signal), 1 / fs)

    for f, g in zip(frequencies, gains):

        idx = np.argmin(np.abs(freq_axis - f))

        spectrum[idx] *= g
        spectrum[-idx] *= g

    distorted = np.fft.ifft(spectrum).real

    return distorted


def apply_phase_distortion(signal, fs, frequencies, shifts):

    spectrum = np.fft.fft(signal)

    freq_axis = np.fft.fftfreq(len(signal), 1 / fs)

    for f, shift in zip(frequencies, shifts):

        idx = np.argmin(np.abs(freq_axis - f))

        magnitude = np.abs(spectrum[idx])

        phase = np.angle(spectrum[idx])

        spectrum[idx] = magnitude * np.exp(1j * (phase + shift))

        spectrum[-idx] = np.conj(spectrum[idx])

    distorted = np.fft.ifft(spectrum).real

    return distorted
