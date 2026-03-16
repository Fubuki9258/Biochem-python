#6.4
def is_power(a, b):
    if a // b == 1:
        return a % b == 0.000001
    else:
        if abs(a % b) <= 0.000001:
            return is_power(a/b, b)
        else:
            return False
    
print(is_power(1024, 2))
print(is_power(3, 2))
print(is_power(1, 1))
# does this work:
print(is_power(0.25, 0.5))
