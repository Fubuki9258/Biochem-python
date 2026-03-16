#Find the longest word in a file
fin = open("t:/ENwords.txt")

palindromes = []
n = 0
for line in fin:
    word = line.strip()
    if word.upper() == word[::-1].upper():
        palindromes.append(word)
        n += 1
print(palindromes)