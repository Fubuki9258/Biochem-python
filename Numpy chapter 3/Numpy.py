"""
Numpy Chapter 3: Basics of Numpy
"""

import numpy as np

weightarray = np.array([60, 72, 57, 90, 95, 72])

print("weightarray length is:", len(weightarray))
print("weightarray length (using np.size) is:", np.size(weightarray))
print(weightarray.shape) # returns tuple (6,)

n = np.array([0, 1, 2, 3, 4])
z = n * 3
p = np.array([10, 20, 30, 40, 50])
q = n * p

print(z, q)

# adding these two array would results in an error, due to the length difference
a = np.array([0, 1, 2, 3, 4, 5])
b = np.array([0, 1, 2])

