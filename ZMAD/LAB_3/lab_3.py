import numpy
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
from matplotlib import cm
from prettytable import PrettyTable

S = 0.2

class Plot_Imshow():

    def __init__(self, data, **kwargs):
        self._data = data[::-1] if kwargs.setdefault('no_y_inverse', True) else data 
        self._kwargs = kwargs

    def _set_figure(self):
        self._figure, self._ax = plt.subplots()
    
    def _show_figure(self):
        self._ax.xaxis.label.set_size(18)
        self._ax.yaxis.label.set_size(18)
        self._ax.title.set_size(18)
        self._ax.tick_params(labelsize = 'large')
        self._ax.get_figure().set_size_inches(18.5, 10.5, forward = True)

        if self._kwargs.setdefault('plot', True):
            plt.show()

    def _save_figure(self, name):

        self._ax.xaxis.label.set_size(18)
        self._ax.yaxis.label.set_size(18)
        self._ax.title.set_size(18)
        self._ax.tick_params(labelsize = 'large')
        self._ax.get_figure().set_size_inches(18.5, 10.5, forward = True)

        if self._kwargs.setdefault('no_save', False):
            self._figure.savefig(f'{name}.png', dpi = 200)
            plt.close()        

    def plot(self):

        self._set_figure()
        imshow = self._ax.imshow(self._data, cmap = self._kwargs.setdefault('heatmap_color', 'jet'), aspect = 'auto')
        
        if not self._kwargs.setdefault('no_colorbar', False):
            colorbar = self._figure.colorbar(imshow)
            colorbar.ax.tick_params(labelsize = 18)
            if self._kwargs.setdefault('colorbar_title', None) is not None:
                colorbar.set_label(self._kwargs['colorbar_title'], size=18)
 
        if self._kwargs.setdefault('extent', None) is not None:
            imshow.set_extent(self._kwargs['extent'])

        self._ax.set_title(self._kwargs.setdefault('title', ''))
        self._ax.set_xlabel(self._kwargs.setdefault('xlabel', ''))
        self._ax.set_ylabel(self._kwargs.setdefault('ylabel', ''))
        self._ax.grid()
        self._show_figure()
        self._save_figure(self._kwargs['name'])

def P_apriori(mu, sigma):
    return -4.15 + 3.6*mu - 0.6*(mu**2) + 4.8*sigma -12*(sigma**2)

def Probability(x, mu, sigma):
    A =  S * 1/(numpy.sqrt(2*numpy.pi)*sigma)
    B = numpy.exp(-((x-mu)**2)/(2*(sigma**2)))
    C = (1-S)/18
    return A * B + C

def Probability_X(X, mu, sigma):
    return numpy.prod([Probability(x, mu, sigma) for x in X])

def zadanie_1():
    SIGMA = numpy.linspace(0.1,0.5,40)
    MU = numpy.linspace(2,4,40)

    RES = []
    for sigma in SIGMA:
        R = []
        for mu in MU:
            R.append(P_apriori(mu, sigma) * Probability_X(X, mu, sigma))
        RES.append(R)
    RES = RES/numpy.sum(RES)
    options = {'name' : '3_1_lipior', 'title' : '','xlabel': '$\mu$', 'ylabel': '$\sigma$' ,
            'no_save': True, 'plot': True,
            'colorbar_title': '', 'heatmap_color': 'plasma','extent': [2, 4, 0.1, 0.5], 'no_y_inverse': False}

    Plot_Imshow(RES, **options).plot()

    sigma = [sum(i) for i in RES]
    fig, ax =plt.subplots()
    ax.plot(SIGMA, sigma)
    fig.savefig('3_12_lipior.png', dpi=200)

    mu = [sum(i) for i in numpy.rot90(RES)][::-1]
    fig, ax =plt.subplots()
    ax.plot(MU, mu)
    fig.savefig('3_13_lipior.png', dpi=200)

    mu_sr = sum([i*j for i,j in zip(mu, MU)])

    sigma_sr = sum([i*j for i,j in zip(sigma, SIGMA)])

    mu_std = numpy.sqrt(sum([(j-mu_sr)**2*i for i,j in zip(mu, MU)]))

    sigma_std = numpy.sqrt(sum([(j-sigma_sr)**2*i for i,j in zip(sigma, SIGMA)]))

    RES = []
    for sigma in SIGMA:
        R = []
        for mu in MU:
            R.append(P_apriori(mu, sigma))
        RES.append(R)
    RES = RES/numpy.sum(RES)
    options = {'name' : '3_11_lipior', 'title' : '','xlabel': '$\mu$', 'ylabel': '$\sigma$' ,
            'no_save': True, 'plot': True,
            'colorbar_title': '', 'heatmap_color': 'plasma','extent': [2, 4, 0.1, 0.5], 'no_y_inverse': False}

    Plot_Imshow(RES, **options).plot()

    TAB = PrettyTable()
    TAB.field_names = ["Nazwa", 'Wartość']
    TAB.add_row(['mu_sr', '{:.4f}'.format(mu_sr)])
    TAB.add_row(['sigma_sr', '{:.4f}'.format(sigma_sr)])
    TAB.add_row(['mu_std', '{:.4f}'.format(mu_std)])
    TAB.add_row(['sigma_std', '{:.4f}'.format(sigma_std)])
    print(TAB)

def zadanie_2():

    N = 10**4
    Nj = 5*10**2
    k_mu = 0.05
    k_sigma = 0.005
    mu_gen = []
    sigma_gen = []
    
    for i in range(N):
        print(f'Calculated {i/N*100} %')
        mu_p = 2 + 2 * numpy.random.rand()
        sigma_p = 0.1 + 0.4 * numpy.random.rand()
        for j in range(Nj):
            mu_n = mu_p + k_mu * numpy.random.randn()
            sigma_n = sigma_p + k_sigma * numpy.random.randn()
            if P_apriori(mu_n, sigma_n) * Probability_X(X, mu_n, sigma_n) > numpy.random.rand() * P_apriori(mu_p, sigma_p) * Probability_X(X, mu_p, sigma_p):
                if (2 < mu_n < 4) and (0.1 < sigma_n < 0.5):
                        mu_p = mu_n
                        sigma_p = sigma_n
        mu_gen.append(mu_p)
        sigma_gen.append(sigma_p)

    fig, ax =plt.subplots()
    ax.hist2d(mu_gen, sigma_gen,bins=int(numpy.sqrt(len(mu_gen))))
    fig.savefig('3_2YY_lipior.png', dpi=200)

    mu_sr = numpy.mean(mu_gen)
    mu_std = numpy.std(mu_gen)
    sigma_sr = numpy.mean(sigma_gen)
    sigma_std = numpy.std(sigma_gen)

    TAB = PrettyTable()
    TAB.field_names = ["Nazwa", 'Wartość']
    TAB.add_row(['mu_sr', '{:.4f}'.format(mu_sr)])
    TAB.add_row(['sigma_sr', '{:.4f}'.format(sigma_sr)])
    TAB.add_row(['mu_std', '{:.4f}'.format(mu_std)])
    TAB.add_row(['sigma_std', '{:.4f}'.format(sigma_std)])
    print(TAB)

if __name__ == "__main__":
    X =  numpy.loadtxt('obserwacje.dat', unpack=True)

    #zadanie_1()
    zadanie_2()