# List comprehension
 
numbers = (2, 4, 7, 10) # still works as a tuple, since new lists are created for the other variables
squares = [x**2 for x in numbers] # likely returns [4, 16, 49, 100]

my_range = range(1000)
odd_numbers = [x for x in my_range if x % 2 == 1] # [] = all odd numbers from 0 - 999
odd_numbers2 = [x for x in range(1000) if x % 2 == 1]	# same thing

row_zero = [0 for y in range(3)]	# [0, 0, 0]

print(squares, odd_numbers, odd_numbers2, row_zero)  

# creates a list [0, 0, 0] 4 times in a big list
grid = [[0 for x in range(3)] for y in range(4)]
print(grid)