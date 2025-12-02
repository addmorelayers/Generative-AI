import numpy as np
import plotly.express as px

def plot_distribution(samples: np.ndarray):
    """
    Plot 1D or 2D histograms using Plotly.
    """
    samples = np.asarray(samples)

    if samples.ndim == 1 or samples.shape[1] == 1:
        # 1D histogram
        fig = px.histogram(
            x=samples.flatten(),
            nbins=40,
            opacity=0.8,
            color_discrete_sequence=["#1f77b4"]
        )
    elif samples.shape[1] == 2:
        # 2D histogram (heatmap)
        fig = px.density_heatmap(
            x=samples[:, 0],
            y=samples[:, 1],
            nbinsx=40,
            nbinsy=40,
            color_continuous_scale="Blues"
        )
    else:
        raise ValueError("plot_distribution supports only 1D or 2D samples")

    fig.update_layout(
        template="simple_white",
        width=600,
        height=450,
        title=None,
        xaxis_title=None,
        yaxis_title=None
    )
    fig.show()

