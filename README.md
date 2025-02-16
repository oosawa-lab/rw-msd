# rw-msd
Random Walk with Diffusion Coefficient Calculation

This repository contains code for simulating a 2D random walk, calculating the Mean Squared Displacement (MSD), and estimating the diffusion coefficient. 
The simulation generates random walk trajectories, computes MSD as a function of time lag, and uses a log-log plot to estimate the diffusion coefficient.

Features

Simulates a 2D random walk with normally distributed step lengths.
Calculates the Mean Squared Displacement (MSD) as a function of time lag.
Computes the diffusion coefficient from the slope of the MSD vs time lag plot.
Visualizes the random walk trajectory and the MSD in log-log scale.
Requirements

This project requires the following Python packages:

numpy (for mathematical operations and random number generation)
matplotlib (for plotting)

How to Use

1. Run the Script
To run the script, open a terminal and navigate to the directory where the script is located. Then run the following command, specifying the number of steps for the random walk:

python3 random_walk_with_diffusion.py <steps>
For example, to run with 1000 steps:

python3 random_walk_with_diffusion.py 1000

2. Output
After running the script, you will see the following output:

A random walk trajectory will be plotted on the left side.
The MSD vs time lag (log-log plot) will be displayed on the right side.
The calculated diffusion coefficient and slope of the MSD log-log plot will be printed in the terminal.

License

This project is licensed under the MIT License. See the LICENSE file for more information.
