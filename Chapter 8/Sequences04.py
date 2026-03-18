def circle_info(r):
    """returns (circumference, area) of a circle of radius r 
    """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return "circumference=" + str(c), "area="+ str(a)

print(circle_info(10))
      