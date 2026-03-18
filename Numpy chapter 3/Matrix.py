import numpy as np
import numpy.random as npr

A = npr.random_integers(-5, 5, size = 9)
A = A.reshape(3, 3)
print("The matrix A is:\n", A)

r = np.array([-1,0,1])
c = np.array([1, 10, 100])

row3 = A[2]
print("\nRow three of matrix A is:\n", row3)

column2 = A[:, 1]
print("\nColumn 2 of A is:\n", column2)

print("\nThe item on the second row and first column is:\n", A[1, 0])
print("\nThe sum of the second column is:\n", sum(A[:, 1]))
print("\nThe sum of every column is:\n", sum(A))
means = []

for row in A:
    mean = float(sum(row) / len(row))
    means.append(mean)
print("\nThe mean of every row of A is\n", means)

print(A ** 2)