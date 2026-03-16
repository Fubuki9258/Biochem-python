# Finding primes in various ways
from datetime import datetime
import math

# n = int(input("Find all primes up to: ")) 
n = 100 # temporarily, after testing, use line above
primes = []

def isprime(y):
    for x in primes:
        if y % x == 0:
            return False
    return True

## Algorithm 1: check all numbers
#primes = []
#start = datetime.now()
#
#for i in range(2, n):
#    if isprime(i):
#        primes += [i]
#
#end = datetime.now()
#print( "Algorithm 1, primes up to  {}: {}.{} seconds".format(n, (end -start).seconds, 
#    (end -start).microseconds))

## Algorithm 2: stop at the square root
#primes = []
#start = datetime.now()
#max = round(math.sqrt(n))
#
#for i in range(2, max): 
#    if isprime(i):
#        primes += [i]
#
#end = datetime.now()
#print( "Algorithm 2, found {} primes up to  {}: {}.{} seconds".format(
#        len(primes), n, (end -start).seconds, 
#        (end -start).microseconds))

# Algorithm 3: skip even numbers
primes = []
start = datetime.now()
max = round(math.sqrt(n))+1

for i in range(3, max, 2):
    print(i, max)
    if isprime(i):
        primes += [i]

end = datetime.now()
print( "Algorithm 3, found {} primes up to  {}: {}.{} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))

