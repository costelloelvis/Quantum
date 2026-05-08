import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Physics parameters
k = 1.0   # spring constant
m = 1.0   # mass
dt = 0.05

# Initial conditions
x = 1.0
v = 0.0

# Data storage
x_data = []
t_data = []
t = 0

# Setup plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 20)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("Time")
ax.set_ylabel("Position")
ax.set_title("Live Harmonic Oscillator")

def update(frame):
    global x, v, t

    # Physics update (Euler method)
    a = -k * x / m
    v += a * dt
    x += v * dt
    t += dt

    # Store data
    t_data.append(t)
    x_data.append(x)

    # Update plot
    line.set_data(t_data, x_data)
    return line,

ani = FuncAnimation(fig, update, interval=50)

plt.show()