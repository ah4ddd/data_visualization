import matplotlib.pyplot as plt

x = [1,2,3,4]
y= [1,4,9,16]

plt.plot(x,y, linewidth=3, color='red')
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Input Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(axis='both', labelsize=12)
plt.show()
