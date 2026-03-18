import numpy as np

n = 50
#uniform distribution of n
randomnumbers = np.random.uniform(size = n, low = 0, high = 1)
maxrandom = randomnumbers.max()
minrandom = randomnumbers.min()
sumsquaredrandom = np.sum(np.square(randomnumbers))
meanrandom = np.mean(randomnumbers)
print("The 10th random number is", randomnumbers[9])
print(randomnumbers)