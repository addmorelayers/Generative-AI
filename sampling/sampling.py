import numpy as np


def sample_1(n_points: int) -> np.ndarray:
    """
    Sample from distribution 1.

    Parameters
    ----------
    n_points : int
        Number of data points to generate.

    Returns
    -------
    np.ndarray
        Array of samples drawn from the distribution.
    """
    hidden_mean = 37.2
    hidden_std = 1.3
    return np.random.normal(hidden_mean, hidden_std, n_points)


