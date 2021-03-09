import argparse
import numpy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
from prettytable import PrettyTable
from scipy.optimize import curve_fit

X, Y = numpy.loadtxt('daneszum2.txt', unpack=True)

### ZADANIE 1 ###

#TODO
#There have to be a better way to do this

def FourierSeries1(x, a0, a1, b1):
    pi_x = 2 * numpy.pi * x
    return a0 + a1*numpy.cos(pi_x) + b1*numpy.sin(pi_x)

def FourierSeries2(x, a0, a1, b1, a2, b2):
    pi_x = 2 * numpy.pi * x
    return a0 + a1*numpy.cos(pi_x) + b1*numpy.sin(pi_x) + a2*numpy.cos(2*pi_x) + b2*numpy.sin(2*pi_x) 

def FourierSeries3(x, a0, a1, b1, a2, b2, a3, b3):
    pi_x = 2 * numpy.pi * x
    return a0 + a1*numpy.cos(pi_x) + b1*numpy.sin(pi_x) + a2*numpy.cos(2*pi_x) + b2*numpy.sin(2*pi_x) + a3*numpy.cos(3*pi_x) + b3*numpy.sin(3*pi_x)

def FourierSeries4(x, a0, a1, b1, a2, b2, a3, b3, a4, b4):
    pi_x = 2 * numpy.pi * x
    return a0 + a1*numpy.cos(pi_x) + b1*numpy.sin(pi_x) + a2*numpy.cos(2*pi_x) + b2*numpy.sin(2*pi_x) + a3*numpy.cos(3*pi_x) + b3*numpy.sin(3*pi_x) + a4*numpy.cos(4*pi_x) + b4*numpy.sin(4*pi_x)

def FourierSeries5(x, a0, a1, b1, a2, b2, a3, b3, a4, b4, a5, b5):
    pi_x = 2 * numpy.pi * x
    return a0 + a1*numpy.cos(pi_x) + b1*numpy.sin(pi_x) + a2*numpy.cos(2*pi_x) + b2*numpy.sin(2*pi_x) + a3*numpy.cos(3*pi_x) + b3*numpy.sin(3*pi_x) + a4*numpy.cos(4*pi_x) + b4*numpy.sin(4*pi_x) + a5*numpy.cos(5*pi_x) + b5*numpy.sin(5*pi_x)


def ChiSquare(X, Y, sigma, fun, param, n):
    return sum([((y - fun(x, *param))/sigma)**2 for x, y in zip(X, Y)])

def ChiSquareSS(X, Y, sigma, fun, param, n):
    return sum([((y - fun(x, *param))/sigma)**2 for x, y in zip(X, Y)])/(len(X)-(2*n+1))

def AIC(chi_sq, n):
    return chi_sq  + (2*n+1)*2

def Pi_Pj(Ai, Aj):
    ret = (Ai - Aj)/2
    return numpy.exp(-ret)

def BIC(chi_sq, n, x):
    return chi_sq  + (2*n+1) * numpy.log(len(x))

popt1, pcov1 = curve_fit(FourierSeries1, X, Y)
popt2, pcov2 = curve_fit(FourierSeries2, X, Y)
popt3, pcov3 = curve_fit(FourierSeries3, X, Y)
popt4, pcov4 = curve_fit(FourierSeries4, X, Y)
popt5, pcov5 = curve_fit(FourierSeries5, X, Y)

x = numpy.linspace(min(X), max(X), 100)
fig, ax = plt.subplots(2,3)

y1 = FourierSeries1(x, *popt1)
y2 = FourierSeries2(x, *popt2)
y3 = FourierSeries3(x, *popt3)
y4 = FourierSeries4(x, *popt4)
y5 = FourierSeries5(x, *popt5)

ax[0][0].plot(X, Y, 'o', x, y1)
ax[0][1].plot(X, Y, 'o', x, y2)
ax[0][2].plot(X, Y, 'o', x, y3)
ax[1][0].plot(X, Y, 'o', x, y4)
ax[1][1].plot(X, Y, 'o', x, y5)

# ax[0][0].set_title('F1')
# ax[0][1].set_title('F2')
# ax[0][2].set_title('F3')
# ax[1][0].set_title('F4')
# ax[1][1].set_title('F5')

fig.savefig('1.png', dpi=200)

#Chi Square per degree of freedom

chi_sqss = []
chi_sqss.append(ChiSquareSS(X, Y, 0.6, FourierSeries1, popt1, 1))
chi_sqss.append(ChiSquareSS(X, Y, 0.6, FourierSeries2, popt2, 2))
chi_sqss.append(ChiSquareSS(X, Y, 0.6, FourierSeries3, popt3, 3))
chi_sqss.append(ChiSquareSS(X, Y, 0.6, FourierSeries4, popt4, 4))
chi_sqss.append(ChiSquareSS(X, Y, 0.6, FourierSeries5, popt5, 5))

#Chi Square

chi_sq = []
chi_sq.append(ChiSquare(X, Y, 0.6, FourierSeries1, popt1, 1))
chi_sq.append(ChiSquare(X, Y, 0.6, FourierSeries2, popt2, 2))
chi_sq.append(ChiSquare(X, Y, 0.6, FourierSeries3, popt3, 3))
chi_sq.append(ChiSquare(X, Y, 0.6, FourierSeries4, popt4, 4))
chi_sq.append(ChiSquare(X, Y, 0.6, FourierSeries5, popt5, 5))

#AIC
aic = [AIC(chi, n+1) for n, chi in enumerate(chi_sq)]

#Pi/Pj AIC
AIC_min = min(aic)
Pi_Pj_AIC = [Pi_Pj(Ai, AIC_min) for Ai in aic]

#BIC
bic = [BIC(chi, n+1, X) for n, chi in enumerate(chi_sq)]

#Pi/Pj BIC
BIC_min = min(bic)
Pi_Pj_BIC = [Pi_Pj(Bi, BIC_min) for Bi in bic]

print(f'\n{15*"-"} ZADANIE 1 {15*"-"}\n')

TAB = PrettyTable()
TAB.field_names = ["F", "Chi2/SS", "AIC", "Pi/Pj AIC", "BIC", "Pi/Pj BIC"]

for i, chi, a, pa, b, pb in zip(range(len(aic)), chi_sqss, aic, Pi_Pj_AIC, bic, Pi_Pj_BIC):
    TAB.add_row([i, '{:.4f}'.format(chi), '{:.4f}'.format(a), '{:.4f}'.format(pa), '{:.4f}'.format(b), '{:.4f}'.format(pb)])

print(TAB)

### ZADANIE 2 ###

def kroswalidacja(ind, fun, X, Y):
    X = list(X)
    Y = list(Y)
    t_x = X.pop(ind)
    t_y = Y.pop(ind)

    popt, pcov = curve_fit(fun, X, Y)
    return (t_y - fun(t_x, *popt))**2

funkcje = [FourierSeries1, FourierSeries2, FourierSeries3, FourierSeries4, FourierSeries5]

cross = [sum([kroswalidacja(i, funkcja, X, Y) for i in range(len(X))])/len(X)/(0.6**2) for funkcja in funkcje]

print(f'\n{15*"-"} ZADANIE 2 {15*"-"}\n')

TAB = PrettyTable()
TAB.field_names = ["F", '"Kroswalidacja"']
for i, cro in enumerate(cross):
    TAB.add_row([i, '{:.4f}'.format(cro)])
print(TAB)