#!/usr/bin/env python

"""

"""

######################################################################
## Create plots without X

import matplotlib
matplotlib.use('Agg')

######################################################################

import numpy as np
import matplotlib.pyplot as plt

######################################################################
## LATEX STYLE

from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
rc('xtick', labelsize=15)
rc('ytick', labelsize=15)
matplotlib.rcParams.update({'font.size': 20})

######################################################################

# Get the axes
axes = plt.gca()

# Fake Data
X = [1, 2, 4, 8, 16, 32]
Y1 = [np.log(x) for x in X]
Y2 = [1.5*np.log(x) for x in X]
Y3 = [x-1 for x in X]

# Plot the data
plt.plot(X, Y1, 'b.-')
plt.plot(X, Y2, 'g.-')
plt.plot(X, Y3, 'r.-')

# Set Ticks
tick_locs = X
tick_lbls = X
plt.xticks(tick_locs, tick_lbls)

tick_locs = range(10)
tick_lbls = range(10)
plt.yticks(tick_locs, tick_lbls)


# Grid
plt.grid(True)

# Focus on the plot
plt.ylim(-0.5, 8)
plt.xlim(-1, max(X)+1)

# Labels
plt.xlabel('$N$ CPU\'s')
plt.ylabel('Speed up')

# Only show ticks on bottom and left frame
axes.get_xaxis().tick_bottom()
axes.get_yaxis().tick_left()

# Save the figure in different formats
plt.savefig('speed_up.png')
plt.savefig('speed_up.eps')
plt.savefig('speed_up.pdf')
plt.savefig('speed_up.tiff')

