# List comprehension
 
numbers = [2, 4, 7, 10]
squares = [x**2 for x in numbers]

my_range = range(1000)
odd_numbers = [x for x in my_range if x % 2 == 1]
odd_numbers2 = [x for x in range(1000) if x % 2 == 1]	

row_zero = [0 for y in range(3)]	

       