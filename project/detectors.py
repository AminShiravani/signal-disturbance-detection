import numpy as np


# -------------------------
# Gaussian Noise Detection (SNR-based)
# -------------------------
def detect_gaussian_noise(clean, noisy):
    noise = noisy - clean
    noise_power = np.mean(noise**2)
    signal_power = np.mean(clean**2)
    snr = 10 * np.log10(signal_power / noise_power)

    return {"noise_power": noise_power, "estimated_snr": snr, "is_noisy": snr < 15}


# -------------------------
# Impulse Detection (robust z-score)
# -------------------------
def detect_impulses(signal):
    median = np.median(signal)
    mad = np.median(np.abs(signal - median))

    threshold = 3 * mad
    impulses = np.abs(signal - median) > threshold

    return impulses


# -------------------------
# Amplitude Distortion (spectral energy shift)
# -------------------------
def detect_amplitude_distortion(clean, distorted):
    c_fft = np.abs(np.fft.fft(clean))
    d_fft = np.abs(np.fft.fft(distorted))

    diff = np.mean(np.abs(c_fft - d_fft)) / np.mean(c_fft)

    return {"spectral_distortion": diff, "is_distorted": diff > 0.2}


# -------------------------
# Phase Distortion
# -------------------------
def detect_phase_distortion(clean, distorted, threshold=0.1):
    """
    Real phase distortion detection using FFT phase difference
    """

    clean_fft = np.fft.fft(clean)
    dist_fft = np.fft.fft(distorted)

    clean_phase = np.angle(clean_fft)
    dist_phase = np.angle(dist_fft)

    phase_diff = np.mean(np.abs(clean_phase - dist_phase))

    is_distorted = phase_diff > threshold

    return {"phase_error": float(phase_diff), "is_distorted": bool(is_distorted)}


# -------------------------
# Combined detection (NEW INTELLIGENT LAYER)
# -------------------------
def detect_comprehensive(clean, signal):

    gauss = detect_gaussian_noise(clean, signal)
    impulses = detect_impulses(signal)
    amp = detect_amplitude_distortion(clean, signal)
    phase = detect_phase_distortion(clean, signal)

    return {
        "impulses_count": int(np.sum(impulses)),
        "is_gaussian": gauss["is_noisy"],
        "snr_est": gauss["estimated_snr"],
        "amplitude_issue": amp["is_distorted"],
        "phase_issue": phase["is_distorted"],
    }
