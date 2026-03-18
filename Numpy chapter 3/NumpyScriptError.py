import numpy as np

n = 4
# uniform distribution of n
x = np.random.uniform(size = n, low = 0, high = 1)
y = np.mean(x)

age_students = np.array([12, 16, 14, 18, 11, 19, 13, 10, 22, 14])
ageStudentsDecade = age_students / 10

print(x, y)

print(ageStudentsDecade)

modernartists = np.array(["Mondriaan", "Röling"])
# dtype <U6 indicates that the longest string will be 6 characters long
# if <U2 was used, Python would be come Py
programminglanguages = np.array(["Python", "R"], dtype="<U6")

print(programminglanguages)

sometimesTrue = np.array([True, False])

x = np.array([0, 1, 2, 3, 4, 5, 6])
x = np.array(range(7))

isEven = x % 2 == 0
isOdd = x % 2 == 1

x = np.array([0, 1, 2, 3])
y = np.array([3, 2, 1, 0])
z = x < y # checks every value for y, returns True if value is larger than the same position in x
print(z)

y = np.array([4, 5, 6, 7])
print(np.isin(2, x)) # checks if x contains the value 2, returns True if found

print(np.isin([2, 5], [x, y])) # checks the values 2 and 5 in both x and y

veryTrue = True + True # True = 1, False = 0, this returns 2
print(veryTrue)

x = np.array([0, 1, 2, 3])
y = np.array([3, 2, 1, 0])
z = x < y # returns True True False False, which equals 2
s = np.sum(x < y) # instead of returning True / False, returns the sum of the conditions (being 2)
print(z, s)