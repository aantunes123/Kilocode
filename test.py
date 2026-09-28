# Alexandre Antunes 09/2026
import numpy as np
from matplotlib import pyplot as plt

import config


def plot_quadratic(
    x_start: float = config.X_START,
    x_end: float = config.X_END,
    step: float = config.X_STEP,
    power: float = config.POWER,
    title: str = config.TITLE,
    xlabel: str = config.X_LABEL,
    ylabel: str = config.Y_LABEL,
    show_grid: bool = config.SHOW_GRID,
) -> None:
    """Plot y = x^power over a specified range.
    
    Args:
        x_start: Starting x value (inclusive)
        x_end: Ending x value (exclusive)
        step: Step size for x values
        power: Exponent for the power function
        title: Plot title
        xlabel: X-axis label
        ylabel: Y-axis label
        show_grid: Whether to display grid lines
    """
    x = np.arange(x_start, x_end, step)
    y = np.power(x, power)

    plt.figure(figsize=(config.FIGURE_WIDTH, config.FIGURE_HEIGHT))
    plt.plot(x, y, f"{config.LINE_COLOR}{config.LINE_STYLE}", 
             linewidth=config.LINE_WIDTH, label=f"y = x^{power}")
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    
    # Set y-axis limits if configured
    if config.Y_MIN is not None or config.Y_MAX is not None:
        plt.ylim(config.Y_MIN, config.Y_MAX)
    
    if show_grid:
        plt.grid(True, alpha=config.GRID_ALPHA)
    
    plt.legend(fontsize=11)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_quadratic()
