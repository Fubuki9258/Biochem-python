number = input("Enter a number: ")
if number.isdigit():
    number = int(number)  
    
    if number == 0:
        print("You entered zero.")

    elif number < 0:
        print("You entered a negative number.")

    elif number > 0:
        while number>0: # if >= 0, 0 will also be counted
            print(number)
            # if number -=1 was missing, the loop would nevery turn off
            number -= 1 # same as number = number - 1

else:
    print("You entered something that is not an integer.")