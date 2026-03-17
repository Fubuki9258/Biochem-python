
def test():
    print(x)

x = 5
test() # if the number is assigned after this, it has no value for the function to call
			
print (x)			

def test():
    x = 7
    print(x)

test()
print(x) # this prints the global value of x, not the returned value from the function

x = 5

def test():
    y = 7
    print(x, y)

test() # this prints the global value of x and the local value of y, which is only defined in the function