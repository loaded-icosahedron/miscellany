import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider, Button, RadioButtons

x = np.linspace(-5,5)

def y(x):
    return np.sin(x)




fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)

l, = plt.plot(x, y(x), lw=2)

axcolor = 'lightgoldenrodyellow'
ax_xscale = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_yscale = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

s_xscale = Slider(ax_xscale, r'$a_x$', -2, 2, valinit=1)
s_yscale = Slider(ax_yscale, r'$b_y$', -2, 2, valinit=1)


def update(val):
    xscale = s_xscale.val
    yscale = s_yscale.val
    l.set_ydata(yscale*y(x))
    l.set_xdata(xscale*x)
    fig.canvas.draw_idle()


s_xscale.on_changed(update)
s_yscale.on_changed(update)

plt.show()
