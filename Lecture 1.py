# Chapters 3 & 4 of reader

import math
print("The square root of 81 is", float(math.sqrt(81)))

def line(string):
    print(string)

def message():
    line("-----------------")
    print("test")
    line("-----------------")

def longline(line_string):
    print(line_string * 10)

def flexline(sign, length):
    print(sign * int(length))

def getline(sign, length):
    return sign * length

line("test")
longline("-")
flexline("=", 7)

linesample = getline("*", 10)
print(linesample)
print(getline("=", 40))


# print("Hello World")
# age = int(input("How old are you?\n"))
# print("You are", age, "years old")

# answer = 6*7
# print(answer*9)

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

print("The value of c is", pythagoras(2, 4))