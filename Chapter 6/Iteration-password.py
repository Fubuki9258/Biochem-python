password = "RealPassword!"

for i in range(3):
    guess = input("Enter the password: ")
    if guess == password:
        print("Correct password! Access granted.")
        break
    else:
        if i == 2:
            print("Too many incorrect attempts. Access denied.")
        else:
            print("Incorrect password. Try again.")
