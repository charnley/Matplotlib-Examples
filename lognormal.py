import numpy
import pylab

def lognormal(x, m, s):
    return 1.0/(x * numpy.sqrt(s * numpy.pi * s**2.0)) * \
           numpy.exp( - (numpy.log(x) - m )**2.0 / (2 * s**2.0 ))

x = numpy.arange(0.01, 45.0, 0.01)

pylab.figure(figsize=(7,5))


sigma = 0.4
median = 14.0
mu = numpy.log(median)

dss = lognormal(x, mu, sigma)

sigma = 0.4
median = 6.4 / 11.0 * 14.0
mu = numpy.log(median)

dst = lognormal(x, mu, sigma)

sigma = 0.4
median = 1.0 / 11.0 * 14.0
mu = numpy.log(median)

edc = lognormal(x, mu, sigma)
#dss = dss /max(dss)
#dst = dst /max(dst)

pylab.plot(x, dss, label = "DSS, 11 angstrom")
pylab.plot(x, dst, label = "DST, 6.4 angstrom")
#pylab.plot(x, edc, label = "EDC, 0 angstrom")

pylab.xlim([0.0, 30.0])
pylab.ylim([0.0, 0.4])

pylab.legend()
pylab.xlabel("Ca-Ca Distance [angstrom]")
pylab.ylabel("Likelihood")
pylab.savefig("lognormal.png")

