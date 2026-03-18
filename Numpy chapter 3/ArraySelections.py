import numpy as np

gradeChar = np.array(["one", "two"])
gradeNum = np.array([3, 4, 5, 6, 7, 8])
grade = np.concatenate((gradeChar, gradeNum))
print(type(grade), grade)

grade[[0, 1]] = [1, 2] # replaces the first and second item wit h1 and 2 respectively
print(grade)

grade = grade.astype(int) # turns the strings into integers
print(type(grade), grade)
print(len(grade))