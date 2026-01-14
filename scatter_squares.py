import matplotlib.pyplot as plt

x_val = range(1, 1001)
y_val = [x**2 for x in x_val]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_val, y_val, c=y_val, cmap='Blues', s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()
