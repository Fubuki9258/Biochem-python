name = "John"
average_grading = float(input("Average grading: "))
age = int(input("Age: "))
# only persons between age 18 and 80 are accessed to this school,
# unless their average grading was above 8.5, than they get free access
has_access = age >= 18 and age <= 80 or float(average_grading) >= 8.5 # complete this line to test if this person is accessible
print(name, "has access:", has_access)
