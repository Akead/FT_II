import numpy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
from prettytable import PrettyTable
from scipy.optimize import curve_fit

from statsmodels.graphics import tsaplots

year, data =  numpy.loadtxt('co2mlo.txt', unpack=True, usecols=(2,4))
data = numpy.array([j for i,j in zip(year, data) if i > 1999.125])
year = numpy.array([i for i in year if i > 1999.125])

def polynomial(x, a, b, c, d):
    return a + b*x +c*x**2 + d*x**3

def fit_polynomial(X, Y):
    popt1, pcov1 = curve_fit(polynomial, X, Y)
    return popt1

def FourierSeriesFitLong(x, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5, a6):
    px = 2 * numpy.pi * x
    Y1 = a1 * numpy.cos(px) + b1 * numpy.sin(px)
    Y2 = a2 * numpy.cos(2*px) + b2 * numpy.sin(2*px)
    Y3 = a3 * numpy.cos(3*px) + b3 * numpy.sin(3*px)
    Y4 = a4 * numpy.cos(4*px) + b4 * numpy.sin(4*px)
    Y5 = a5 * numpy.cos(5*px) + b5 * numpy.sin(5*px)
    Y6 = a6 * numpy.cos(6*px)
    return Y1 + Y2 + Y3 + Y4 + Y5 + Y6

def FourierSeriesFitShort(x, a1, b1, a2, b2):
    px = 2 * numpy.pi * x
    Y1 = a1 * numpy.cos(px) + b1 * numpy.sin(px)
    Y2 = a2 * numpy.cos(2*px) + b2 * numpy.sin(2*px)
    return Y1 + Y2

def fit_fourier(X, Y, fun=FourierSeriesFitLong):
    popt1, pcov1 = curve_fit(fun, X, Y)
    return popt1

def zadanie_1():

    fig, ax = plt.subplots()
    ax.plot(year, data)
    ax.set_title('$X_i$')
    fig.savefig('lipior_4_0.png', dpi=200)

    poly_fit = fit_polynomial(year, data)
    Ti = polynomial(year, *poly_fit)

    fig, ax = plt.subplots()
    ax.plot(year, data, year, Ti)
    ax.set_title('$X_i$ | $T_i$')
    fig.savefig('lipior_4_1.png', dpi=200)

    # four_long_fit = fit_fourier(year, data)
    # print(four_long_fit)
    # Si = FourierSeriesFitLong(year, * four_long_fit)

    four_fit = fit_fourier(year, data-Ti, FourierSeriesFitShort)
    Si = FourierSeriesFitShort(year, * four_fit)

    fig, ax = plt.subplots()
    ax.plot(year, data, year, Ti, year, Si + Ti)
    ax.set_title('$X_i$ | $T_i$ | $T_i$ + $S_i$')
    fig.savefig('lipior_4_2.png', dpi=200)


    szum = data - Ti - Si
    fig, ax = plt.subplots()
    ax.plot(year, szum)
    ax.set_title('Szum')
    fig.savefig('lipior_4_3.png', dpi=200)

    fig = tsaplots.plot_acf(szum, lags=20)
    fig.savefig('lipior_4_3a.png', dpi=200)

    

    szum_bialy = numpy.random.randn(100)
    fig, ax = plt.subplots()
    ax.plot(szum_bialy)
    ax.set_title('Szum biały')
    fig.savefig('lipior_4_4.png', dpi=200)

    fig = tsaplots.plot_acf(szum_bialy, lags=20)
    fig.savefig('lipior_4_4a.png', dpi=200)

def gen_xi(x_1 ,x_2, fi_1, fi_2):
    epsilon = numpy.random.normal(0, 0.3)
    xi = fi_1 * x_1 + fi_2 * x_2 + epsilon
    yi = epsilon
    return (xi ,yi)

def zadanie_2():
    fi_1 = 0.95
    fi_2 = -0.2

    x_1 = 0
    x_2 = 0

    Xdata = []
    Ydata = []
    for i in range(-20, 2001):
        x, y = gen_xi(x_1, x_2, fi_1, fi_2) 
        x_2, x_1 = x_1, x
        if i >0:
            Xdata.append(x)
            Ydata.append(y)

    X = Xdata[:101]
    Y = Ydata[:101]

    fig, ax = plt.subplots()
    ax.plot(X)
    ax.plot(Y)
    fig.savefig('lipior_4_2_1.png', dpi=200)

    fig = tsaplots.plot_acf(Xdata, lags=20)
    fig.savefig('lipior_4_2_1X.png', dpi=200)

    fig = tsaplots.plot_acf(Ydata, lags=20)
    fig.savefig('lipior_4_2_1Y.png', dpi=200)

    fi_1 = 0.95
    fi_2 = -0.8

    x_1 = 0
    x_2 = 0

    Xdata = []
    Ydata = []
    for i in range(-20, 2001):
        x, y = gen_xi(x_1, x_2, fi_1, fi_2) 
        x_2, x_1 = x_1, x
        if i >0:
            Xdata.append(x)
            Ydata.append(y)

    X = Xdata[:101]
    Y = Ydata[:101]

    fig, ax = plt.subplots()
    ax.plot(X)
    ax.plot(Y)
    fig.savefig('lipior_4_2_2.png', dpi=200)

    fig = tsaplots.plot_acf(Xdata, lags=20)
    fig.savefig('lipior_4_2_2X.png', dpi=200)

    fig = tsaplots.plot_acf(Ydata, lags=20)
    fig.savefig('lipior_4_2_2Y.png', dpi=200)

if __name__ == "__main__":
    zadanie_1()
    #zadanie_2()