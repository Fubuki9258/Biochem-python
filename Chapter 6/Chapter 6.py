"""
Chapter 6: Iteration
"""

"""
When we started the simulation, we have 1000 pigs
In later years the supply will be dependant on last year's price:
supply = 500 + previous_price * 8

The new price will be determined by the supply
price = int((5000-supply)/10) (rounded down to the nearest integer)
"""


year = 0
supply = 1000
price = int((5000-supply)/10)

for i in range(60):
    old_supply = supply #sets the supply to the current supply before it calculates it for the current year
    print("Year:", year, "Supply:", supply, "Price:", price)
    year += 1
    supply = 500 + price * 8
    price = int((5000-supply)/10)

    if supply == old_supply:
        print("The supply has stabilized for two years at", supply, "pigs.")
        break

def pi(iterations=100):
    """
    Approximates pi, to the given number of iterations.
    The formula used is 4 * (1/1 - 1/3 + 1/5 - 1/7 + 1/9 ...)
    """
    approx = 0.0
    for i in range(iterations):
        denominator = 2 * i + 1
        term = 1.0 / denominator
        if i % 2 == 0: # if i is even, add the term
            approx += term
        else: # if i is odd, substract the term
            approx -= term

    return 4.0 * approx

print("Approximation of pi with 10000 iterations:", pi(10000))