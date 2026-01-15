import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('ggplot')

    fig, ax = plt.subplots()
    points_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap='Blues', edgecolors=None, s=1)
    #show start-end
    ax.scatter(0, 0, c='lime', s=150, marker='*', edgecolors='black', linewidth=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='yellow', s=100, marker='o', edgecolors='white', linewidth=2)

    #remove axes (optinal btw)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_aspect('equal')
    plt.show()
    keep_running = input("Make another walk? y/n: ")
    if keep_running == 'n':
        break
