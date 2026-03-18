"""
Chapter 8: Sequences
"""

various = ["John", 42, True, [1, 2, 3]] # creates a list containing 4 variables
print(various[1]) # prints the second item from the list, 42

tuple1 = ("string 1", "string 2", "string 3", "string 4")
print(len(tuple1))
print(len(tuple1[1]))

list1 = ["John", 42, True]
list1 += (1, 2, 3)

print(list1)

list2 = ["John", 42, True]
list2.insert(3, [1, 2, 3])

print(list2)

list3 = ["John", 42, True]
list3 += [1]

print(list3)

tuple = ("John", 42, True)
tuple += (1, 2, 3)

print(tuple)

wordlist = ["word1", "word2", "word3"]
newwordlist = []
for word in wordlist:
    x = word.upper()
    newwordlist.append(x)
    
print(newwordlist)

placement= [[3,"Marie"], [1,"Sara"], [2,"Mark"], [4,"Emilie"]]
placement.sort()
print(placement[0:3])