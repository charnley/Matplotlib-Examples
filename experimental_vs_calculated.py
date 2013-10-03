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

# Fake Data
X = np.arange(0.0, 20.0, 0.1)
Y = np.array([x+np.random.uniform(2,-2) for x in X])
X = np.array([x+np.random.uniform(2,-2) for x in X])

# DATA
plt.plot(X, Y, 'k.')

# LINES
lin = np.array([-100,100])
linp = lin + 2.0
linm = lin - 2.0
plt.plot(lin, lin, 'k-')
plt.plot(lin, linm, 'k--')
plt.plot(lin, linp, 'k--')

# Grid
plt.grid(True)

# Focus on the plot
x_max = np.max(X)
y_max = np.max(Y)
x_min = np.min(X)
y_min = np.min(Y)
x_average = np.average(Y)
y_average = np.average(X)
plt.ylim( y_max+0.1*y_average, y_min-0.1*y_average)
plt.xlim( y_max+0.1*y_average, y_min-0.1*y_average)

# Labels
plt.xlabel('Experimental [A.U.]')
plt.ylabel('Calculated [A.U.]')

# Dots on axis
from matplotlib.ticker import FixedLocator
axes = plt.gca()
axes.xaxis.set_minor_locator(FixedLocator(X))
axes.yaxis.set_minor_locator(FixedLocator(Y))

# Turn off the default frame
# axes.set_frame_on(False)

# Only show ticks on bottom and left frame
axes.get_xaxis().tick_bottom()
axes.get_yaxis().tick_left()

# Save the figure in different formats
plt.savefig('experimental_vs_calculated.png')
plt.savefig('experimental_vs_calculated.eps')
plt.savefig('experimental_vs_calculated.tiff')

