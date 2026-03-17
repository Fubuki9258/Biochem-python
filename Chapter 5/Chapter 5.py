"""
Chapter 5: Conditions and Recursion
"""

def tousgrade(grade):
    if grade <= 5.5:
        return "F"
    
    elif grade >= 7.5:
        return "A"
    
    elif grade >= 6.5 and grade < 7.5:
        return "B"
    
    elif grade >= 6 and grade < 6.5:
        return "C"
    
    elif grade >= 5.5 and grade < 6:
        return "D"
    
grade = float(input("Enter your grade: "))
print("Your grade, converted to American grades is:", tousgrade(grade))
