import numpy as np
from scipy.stats import zscore


def detect_impulses(signal, threshold=3):
    """
    Detecting spikes with Z-score
    """

    z = np.abs(zscore(signal))
    impulses = z > threshold
    return impulses


def detect_gaussian_noise(original, noisy):
    """
    Estimation of the existence of Gaussian noise with energy difference
    """

    noise = noisy - original
    noise_power = np.mean(noise**2)
    signal_power = np.mean(original**2)

    snr_est = 10 * np.log10(signal_power / (noise_power + 1e-12))

    return {
        "noise_power": noise_power,
        "estimated_snr": snr_est,
        "is_noisy": snr_est < 20,
    }


def detect_amplitude_distortion(original, processed):
    """
    Checking spectral shift for amplitude distortion
    """

    O = np.abs(np.fft.fft(original))
    P = np.abs(np.fft.fft(processed))

    distortion = np.mean(np.abs(O - P))

    return {
        "spectral_distortion": distortion,
        "is_distorted": distortion > 0.1 * np.mean(O),
    }


def detect_phase_distortion(original, processed):
    """
    Checking the phase difference
    """

    O = np.angle(np.fft.fft(original))
    P = np.angle(np.fft.fft(processed))

    phase_error = np.mean(np.abs(O - P))

    return {"phase_error": phase_error, "is_distorted": phase_error > 0.5}


def detect_comprehensive(original, signal):
    """
    Combined diagnosis
    """

    impulse = detect_impulses(signal)
    gaussian = detect_gaussian_noise(original, signal)

    return {
        "impulses_count": np.sum(impulse),
        "is_gaussian": gaussian["is_noisy"],
        "snr_est": gaussian["estimated_snr"],
    }
