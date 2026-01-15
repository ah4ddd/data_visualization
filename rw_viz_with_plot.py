import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    cmap = plt.get_cmap('Blues')
    for i in range(rw.num_points - 1):
        ax.plot(rw.x_values[i:i+2], rw.y_values[i:i+2], color=cmap(i/rw.num_points), linewidth=1)

    ax.scatter(0, 0, c='lime', s=150, marker='*', edgecolors='black', linewidth=2, zorder=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', s=100, marker='o', edgecolors='white', linewidth=2, zorder=10)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break
