#Shor's

# TODO: Make this more readable on laptops

import numpy as np
from numpy import * #Use with caution as this causes packages to mess with each other
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import random
# %matplotlib 
plt.style.use('default')


# The parametrized function to be plotted
def f(x , a):
    return 10/a * x**3

x = np.linspace(0, 100, 1000)


# Define initial parameters

a = 1

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = plt.plot(x, f(x, a), label = 'Quantum factorisation')
g = np.exp(x**1/3)
plt.plot(x,g, label = 'Classical Factorisation' )
ax.set_xlabel('Size of problem')
ax.set_ylabel('Time taken to solve')
ax.set_yscale('log')
ax.set_title("Shor's Factoring Algorithm")


# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.25)

# Make a horizontal slider to control the frequency.
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03])
speed_slider = Slider(
    ax=axfreq,
    label='Speed of Quantum Computer',
    valmin=0.1,
    valmax= 1,
    valinit=0.1,
)

# The function to be called anytime a slider's value changes
def update(val):
    line.set_ydata(f(x, speed_slider.val))
    fig.canvas.draw_idle()


# register the update function with each slider
speed_slider.on_changed(update)

# Create a `matplotlib.widgets.Button` to reset the sliders to initial values.
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    speed_slider.reset()
button.on_clicked(reset)

plt.show()