import numpy as np

numbers = np.array(range(1, 6))
print(numbers)

print(np.sum(numbers))

array10 = np.array([10] * 5)
sum10 = numbers + array10
print(np.sum(sum10))

print(np.square(numbers))

print(np.sqrt(numbers))

print(np.square(np.square(numbers)))