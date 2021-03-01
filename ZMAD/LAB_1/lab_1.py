import argparse
import numpy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
from prettytable import PrettyTable

######## ZADANIE 1 ########

def zmienna_losowa(N=1):
    return [-2 * numpy.log(1 - (1-numpy.exp(-2)) * numpy.random.random()) for _ in range(N)]

def gestosc_prawdopodobienstwa(x):
    return numpy.exp(- x/2)/(2 * (1 - numpy.exp(-2)))

def zadanie_1():
    x = zmienna_losowa(int(1e6))
    X_g = numpy.linspace(0,4,1000)
    Y_g = [gestosc_prawdopodobienstwa(x) for x in X_g]

    fig, ax = plt.subplots()
    ax.hist(x, density=True, bins=50, align='left')
    ax.plot(X_g, Y_g)

    ax.get_figure().savefig('1.png', dpi=200)

######## ZADANIE 2 ########

def zmienna_losowa_2(N=1):
    return [-2 * numpy.log(1 - (1-numpy.exp(-numpy.pi/2)) * numpy.random.random()) for _ in range(N)]

def gestosc_prawdopodobienstwa_2(x):
    return numpy.exp(- x/2)/(2 * (1 - numpy.exp(-numpy.pi/2)))

def fun_x(x):
    return 65/66 * 1/(1 - numpy.exp(-numpy.pi/2)) * numpy.cos(2*x)**2 * numpy.exp(-x/2) 

def fun_1(x):
    return 65/33 * numpy.exp(-x/2)/2 * 1/(1 - numpy.exp(-2))

def fun_2(x):
    return 65/66 * 1/(1 - numpy.exp(-2)) * numpy.cos(2*x)**2 * numpy.exp(-x/2) 

def wybieranie():
    x_try = zmienna_losowa_2()[0]
    u_try = numpy.random.random()
    while True:
        xx = fun_1(x_try) * u_try
        yy = fun_2(x_try)
        if xx < yy:
            return x_try
        else:
            x_try = zmienna_losowa_2()[0]
            u_try = numpy.random.random()

def zadanie_2():
    #x = zmienna_losowa_2(int(1e4))
    x = [wybieranie() for _ in range(10**6)]
    X_g = numpy.linspace(0,numpy.pi,1000)
    Y_g = [65/33 * gestosc_prawdopodobienstwa_2(x) for x in X_g]

    X_f = numpy.linspace(0,numpy.pi,1000)
    Y_f = [fun_x(x) for x in X_f]

    fig, ax = plt.subplots()
    ax.hist(x, density=True, bins=50, align='mid')
    ax.plot(X_g, Y_g)
    ax.plot(X_f, Y_f)

    ax.get_figure().savefig('2.png', dpi=200)

#zadanie_1()
zadanie_2()