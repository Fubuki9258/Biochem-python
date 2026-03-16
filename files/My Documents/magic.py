#Creating a magic square

def magic_square(n):
    """
    generates and prints a magix square of size n * n
    n must be a positive odd integer
    a grid (list of lists) with the square is returned
    """
    
    row = [] 
    grid = []
    
    for i in range(n):  # create a row with n item s
        row.append(None)
    for i in range(n):  # built a table/grid of n rows
        grid.append(row.copy()) # grid.append(row) would just add an alias to row!
    
    r = (n+1)//2 -1# the row number-1, because of numbering from 0
    c = n -1 # the column number
    maxnr = n**2
    nr = 1 # the starting integer
    
    while nr <= maxnr: # continue as long as not all cells are filled
        if grid[r][c] == None: 
            grid[r][c] = nr
            if c == n-1 and r == 0:
                c = n-2
            else:
                if c<n-1:
                    c += 1
                else:
                    c = 0
                if r>0:
                    r -= 1
                else:
                    r = n-1
            nr += 1  # next number
        else: # if the destination was not empty
            if c>1:
                c -= 2
            else:
                c = n-1
            if r<n-1:
                r += 1
            else:
                r = 0
            # try again with the same number
            
    for i in range(n): 
        for j in range(n): 
            print("{:4d}".format(grid[i][j]), end="") # no line breaks
        print() # to get a line break
    return grid

def check_list(series):
    n = len(series)
    required = int(n * (n*n + 1)/2) # int is essential for comparison below
    sum = 0
    for cell in series:
        sum += int(cell)
    return sum, required

def check_magic_square(grid):
    """ check sum of all rows, columsn and diagonals """
    
    n= len(grid)
    msg = ""
    # check rows
    for row in grid:
        sum, required = check_list(row)
        if sum != required:
            msg = msg + "Row {} has sum {} instead of {}\n".format(
                    row, sum, required)
        else:
            msg = msg + "Row {} has sum {}: OK\n".format(row, sum) 

    # check columns
    for j in range(n): # columns
        series = []
        for i in range(n): # rows
            series += [grid[i][j]]  #column j of row i, remember the outer []
        sum, required = check_list(series)
        if sum != required:
            msg = msg + "Column {} has sum {} instead of {}\n".format(
                    series, sum, required)
        else:
            msg = msg + "Column {} has sum {}: OK\n".format(series, sum) 

    # check diagonal1
    series = []
    for i in range(n): 
        series += [grid[i][i]]  #column i of row i
    sum, required = check_list(series)
    if sum != required:
        msg = msg + "Diagonal {} has sum {} instead of {}\n".format(
                series, sum, required)
    else:
        msg = msg + "Diagonal {} has sum {}: OK\n".format(series, sum) 

    # check diagonal2
    series = []
    for i in range(n): 
        series += [grid[i][n-i-1]]  #column n-1 of row i
    sum, required = check_list(series)
    if sum != required:
       msg = msg + "Diagonal {} has sum {} instead of {}\n".format(
                series, sum, required)
    else:
        msg = msg + "Diagonal {} has sum {}: OK".format(series, sum) 
        
    return msg

# After testing, line 6 will be removed and 4 will be acivated instead
# n = input("Size of the square (odd positive integer):")
# It ought to be checked whether the value is an odd positive integer
n=5 
# The magic square will be stored in a list.
# As the elements of the list count from 0,
# you have to to correct for that.

#print(check_magic_square(magic_square (5)))

# while debugging, it is easier to see intermediate results
# after that, the next three lines might be removed
# and the previous one 'uncommented'
grid = magic_square (n)
result = check_magic_square(grid)
print(result)


        
    

