# This file takes random samples from a population with distribution F. The sample size, starting at 10, will successively 
# increase by factor 10, ending at 100000. This simulation intends to illustrate that the empirical distribution function
# converges to the true distribution function of the population. 

# Load packages
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import expon

# Set some global settings for the plots
mpl.rc(('axes', 'xtick', 'ytick'), labelsize='small')
mpl.rcParams['axes.titlesize'] = 'medium'
mpl.rcParams['axes.titleweight'] = 'bold'
mpl.rcParams['axes.grid'] = True
mpl.rcParams['grid.alpha'] = 0.2

# 1) Simulation: Normal distribution

# Create true distribution function
x = np.linspace(-3, 3, 1000)
dist = norm()

# Sample characteristic X~N(0,1) from the population with sample sizes (10, 100, 1000, 10000, 100000)
normal_samples = [(n, np.random.normal(size=n)) for n in [10, 100, 1000, 10000, 100000]]

# Plot histogram of each sample from the population
fg, ax = plt.subplots(5, 1, figsize = [4, 6], sharex=True, sharey=True)
fg.suptitle(r'$X \backsim N(\mu = 0, \sigma = 1)$', y = 0.95)
for i in range(5):
    n = normal_samples[i][0]
    sample = normal_samples[i][1]
    ax[i].hist(sample, normed=1, bins=int(n**.5))
    ax[i].plot(x, dist.pdf(x), color='darkred')
    ax[i].text(0, 1, 'N={0}'.format(n), va='top', 
               bbox={'boxstyle':'square', 'facecolor':'white', 'lw':1}, 
               transform=ax[i].transAxes)
fg.subplots_adjust(hspace=0)
plt.show()

# 2) Simulation: Exponential distribution

# Create true distribution function
x = np.linspace(0, 10, 1000)
dist = expon()

# Sample characteristic X~N(0,1) from the population with sample sizes (10, 100, 1000, 10000, 100000)
expon_samples = [(n, np.random.exponential(size=n)) for n in [10, 100, 1000, 10000, 100000]]

# Plot histogram of each sample from the population
fg, ax = plt.subplots(5, 1, figsize = [4, 6], sharex=True, sharey=True)
fg.suptitle(r'$X \backsim Exp(\lambda = 1)$', y = 0.95)
for i in range(5):
    n = expon_samples[i][0]
    sample = expon_samples[i][1]
    ax[i].hist(sample, normed=1, bins=int(n**.5))
    ax[i].plot(x, dist.pdf(x), color='darkred')
    ax[i].text(0, 1, 'N={0}'.format(n), va='top', 
               bbox={'boxstyle':'square', 'facecolor':'white', 'lw':1}, 
               transform=ax[i].transAxes)
fg.subplots_adjust(hspace=0)
plt.show()

# Observations:
# A histogram is a consistent estimator for the distribution function of the population
# The empirical distribution converges to the true distribution for large N
