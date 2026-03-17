name = "John"
average_grading = 7
age = 23
# only persons between age 18 and 80 are accessed to this school,
# unless their average grading was above 8.5, than they get free access
has_access =  age >= 18 and age <= 80 or float(average_grading) >= 8.5# complete this line to test if this person is accessible
# complete the program
if has_access ==True:
    print(name, "has access")

elif has_access == False:
    print(name, "does not have access")