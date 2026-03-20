"""
Final Python Assignment
Quinten Adema
S6413943
March 20th 2026
"""

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
        print(final_sequence)
        return final_sequence

def DNA_reverse_builtin(sequence):
    reverse_sequence = (sequence[::-1])
    print(reverse_sequence)
    
         

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

    print("The input sequence contains the following amounts of nucleotides:\n", 
          "Adenine:", adenine, "\n Thymine:", thymine, "\n Guanine:", guanine, "\n Cytosine:", cytosine)
    
DNA_count("ATGCC")

#  print("Hello World"[::-1])