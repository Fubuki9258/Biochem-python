condition = True

while True:
    number = float(input("Number: "))
    print(number ** 2)
    ans = input("Square another number? Y/N: ").strip().lower()
    if ans == 'n' or ans == "no":
        break
    