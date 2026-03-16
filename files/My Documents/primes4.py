# Finding primes in various ways
from datetime import datetime

# n = int(input("Find all primes up to: ")) # try 100000
n = 1000000 # temporarily, after testing, use line above

primes = []

# generate a list for all candidates that indicates if they have been checked
# we will simply neglect the existence of checked[0]
start = datetime.now()

checked = [] 
for i in range(n+1):
    checked += [False]
   
for i in range(2, n+1): # 1 is not a prime, so we start at 2
    if not checked[i]: # it must be a prime!
        primes += [i] # add it to the list of found primes
        for j in range(i, n+1, i): # find all multiples of this prime
            checked[j] = True # and mark them as checked

end = datetime.now()
print( "Algorithm 4, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))


