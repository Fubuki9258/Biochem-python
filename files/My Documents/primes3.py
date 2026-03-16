# Finding primes in various ways
from datetime import datetime
import math

# n = int(input("Find all primes up to: ")) # try 100000
n = 10000 # temporarily, after testing, use line above
primes = []

def isprime(y):
    for x in primes:
        if x > math.sqrt(y): # stop at squareroot(y)
            return True
        if y % x == 0:
            return False
    return True
    
primes = []
start = datetime.now()

for i in range(3, n, 2):
    if isprime(i):
        primes += [i]

end = datetime.now()
print( "Algorithm 3, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))


