"""
Chapter 4: Functions
"""
import webbrowser
import math

john_type = type("John") # this functions ssets the veriable to the string class, but is unused
print(type("John")) # this function prints the type of "John", which is a string

# webbrowser.open_new("www.rug.nl/cit/academy") opens the website in a new tab

def message(text, ornament):
    print(ornament * 50)
    print(text)
    print(ornament * 50)

message("I understand functions now!", "-")
message(text="Even better!", ornament="=") #sets text and ornament argument
message(ornament="=0=", text="Eureka!") # sets text and ornament argument, but reverse order

message("My name is Quinten", "-")

def right_justify(s, length = 70):
    print(" " * (length - len(s)) +s)

right_justify("monty", 15)
right_justify("montyyyyyyyyyyyyyyyyyyyyyyyy")

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

print("\nFor the side lengths 2 and 4, the hypotenuse is", pythagoras(2, 4))

def distance_theorem(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

print("\nThe distance between the points (1, 2) and (4, 6) is", distance_theorem(1, 2, 4, 6))

def rope_length(circumference = 40000, height = 1):
    radius = circumference / (2 * math.pi)
    rope_length = math.sqrt(radius**2 + height**2)
    return rope_length

print("\nThe length of the rope is", round(rope_length(), 2), "meters for a circumference of 40000 meters and a height of 1 meter")