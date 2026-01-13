import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label="Squares")
plt.plot(x, y2, label="Linear")

plt.legend()
plt.show()
