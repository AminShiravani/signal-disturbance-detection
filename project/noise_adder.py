import numpy as np


def add_gaussian_noise(signal, snr_db):

    signal_power = np.mean(signal**2)

    snr_linear = 10 ** (snr_db / 10)

    noise_power = signal_power / snr_linear

    noise = np.random.normal(0, np.sqrt(noise_power), len(signal))

    noisy_signal = signal + noise

    actual_snr = 10 * np.log10(np.mean(signal**2) / np.mean(noise**2))

    return noisy_signal, noise, actual_snr


def add_impulse_noise(signal, probability, amplitude):

    noisy = signal.copy()

    impulse_locations = np.random.rand(len(signal)) < probability

    impulses = amplitude * np.random.choice([-1, 1], size=np.sum(impulse_locations))

    noisy[impulse_locations] += impulses

    return noisy, impulse_locations


def add_combined_noise(signal, snr_db, probability, amplitude):

    gaussian_signal, gaussian_noise, snr = add_gaussian_noise(signal, snr_db)

    combined_signal, impulse_locations = add_impulse_noise(
        gaussian_signal, probability, amplitude
    )

    info = {
        "gaussian_noise": gaussian_noise,
        "impulse_locations": impulse_locations,
        "actual_snr": snr,
    }

    return combined_signal, info
