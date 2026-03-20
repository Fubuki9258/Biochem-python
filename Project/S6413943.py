"""
Final Python Assignment
Quinten Adema
S6413943
March 20th 2026
"""

import time

def DNA_complement(sequence):
    
    """
    Accepts a string of nucleotides as input, shows the non-reverse complementary strand and returns it as a string.
    If input contains a non-nucleotide letter, shows position of wrong letter.
    """
    
    DNA_complement_list = []
    position = 0
    error = False
    
    for nucleotide in sequence:
        
        if nucleotide == "A":
            DNA_complement_list.append("T")
            position += 1
        
        elif nucleotide == "T":
            DNA_complement_list.append("A")
            position += 1

        elif nucleotide == "G":
            DNA_complement_list.append("C")
            position += 1

        elif nucleotide == "C":
            DNA_complement_list.append("G")
            position += 1
        
        elif nucleotide != "A" or nucleotide != "T" or nucleotide != "C" or nucleotide != "C":
            print("Sequence contains a non-nucleotide letter at position ", position,)
            error = True
            break
    new_sequence = ""
    if error is False:
        final_sequence = new_sequence.join(DNA_complement_list)
        print("Sequence before error is: ", final_sequence)
        return final_sequence

def DNA_reverse_for(sequence):
    DNA_reverse_for_list = []
    position = 0
    error = False

    for nucleotide in sequence:
        
        if nucleotide == "A":
            DNA_reverse_for_list.insert(0, "A")
            position += 1
        
        elif nucleotide == "T":
            DNA_reverse_for_list.insert(0, "T")
            position += 1

        elif nucleotide == "G":
            DNA_reverse_for_list.insert(0, "G")
            position += 1

        elif nucleotide == "C":
            DNA_reverse_for_list.insert(0, "C")
            position += 1
        
        elif nucleotide != "A" or nucleotide != "T" or nucleotide != "C" or nucleotide != "C":
            print("Error: Sequence contains a non-nucleotide letter at position ", position,)
            error = True
            break
    new_sequence = ""



    if error is False:
        final_sequence = new_sequence.join(DNA_reverse_for_list)
        return final_sequence

def DNA_reverse_builtin(sequence):
    reverse_sequence = (sequence[::-1])
    return reverse_sequence
    
         

def DNA_count(sequence):
    adenine = 0
    thymine = 0
    guanine = 0
    cytosine = 0

    for nucleotide in sequence:
        if nucleotide == "A":
            adenine += 1
        if nucleotide == "T":
            thymine += 1
        if nucleotide == "G":
            guanine += 1
        if nucleotide == "C":
            cytosine += 1

    print("\nThe input sequence contains the following amounts of nucleotides:\n", 
          "Adenine:", adenine, "\n Thymine:", thymine, "\n Guanine:", guanine, "\n Cytosine:", cytosine,
          "\n\nThe total number of nucleotides: ", adenine + thymine + guanine + cytosine)
    
with open(r"C:\Users\qadem\Documents\biochem\Biochem-python-2\dna_sequence.txt", "r") as f:
    dna = f.read()

t1 = time.time()
DNA_reverse_for(dna)
t2 = time.time()
for_time = t2-t1
print("For function took :", for_time, "seconds.")

t1 = time.time()
DNA_reverse_builtin(dna)
t2 = time.time()
for_time = t2-t1
print("Builtin function took :", for_time, "seconds.")

"""
Numpy statistics assignments
"""

import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

random_array = npr.random_integers(0, 10, size = 524288)
random_array = random_array.reshape(1024, 512)

row64 = random_array[64]
mean64 = sum(row64) / len(row64)

print("The mean of row 64 is:", mean64)

column128_sorted = np.sort(random_array[:, 128])
print(column128_sorted)
column128_median = (column128_sorted[256]) + int(column128_sorted[257]) / 2

print(column128_median)

column256 = random_array[:, 256]
print(column256)
plt.hist(column256, bins = 40)
plt.xlabel("Integer")
plt.title("Distribution of random integers between 0 and 10 on column 256")
plt.show()

"""
Question 3: Plotting the sin function
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10 * np.pi, 0.1)
y1 = np.sin(x)
y2 = np.sin(1.1 * x + 0.5)

plt.plot(x, y1, color="hotpink", label="f(x) = sin(x)")
plt.plot(x, y2, color="darkgreen", label="g(x) = sin(1.1x + 0.5)")
plt.legend()
plt.show()
