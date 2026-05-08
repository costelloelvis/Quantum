import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
N = 20

# Generate data
alice_bits = np.random.randint(0, 2, N)
alice_bases = np.random.randint(0, 2, N)  # 0=+, 1=x
bob_bases = np.random.randint(0, 2, N)

bob_results = []

for i in range(N):
    if alice_bases[i] == bob_bases[i]:
        bob_results.append(alice_bits[i])
    else:
        bob_results.append(np.random.randint(0, 2))

matches = alice_bases == bob_bases

# Setup plot
fig, ax = plt.subplots(figsize=(8, 3))
ax.set_xlim(0, 10)
ax.set_ylim(-1, 1)
ax.axis('off')

photon, = ax.plot([], [], 'ro', markersize=10)

text = ax.text(0.5, 0.5, '', fontsize=12, ha='center')

x_pos = 0
current = 0

def update(frame):
    global x_pos, current

    # Move photon
    x_pos += 0.2

    if x_pos >= 10:
        x_pos = 0
        current += 1

        if current >= N:
            ani.event_source.stop()
            return photon, text

    photon.set_data(x_pos, 0)

    if current < N:
        info = f"""
Photon {current+1}/{N}

Alice Bit: {alice_bits[current]}
Alice Basis: {'+' if alice_bases[current]==0 else '×'}

Bob Basis: {'+' if bob_bases[current]==0 else '×'}
Bob Result: {bob_results[current]}

Match: {'YES' if matches[current] else 'NO'}
"""
        text.set_text(info)

    return photon, text

ani = FuncAnimation(fig, update, interval=100, cache_frame_data=False)

plt.title("BB84 Quantum Key Distribution (Live)")
plt.show()