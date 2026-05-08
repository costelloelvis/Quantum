import numpy as np
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Setup figure
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.axis('off')

# Labels
ax.text(1, 1.5, "Alice", fontsize=12)
ax.text(8, 1.5, "Bob", fontsize=12)

# Qubit points
q0, = ax.plot([], [], 'bo', label='Qubit ψ (to teleport)')
q1, = ax.plot([], [], 'go', label='Entangled (Alice)')
q2, = ax.plot([], [], 'ro', label='Entangled (Bob)')

# Text display
info = ax.text(5, -1.5, "", ha='center', fontsize=11)

# Initial positions
x0, y0 = 1, 0
x1, y1 = 3, 0
x2, y2 = 7, 0

step = 0

def update(frame):
    global step, x0

    # Step progression
    if frame < 30:
        info.set_text("Step 1: Prepare state |ψ⟩ at Alice")
        q0.set_data(x0, y0)
        q1.set_data(x1, y1)
        q2.set_data(x2, y2)

    elif frame < 60:
        info.set_text("Step 2: Create entanglement (q1 ↔ q2)")
        q1.set_color('cyan')
        q2.set_color('cyan')

    elif frame < 100:
        info.set_text("Step 3: Bell measurement at Alice")
        x0 += 0.1
        q0.set_data(x0, y0)

    elif frame < 140:
        info.set_text("Step 4: Classical bits sent to Bob")

    elif frame < 180:
        info.set_text("Step 5: Bob reconstructs |ψ⟩")
        q2.set_color('yellow')

    else:
        info.set_text("Teleportation complete ✅")

    return q0, q1, q2, info

ani = FuncAnimation(fig, update, frames=200, interval=50, cache_frame_data=False)

plt.legend()
plt.title("Quantum Teleportation (Live Animation)")
plt.show()