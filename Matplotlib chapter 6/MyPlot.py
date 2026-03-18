import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# X axis is 0 - 19
x = np.array(range(20))

# Y axis is 20 random numbers between 1 - 50
y = np.array([40, 31, 21, 5, 21, 46, 44, 24, 3, 1, 27, 14, 2, 49, 37, 24, 30, 38, 43, 20])

plt.figure(figsize=(12, 8)) # plotsize is 12 by 8
# scatter plot, using x and y values, with blue stars as points
plt.scatter(x, y, color="blue", marker="*")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Random plot")
plt.show()
