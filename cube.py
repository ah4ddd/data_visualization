import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# ── Small plot: First five cubes ──
x_small = [1, 2, 3, 4, 5]
y_small = [x**3 for x in x_small]

fig1, ax1 = plt.subplots()

ax1.scatter(x_small, y_small, c=y_small, cmap='Greens', s=40)

ax1.set_title("First Five Cube Numbers", fontsize=24)
ax1.set_xlabel("Value", fontsize=14)
ax1.set_ylabel("Cube of Value", fontsize=14)
ax1.tick_params(labelsize=14)

ax1.set_xlim(0, 6)
ax1.set_ylim(0, 140)

plt.tight_layout()
plt.show()

# ── Big plot: Your original 5,000 cubes ──
x_val = range(1, 5001)
y_val = [x**3 for x in x_val]

fig2, ax2 = plt.subplots()

ax2.scatter(x_val, y_val, c=y_val, cmap='Greens', s=10)

ax2.set_title("Cube Numbers", fontsize=24)
ax2.set_xlabel("Value", fontsize=14)
ax2.set_ylabel("Cube of Value", fontsize=14)
ax2.tick_params(labelsize=14)
ax2.ticklabel_format(style='plain')

plt.tight_layout()
plt.show()
