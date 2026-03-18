"""
Chapter 7: Error Handling and Debugging
"""

denominator = float(input("Denominator: "))
print("1 divided by", denominator, "is", 1/denominator)

"""
This can also be done by if else statement
"""

try:
    denominator = float(input("Denominator: "))
    print("1 divided by", denominator, "is", 1/denominator)

except ValueError:
    print("You did not enter a number.")

