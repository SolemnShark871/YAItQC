# Interactive graph to show how 

import numpy as np
from numpy import * #Use with caution as this causes packages to mess with each other
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
plt.style.use('seaborn')
# %matplotlib


# The parametrized function to be plotted
def f(x , a):
    return 10/a * np.sqrt(x)

x = np.linspace(0, 1000, 10000)

# Define initial parameters

a = 1

# Create the figure and the line that we will manipulate
fig, ax = plt.subplots()
line, = plt.plot(x, f(x, a),lw = 5,  label = 'Quantum search')
plt.plot(x,x,lw = 5,label = 'Classical search')
ax.set_xlabel('Size of problem', fontsize = 24)
ax.set_ylabel('Time taken to solve', fontsize = 24)
ax.set_title("Grover's Search Algorithm", fontsize = 36)
# adjust the main plot to make room for the sliders
plt.subplots_adjust(bottom=0.25)
plt.legend()
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