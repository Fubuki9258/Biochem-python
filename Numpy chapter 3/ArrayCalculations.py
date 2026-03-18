import numpy as np

x = np.array([3, 4, 5, 6])
isEven = np.array(x % 2 == 0) # checks for every value in x if it is even, if it is, returns True, else False
isThreefold = np.array (x % 3 == 0) #checks if value is divisible by 3

isEvenThreefold = np.isin([True], [isEven, isThreefold])
print(isEvenThreefold)

fruits = np.array(["Apple", "pear", "Pear", "Orange"])
isNotPear = np.array(fruits == "pear")
print(isNotPear)

x = np.concatenate([[True, False], [2, 3, 4]]) # True = 1, False = 0
y = np.concatenate([[2, 3], ["four", "five"]]) # turns numbers into strings
print(x, y)

mystring = "Apples"
mynumber = 10
mynumber = str(mynumber)
print(mystring < mynumber) # 10 comes alphabetically before Apples

x = np.array([10, 20, 30, 40, 50])
y = x[3] # y = 40
z = x[[1, 3]] # z = [20, 40]
z = x[[ - 1]] # z = 50
z = x[[ - 1, - 3, - 5]] # z = [50, 30, 10]
q = x[[True, False, False, True, False]] # q = [10, 40]
# p = x[[True, False, False, True]] WILL return an error due to incorrect array
# size

isGreaterThan29 = x > 29
print(isGreaterThan29)

s = x[isGreaterThan29]
print(s)

del (x, y)

x = np.array([[1,2,3,4], [5,6,7,8]])
print("\n", x)
xflat = x.flatten()
print(xflat)

print(xflat.reshape(2, 4))
