import matplotlib.pyplot as plt
import numpy

X = numpy.linspace(0, 2*numpy.pi,100)
Y = numpy.sin(X)

# first order term
Y1 = numpy.pi - X

# new (post version 1.2) style for plotting uses the subplots function
# to make a figure _and_ the axes. The old methods are still available
f, ax = plt.subplots()

ax.plot(X,Y)
ax.plot(X,Y1)

ax.annotate("$\pi - x$",
            xy=(2*numpy.pi/3, numpy.pi/3), xycoords='data',
            xytext=(+30,+10), textcoords='offset points',
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))

ax.set_title("Taylor Expansion of $\sin(x)$ around $x=\pi$")
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")

ax.set_ylim(numpy.min(Y)*1.5, numpy.max(Y)*1.5)
ax.set_xlim(numpy.min(X), numpy.max(X))

plt.savefig("annotate.png")
