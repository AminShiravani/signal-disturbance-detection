import numpy as np


def calculate_snr(original, processed):

    signal_power = np.mean(original**2)

    noise_power = np.mean((original - processed) ** 2)

    if noise_power == 0:
        return np.inf

    return 10 * np.log10(signal_power / noise_power)


def calculate_mse(original, processed):

    return np.mean((original - processed) ** 2)


def calculate_rmse(original, processed):

    return np.sqrt(calculate_mse(original, processed))


def calculate_correlation(original, processed):

    return np.corrcoef(original, processed)[0, 1]


def calculate_all_metrics(original, processed):

    return {
        "SNR_dB": calculate_snr(original, processed),
        "MSE": calculate_mse(original, processed),
        "RMSE": calculate_rmse(original, processed),
        "Correlation": calculate_correlation(original, processed),
    }
