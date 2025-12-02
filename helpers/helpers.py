import numpy as np
import matplotlib.pyplot as plt

def plot_distribution(samples: np.ndarray):
    """
    Plot the distribution of sampled data.
    - If samples are 1D: show histogram.
    - If samples are 2D: show scatter plot.
    """
    samples = np.asarray(samples)

    plt.figure(figsize=(6, 4))

    if samples.ndim == 1 or samples.shape[1] == 1:
        # 1D samples → histogram
        plt.hist(samples, bins=30, density=True, color="#1f77b4", alpha=0.7, edgecolor="white")
    elif samples.shape[1] == 2:
        # 2D samples → scatter
        plt.scatter(samples[:, 0], samples[:, 1], s=25, color="#1f77b4", alpha=0.75, edgecolors="white", linewidth=0.5)
    else:
        raise ValueError("plot_distribution only supports 1D or 2D samples")

    plt.grid(alpha=0.2)
    plt.tight_layout()
    plt.show()

