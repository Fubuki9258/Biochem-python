number = int(input("Enter a whole number: "))

is_even =  number % 2 == 0    # complete this line to test if number is even

if number >= 1000:
    condition = "too large"

elif number == 0: 
    condition = "zero"

elif is_even == True:
    condition = "even"

elif is_even == False:
    condition = "odd"

else:
    condition = "not an integer"

print(number, "is", condition) # only works for integers, not floats