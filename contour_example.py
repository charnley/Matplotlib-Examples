import numpy
from matplotlib import pyplot
from matplotlib import cm

# Get the same plot every time.
numpy.random.seed(666)

# Make some fake data.
x_vals = numpy.random.normal(5.0, 2.0, 10000)
y_vals = numpy.random.normal(300.0, 60.0, 10000)

# Set X- and Y-ranges.
x_range = [0,10]
y_range = [0,500]

# Number of bins.
bin_no = 25

# Make a 2D histogram using NumPy.
# Note the different ordering of edges (output) from that of values and ranges.
H, xedges, yedges = numpy.histogram2d(y_vals, x_vals, range=[y_range,x_range], bins=(bin_no, bin_no))

# Define the plot-range and plot.
extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]
pyplot.contourf(H, extent=extent, zorder = -1, cmap = cm.PuBu)

# Finally, set limits and save file.
pyplot.xlim(x_range)
pyplot.ylim(y_range)
pyplot.savefig("contour.png")


