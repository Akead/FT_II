import numpy
from scipy.linalg import eigh
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker

class Plot_1D:

    def __init__(self, x, y, plot_options, settings, plot = True, save = True):
        self._x = x if isinstance(x, list) else [x]
        self._y = y if isinstance(x, list) else [y]
        self._plot_options = plot_options if isinstance(plot_options, list) else [y]
        self._settings = settings
        self._settings['name'] = f'{settings["name"]}.png'
        self._plot = plot
        self._save = save

    def plot(self):
        
        fig, ax = plt.subplots()
        legend = []
        right_flag = False
        for x, y, options in zip(self._x, self._y, self._plot_options):
            if self._settings.setdefault('log', False):
                if options.setdefault('right_axis', None) is not None:
                    right_flag = True
                    ax_right = ax.twinx()
                    line, = ax_right.loglog(x,y)
                else:
                    right_flag = False
                    line, = ax.loglog(x, y)

            else:
                if options.setdefault('right_axis', None) is not None:
                    right_flag = True
                    ax_right = ax.twinx()
                    line, = ax_right.plot(x,y)
                else:
                    right_flag = False
                    line, = ax.plot(x, y)

            color = options['color'] if options.setdefault('color', None) is not None else 'black'
            linestyle = options['linestyle'] if options.setdefault('linestyle', None) is not None else 'solid'
            marker = options['marker'] if options.setdefault('marker', None) is not None else None
            markersize = options['markersize'] if options.setdefault('markersize', None) is not None else 6
            label = options['legend'] if options.setdefault('legend', None) is not None else ''

            line.set_color(color)
            line.set_linestyle(linestyle)
            line.set_linewidth(4)
            line.set_marker(marker)
            line.set_markersize(markersize)
            line.set_markeredgecolor('red')
            description = mlines.Line2D([], [], label = label, color = color, marker = marker, linestyle = linestyle)
            legend.append(description)

        location = self._settings['location'] if self._settings.setdefault('location', None) is not None else 'lower right'
        if label:
            ax.legend(handles = legend, loc = location, fontsize = 'large',prop={'size': 30})
        ax.set(title = self._settings['title'], xlabel = self._settings['x_label'], ylabel = self._settings['y_label'])
        if right_flag:
            ax_right.set(ylabel = self._settings['y_right_label'])
            ax_right.yaxis.label.set_size(18)
            ax_right.tick_params(labelsize = 'large')
            ax_right.grid()
        ax.grid()
        ax.xaxis.label.set_size(18)
        ax.yaxis.label.set_size(18)
        ax.title.set_size(18)
        ax.tick_params(labelsize = 'large')
        ax.get_figure().set_size_inches(18.5, 10.5, forward = True)

        if self._plot:
            plt.show()
        
        if self._save:
            fig.savefig(self._settings['name'], dpi = 100, bbox_inches='tight')
            plt.close()

xi = numpy.sqrt(2)/2
omega_a = 2*numpy.pi * 1.6e3

def pt(xi, omega_a, omega_d, psi, t):
    A = numpy.exp(-xi*omega_a*t)
    B = numpy.sqrt(1-xi**2)
    C = numpy.sin(omega_d*t+psi)
    return 1 - A/B*C

def omega_d (omega_a, xi):
    return omega_a * numpy.sqrt(1-xi**2)

def psi(xi):
    return numpy.arctan(numpy.sqrt(1-xi**2)/xi)

omega_d = omega_d(omega_a, xi)
psi = psi(xi)

t = numpy.linspace(0,3e-3,30000)

pt = pt(xi, omega_a, omega_d, psi, t)

l = [0]
for i in range(len(t)-1):
    l.append(1)

classic = {'color': 'blue', 'marker': 'None', 'markersize': 15, 'linestyle': 'solid', 'linewidth': '5', 'legend': 'Odpowiedź filtru'}
classic2 = {'color': 'green', 'marker': 'None', 'markersize': 15, 'linestyle': 'dashed', 'linewidth': '3', 'legend': 'Skok jednostkowy'}

settings = {'name': '3_2', 'title': '',
            'y_label': 'Odpowiedź [j.u.]', 'x_label': 't [$\\mu$s]', 'location': 'lower right'}

Plot_1D([t*10**6, t*10**6], [pt, l], [ classic, classic2], settings, False, True).plot()

for t, p in zip(t, pt):
    if p>0.9 and p<0.91:
        print(t*10**6)