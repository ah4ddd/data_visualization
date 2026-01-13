import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Explicit Control")
ax.set_xlabel("X")
ax.set_ylabel("Y")
plt.show()
fig.savefig("plot.png")
