#Check a file name
filename = input("File (including path):")

fin = open(filename)

n = 0
for line in fin:
    n += 1

print("File", filename, "contains", n, "lines")