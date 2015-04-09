"""
PERSEUS SimpleDisplay

[Derek Merck](derek_merck@brown.edu)
[Leo Kobayashi](lkobayashi@lifespan.org)
Spring 2015

<https://github.com/derekmerck/PERSEUS>

Dependencies: Numpy, matplotlib

See README.md for usage, notes, and license info.
"""

#import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # There is a problem with the default renderer under OSX
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Stripchart:
    def __init__(self, pnode, maxt=2, dt=0.02):
        self.pnode = pnode

        fig, ax = plt.subplots()

        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(-.1, 1.1)
        self.ax.set_xlim(0, self.maxt)
        self.ani = animation.FuncAnimation(fig, self.update, interval=self.pnode.update_interval * 1000, blit=True)

        plt.show()


    def update(self, dummy):

        y = self.pnode.get('listener0')[1]

        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:     # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        return self.line,
