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

Z = numpy.rot90(numpy.loadtxt('21.txt'))

D = Z[-1]
Vo = Z[-2]
Ii = Z[-3]
Io = Z[-4]
S = Z[0]*100
print(D,Vo,Ii,Io,S)

classic = {'color': 'blue', 'marker': 'd', 'markersize': 15, 'linestyle': 'None', 'linewidth': '5'}

settings = {'name': '2_42_1', 'title': '',
            'y_label': '$V_{o}$ [V]', 'x_label': '$D$ [%]', 'location': 'upper right'}

Plot_1D(D, Vo, [classic], settings, False, True).plot()

classic = {'color': 'blue', 'marker': 'd', 'markersize': 15, 'linestyle': 'None', 'linewidth': '5'}

settings = {'name': '2_42_2', 'title': '',
            'y_label': '$\eta$ [%]', 'x_label': '$D$ [%]', 'location': 'upper right'}

Plot_1D(D, S, [classic], settings, False, True).plot()