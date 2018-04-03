import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# scratch:
# 1) Taking k samples in sample size n
# 2) Calculating the average of each sample
# 3) Saving the k averages in list
# 4) Plot the distribution of the averages
# 5) Compare to normal distribution

# Initialize settings
num_of_samples = 100000
sample_size = [5, 10, 100, 5000, 10000]
fg, ax = plt.subplots(5, 1, figsize = [4, 6], sharex=True)
fg.suptitle(r'$X \backsim Exp(\lambda = 1)$', y = 0.95)

# Creating one plot for each simulation with a different sample size
for i in range(len(sample_size)):
    sample_averages = []
    # Creating theoretical distribution of the sample average
    x = np.linspace(1-4*1/sample_size[i]**0.5, 1+4*1/sample_size[i]**0.5, 1000)
    dist = norm(1, 1/sample_size[i]**0.5)
    # Collect the sample averages of N samples
    for k in range(num_of_samples):
        arr = np.random.exponential(1, sample_size[i])
        mean = arr.mean()
        # Append sample average to list
        sample_averages.append(mean)
    # Plot the distribution of the collected sample averages against the theor. distribution
    ax[i].hist(sample_averages, density=True, bins=int(num_of_samples**.5), )
    ax[i].plot(x, dist.pdf(x), color='darkred')
    ax[i].text(0, 1, 'N={0}'.format(sample_size[i]), va='top',
               bbox={'boxstyle':'square', 'facecolor':'white', 'lw':1},
               transform=ax[i].transAxes)

# Showing plots
fg.subplots_adjust(hspace=0)
plt.show()

