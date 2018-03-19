# Load packages
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# Set some global settings for the plots
mpl.rc(('axes', 'xtick', 'ytick'), labelsize='small')
mpl.rcParams['axes.titleweight'] = 'bold'
mpl.rcParams['axes.grid'] = True
mpl.rcParams['grid.alpha'] = 0.2

# Define a function that illustrates the law of large numbers
def simulation(nmax, mu, sigma, interactive=False):
    # Initialize plot
    plt.title('Simulation: Convergence of sample mean')
    plt.xlabel('Sample Size')
    plt.ylabel('Sample Mean')
    plt.axis([0, nmax, -1.65*sigma, 1.65*sigma])
    plt.hlines(mu, 0, nmax, color = 'darkred', label = 'Theoretical mean')
    # Initialize lists
    sample = []
    means = []
    # Start of the simulation
    for n in range(1, nmax):
        # Append sample by iid new observation
        sample.append(np.random.normal(mu, sigma))
        # Recalculate the sample mean
        means.append(np.mean(sample))
    plt.plot(means, color = 'darkblue', label = 'Sample averages')
    plt.legend()
    plt.show()

# Tryin
simulation(10000, 0, 10)