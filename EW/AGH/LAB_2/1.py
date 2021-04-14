import sys
import time as TIME
import argparse
import numpy
from scipy.linalg import eigh
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit

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


def xd(D,f,y1,y2):
    T = 1/f
    t = D/100*T
    A = (y2-y1)/t
    B = y1

    X1 = numpy.linspace(0, t, 100)
    Y1 = A*X1 + B
 
    t2 = T-t
    A = -(y2-y1)/t2
    B = y2

    X2 = numpy.linspace(0, t2, 100)
    Y2 = A*X2 + B
    
    X1 =numpy.array([*X1, *X2+t])
    X2 = X1 + T
    X3 = X2 + T
    X = [*X1, *X2, *X3]
    Y = 3*[*Y1, *Y2]
    Y = [i if i >0 else 0 for i in Y]
    return(X,Y)

# X1,Y1 = xd(5,30,-5.225,22.35)
# X2,Y2 = xd(30,30,0.225,75.225)
# X3,Y3 = xd(50,30,11.275,95.425)

X1,Y1 = xd(5,30,-0.75,24.5)
X2,Y2 = xd(30,30,33.25,122.8)
X3,Y3 = xd(50,30,76,166.5)

K1 = {'color': 'blue', 'marker': 'None', 'markersize': 15, 'linestyle': 'solid', 'linewidth': '5', 'legend': 'D=5%'}
K2 = {'color': 'red', 'marker': 'None', 'markersize': 15, 'linestyle': 'solid', 'linewidth': '5',  'legend': 'D=30%'}
K3 = {'color': 'green', 'marker': 'None', 'markersize': 15, 'linestyle': 'solid', 'linewidth': '5', 'legend': 'D=50%'}

settings = {'name': '42_11', 'title': '',
            'y_label': '$I_{L}$ [mA]', 'x_label': '$t$ [ms]', 'location': 'upper right'}

Plot_1D([X1, X2, X3], [Y1, Y2, Y3], [K1, K2, K3], settings, False, True).plot()