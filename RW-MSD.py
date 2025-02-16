# -----------------------------------------------------------------------------
# Copyright (c) 2025 Chikoo Oosawa, Kyushu Institute of Technology
#
# This project is licensed under the MIT License.
# You can find the full license at: https://opensource.org/licenses/MIT
#
# Repository: https://github.com/oosawa-lab/inter-Kuramoto-inhomo/
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import sys

def generate_random_walk(steps=1000):
    """
    Generate coordinates for a random walk with normally distributed step lengths.
    :param steps: Number of steps
    :return: x and y coordinates
    """
    x_steps = np.random.normal(0, 1, size=steps)  # Normally distributed steps for x
    y_steps = np.random.normal(0, 1, size=steps)  # Normally distributed steps for y

    x = np.cumsum(x_steps)  # Cumulative sum to get x coordinates
    y = np.cumsum(y_steps)  # Cumulative sum to get y coordinates

    return x, y

def calculate_msd(x, y, max_lag=None):
    """
    Calculate the mean squared displacement (MSD) as a function of time lag.
    :param x: x coordinates
    :param y: y coordinates
    :param max_lag: Maximum time lag to calculate MSD
    :return: Time lags and corresponding MSD values
    """
    if max_lag is None:
        max_lag = len(x) // 2  # Default to half the total steps

    lags = np.arange(1, max_lag + 1)
    msd = np.zeros_like(lags, dtype=float)

    for lag in lags:
        dx = x[lag:] - x[:-lag]
        dy = y[lag:] - y[:-lag]
        msd[lag - 1] = np.mean(dx**2 + dy**2)

    return lags, msd

def calculate_diffusion_coefficient(lags, msd):
    """
    Calculate the diffusion coefficient from the slope of the MSD vs time.
    :param lags: Time lags
    :param msd: MSD values
    :return: Diffusion coefficient
    """
    log_lags = np.log(lags)
    log_msd = np.log(msd)

    coeffs = np.polyfit(log_lags, log_msd, 1)  # Linear fit to log-log data
    slope = coeffs[0]
    diffusion_coefficient = np.exp(coeffs[1]) / 4  # Adjusted for 2D diffusion
    return diffusion_coefficient, slope, coeffs

def plot_msd_loglog(lags, msd, coeffs):
    """
    Plot the MSD as a function of time lag on a log-log scale.
    :param lags: Time lags
    :param msd: MSD values
    :param coeffs: Linear fit coefficients for log-log MSD vs time
    """
    plt.loglog(lags, msd, 'o-', label="MSD")
    plt.loglog(lags, np.exp(np.polyval(coeffs, np.log(lags))), 'r--', label=f"Linear Fit (Slope={coeffs[0]:.2f})")
    plt.xlabel("Log(Time Lag)")
    plt.ylabel("Log(MSD)")
    plt.title("MSD vs Time Lag (Log-Log Plot)")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

if __name__ == "__main__":
    # Check for command-line arguments (steps)
    if len(sys.argv) != 2:
        print("Usage: python3 random_walk_with_diffusion.py <steps>")
        sys.exit(1)

    steps = int(sys.argv[1])  # Get number of steps from command-line argument

    # Generate a random walk
    x, y = generate_random_walk(steps)

    # Create a figure with two subplots (side by side)
    fig, ax = plt.subplots(1, 2, figsize=(16, 8))  # 1 row, 2 columns

    # Left subplot: Random Walk Trajectory
    ax[0].plot(x, y, marker='o', markersize=2, label="Random Walk Trajectory")
    ax[0].scatter(x[0], y[0], color="green", label="Start Point", zorder=5)
    ax[0].scatter(x[-1], y[-1], color="red", label="End Point", zorder=5)
    ax[0].set_title("Random Walk Trajectory")
    ax[0].set_xlabel("X Coordinate")
    ax[0].set_ylabel("Y Coordinate")
    ax[0].legend()
    ax[0].grid(True)
    ax[0].axis("equal")

    # Calculate and display the MSD and diffusion coefficient
    lags, msd = calculate_msd(x, y)
    diffusion_coefficient, slope, coeffs = calculate_diffusion_coefficient(lags, msd)
    print(f"Diffusion Coefficient: {diffusion_coefficient:.2f}")
    print(f"Slope of log-log MSD plot: {slope:.2f}")

    # Right subplot: MSD vs Time Lag (log-log scale)
    plot_msd_loglog(lags, msd, coeffs)
    ax[1].set_title("MSD vs Time Lag (Log-Log Plot)")
    ax[1].set_xlabel("Log(Time Lag)")
    ax[1].set_ylabel("Log(MSD)")

    # Show both plots
    plt.tight_layout()
    plt.show()
    
    





    
    
    
