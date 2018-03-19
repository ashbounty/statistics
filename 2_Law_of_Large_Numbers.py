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
def simulation(population, nmax, interactive=False):
    # Calculate population characteristics
    population_mean = np.mean(population)
    population_sd = np.var(population)**0.5
    # Initialize plot
    plt.title('Simulation: Convergence of sample mean')
    plt.xlabel('Sample Size')
    plt.ylabel('Sample Mean')
    plt.axis([0, nmax, population_mean-1.65*population_sd, population_mean+1.65*population_sd])
    plt.hlines(population_mean, 0, nmax, color = 'darkred', label = 'Population mean')
    # Initialize lists
    sample = []
    means = []
    # Start of the simulation
    for n in range(1, nmax):
        # Append sample by iid new observation
        sample.append(np.random.choice(population))
        # Recalculate the sample mean
        means.append(np.mean(sample))
    plt.plot(means, color = 'darkblue', label = 'Sample averages')
    plt.legend()
    plt.show()

# Tryin with different population
simulation(np.random.normal(size=1000000), 2000)
simulation(np.random.exponential(size=1000000), 2000)
simulation(np.random.uniform(size=1000000), 2000)