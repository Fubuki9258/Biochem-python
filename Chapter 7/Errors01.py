#error trapping

number = input("How many? ")

try:
    number = int(number)
    print("You entered", number)

except ValueError:
    print("You did not enter a number")


def isnum(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

isnumber = input("Enter a number: ")
print("Is it a number?", isnum(isnumber))
