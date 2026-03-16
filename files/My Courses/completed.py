
#%% 3.2 Variables, assignment:
#Basics01.py
length = 40  #cm
width = 20  #cm
area = length * width
print(40*20)  #result of calculation is printed
print(length * width)  #values of variables are used
print(area) #value of area is printed
print("The area is:", area)  #combining values in one print
print("Half of the area is:", area/2)  #why is the result 400.0 instead of 40
print("The area divided by 81 is:", area/81)  #showing the precision

# Modify this program to calculate and print the volume of an aquarium 
# of this length and width, and 15 cm height
length = 40  #cm
width = 20  #cm
height = 15
volume = length * width * height
print(volume) #value of volume is printed
print("The volume is:", volume)  #combining values in one print

#%% 3.3 Values, Strings:
#Basics02.py
print("1.\titem \"1\"\n2.\titem \"2\"")

#%% 3.3.Values, String operators
#Basics03.py
firstname = "John"
lastname = "Doe"
print("*"*6, "My name is", firstname, lastname,"*"*6)
#or:
print("*"*6 + " My name is " + firstname + " " + lastname + " " + "*"*6)

#%% 3.4 Basic input and output, basic input
#Basics04.py
length = float(input("Length? "))
width = float(input("Width? "))
area = length * width
print("The area is:\n", area) 

#there are many variants, e.g.:
length = input("Length? ")
width = input("Width? ")
area = float(length) * float(width)
print("The area is:\n", area) 

#or even:
print("The area is:\n", float(input("Length? ")) * float(input("Width? "))) 

#%% 3.6 Exercises
#Think Python, 2.10, 2.2.1:
import math

r = float(input("radius of sphere (in cm): "))
volume_sphere = 4/3 * math.pi * r
print("Volume =",volume_sphere, "cm3")

#Think Python, 2.10, 2.2.2:
bookprice = 24.95
discount = 40/100 # 40% = 40/100
shippingcost_first = 3
shippingcost_rest = 0.75
number_copies = 60
books_cost = number_copies * bookprice * (1-discount) # 1 - discount = 60%
shipping = shippingcost_first + ((number_copies -1) *shippingcost_rest)
wholesale = books_cost + shipping
print("$", wholesale)
#Or, friendlier, after rounding:
print("Wholesale cost of", number_copies, "books is $", round(wholesale, 2))

#%% 4.1, Function fundamentals, Built-in functions
type("John") # wrong: type yields an answer and nothing is done with it
print("John") # OK: print does not yield a result, but simply does something
#int() simply drops the decimals, round() really rounds a number

#%% 4.2 User-defined functions, Defining a function
# Functions01.py
def line(char):
    print(char * 40)

line("*")
line("=") # prints a line of equal signs

def varline(char, length): # line of variable length
    print(char * length)

short=20
varline("*", 80)
varline("|=", short) # accepts a variable
varline("=", 3*short) # accepts a formula

def fixedline(): # simple line of 50 stars
    print("*" * 50)

fixedline()

def autoline(char="*", length=50): # default line of default length
    print(char * length)

autoline()
autoline("*", 80)
autoline("|=", short) # accepts a variable
autoline("=", 3*short) # accepts a formula
#%% 4.2 User-defined functions, Returning a value
# Functions02.py
def twice(number):
    result = 2 * number
    return result

print(twice(5))

def shorttwice(number):
    return 2 * number

print(shorttwice(5))

def CtoF(celsius):
    return celsius * 9/5 + 32

print("37°C =", CtoF(37))

#%% 4.3 Exercises
# Pythagoras
import math

def pyth(a, b):
    return math.sqrt(a**2 + b**2)

#alternative, that does not need math: square root is raising to the power 0.5
def pythAlt(a, b):
    return (a**2 + b**2)**0.5
    
#testing with a known triangle
a=3
b=4
print("When a=", a, "and b=", b, "then c=", pyth(a, b))
print("When a=", a, "and b=", b, "then c=", pythAlt(a, b))

#Distance
def dist(x1, y1, x2, y2):
    return ((y2-y1)**2+(x2-x1)**2)**0.5

x1=0
y1=0
x2=1
y2=1
distance=dist(x1, y1, x2, y2)

# Rope: 
def circumference(radius):
    return 2* 3.14159 * radius

def radius(circumference):
    return circumference / 2 / 3.14159 	# why not circumference / 2*3.14159 ?

earth_circ = 40000 * 1000 # meters
earth_radius = radius(earth_circ)
rope_radius = earth_radius + 1
rope_circ = circumference(rope_radius)
print(rope_circ)

# Just an alternative, as there may be many:
import math

def circumference (extra):
    earth_r = 40000 / (2 * math.pi)
    return 2* math.pi * (earth_r + (extra/1000))
    
extraradius = input("How many meters should your rope be above the earth surface? ")
print ("You need a rope", circumference (float(extraradius)), "kilometers long")

#%% 5.1 Comparing, Boolean variables
# Conditions02.py
number = 7
is_even = number%2==0     # complete this line to test if number is even
print(number, "is even", is_even)

def iseven(number):
    return int(number)%2==0  # make sure it is an integer

num = input("Integer number: ")
print(num, "is even?",iseven(num))

#%% 5.1 Comparing, Combining comparisons
# Conditions03.py
name = "John"
average_grading = input("Average grading: ")
age = 123
# only persons between age 18 and 80 are accessed to this school,
# unless their average grading was above 8.5, than they get free access
has_access =  18<=age<=80 or float(average_grading)>8.5
# alternative:
# has_access =  age>=18 and age<=80 or float(average_grading)>8.5
print(name, "has access:", has_access)

#%% 5.2 Conditional processing, Do or don't
# Conditions04.py
number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))
if number1 > 0 and number2>0:
    print(number1, "and", number2, "are both positive")
print(number1, "and", number2, "have both been investigated")
#%% 5.2 Conditional processing, Do one thing or the other
# Conditions05.py
name = "John"
average_grading = 7
age = 23
# only persons between age 18 and 80 are accessed to this school,
# unless their average grading was above 8.5, than they get free access
has_access =  18<=age<=80 or float(average_grading)>8.5
# complete the program
if has_access:
    print(name, "has access")
else:
    print(name, "does not have access")
#%% 5.2 Conditional processing, Many options
# ConditionsCheck.py

number = float(input("Number: "))

if number<1000:
    if number<0:
        print(number, "is negative")
    elif number==0:
        print(number, "is zero")
    if number>0:
        print(number, "is positive")
else:
    print("Only numbers smaller than 1000 are accepted")    

#%% 5.3 Recursion, Repeating by recursion
# Conditions06.py
wish = "Hurrah!"

def salvo(n, message):  # fine, except for n=0 
    print(message)
    if n>1:
        salvo(n-1, message)

def finesalvo(n, message):  # fine, even for n=0 
    if n>0:
        print(message)
        if n>1:
            salvo(n-1, message)
    
salvo (3, wish) # OK
salvo (0, wish) # not OK

finesalvo (3, wish) # OK
finesalvo (0, wish) # OK

#%% 5.4 Exercises

def tousgrade(grade):
    if 8.5 <= grade <=10:
        return "A"
    elif grade >= 7.5: # or: elif grade==7.5 or grade==8
        return "B" 
    elif grade >= 6.5: # or: elif grade==6.5 or grade==7
        return "C"
    elif grade >=5.5:
        return "D"
    else:
        return "F" 
    
print(tousgrade(3))
print(tousgrade(9))
print(tousgrade(5.5))

#%% 5.4 Exercises

def gcd(i1, i2):
    # gcd only applies to integers, so you might want to check first:
    if not (isinstance(i1, int)) and (isinstance(i2, int)):
        print("\nBoth numbers must be integers!")
    else: 
        # determining the largest
        if i1>=i2:
            largest = i1
            smallest = i2
        else:
            largest = i2
            smallest = i1
        # According to Euclid:
        if largest % smallest == 0:
            return smallest
        else:
            return gcd(smallest, largest%smallest)
    
print(gcd(4, 12))
print(gcd(54, 94))
print(gcd(12, 4))

# but look at this simplified function! How come that it works as well?
def gcd2(small, big):
    remainder= big % small
    if remainder == 0:
        return small
    else:
        return gcd(small, remainder)

print(gcd2(4, 12))
print(gcd2(54, 94))
print(gcd2(12, 4))

#%% 5.4 Exercises
#Think Python, 5.1    
import time
print(time.time())
print(time.gmtime(0))
print(time.gmtime())
print(time.localtime())
print(time.strftime("%a %d %B %Y, %H.%M"), time.time()/24/60/60)


#%% 5.4 Exercises
#Think Python, 5.2

def check_fermat(a, b, c, n):
    print(str(a) + "^" + str(n) + " + "  + str(b) + "^" + str(n) + " =? " 
          + str(c) + "^" + str(n))
    print(str(a**n + b**n) + " =? " + str(c**n))
    if (n>2) and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that does not work.")
        
def fermat():
    a = int(input("First integer:"))
    b = int(input("Second integer:"))
    c = int(input("Third integer:"))
    n = int(input("Power (integer >2):"))
    check_fermat (a, b, c, n)

fermat()


#%% 5.4 Exercises
#Think Python,5.3

def is_triangle(a, b, c):
    if a>b+c or b>a+c or c>a+b:
        print("No, not a triangle")
    else:
        print("Yes, a triangle!")
        
def triangletest()        :
    a = int(input("First length:"))
    b = int(input("Second length:"))
    c = int(input("Third length:"))
    is_triangle(a, b, c)
    
triangletest()


#%% 6.1, Simple repetition: the for loop, range()
#Iteration01.py
number = float(input("Number? "))

for i in range(1, 11):
    print(i, "*", number,"=", i*number)
    
    
#%% 6.2, Conditional iteration: the while-loop, Condition beforehand
#Iteration03.py
    
number = int(input("Type an integer number: "))
while number>0:
    print(number)
    number = number - 1


#%% 6.2, Conditional iteration: the while-loop, Condition afterwards
#Iteration-password.py
    
password = "s3cret"

while True:
    pw = input("Password: ")
    if pw == password: 
        break

#short alternative:
while input("Password: ")!= password: 
    print("Wrong password, try again!")

#No more than 3 attempts; many variations possible
number = 3
while number>0:
    pw = input("Password: ")
    number -= 1
    if pw == password: 
        break
if number<=0: # detemine what was the cause of exiting the loop
    print("No more retries.")
else:
    print("the program continues")
    
#alternative   
for i in range(3):
    pw = input("Password: ")
    if pw == password: 
        break
if pw != password: # detemine what was the cause of exiting the loop
    print("No more retries.")
else:
    print("the program continues")
    # rest of the program
    
# Or, using a function
def passwordOK(number):
    while number>0:
        pw = input("Password: ")
        number -= 1
        if pw == password: 
            break
    return pw == password

if passwordOK(3):
    print("the program continues")
    # rest of the program
    
#%% 6.3, Excercises
# Pig market

#Full question:
    #Far, far away, in Utopia, every year a number of pigs is sold on the market. If in the previous year the price was good, farmers breed more pigs, which lowers the price, which in turn makes the farmers breed fewer pigs, and so on. It turns out that the economic formulas to approximate this trade are:
# When we start our simulation, the supply is 1000 pigs.
# The new price will be determined by the supply: Price = (5000- Supply) // 10 (Utopians only have Utopian dollars, no dollar cents. That is why integer division (//) is used instead of “normal” division (/)).
# The supply of each following year will be dependent on last year's price: Supply = 8 * PreviousPrice + 500
#Write a program to simulate this market for at most 60 years, but stop when the Supply is constant for two subsequent years.
 
supply_next_year = 1000
for year in range(1, 60):
  #calculate and report on current year
    current_supply = supply_next_year
    currentprice = int((5000-current_supply) / 10)
    print (year, "\tsupply:", current_supply, "\tprice:", currentprice) 
  #prepare for next year
    supply_next_year = 500 + currentprice * 8 
    if supply_next_year == current_supply: 
        break
#final report
print("On year ", year, "and year ", year +1, "the supply was", current_supply)

    

#%% 6.3, Excercises
#Apprentice Exercise 8.2 p.115

def incommon(string1, string2):
    n = 0
    for letter1 in string1:
        for letter2 in string2:
            if letter1==letter2:
                n += 1
    return n            

print(incommon("beer", "pears")) # also counts repeated letters
                
#Or, skipping previously found letters:
def incommonstrict(string1, string2):
    # can be simplified using string methods (see chapter on Sequences)
    n = 0
    alreadyfound="" # keeps track of previously found letters
    for letter1 in string1:
        # check if letter1 was found previously
        isfound = False
        for letterfound in alreadyfound:
            if letter1==letterfound:
                isfound=True
        if not isfound: # only continue if not found already
            for letter2 in string2:
                if letter1==letter2:
                    n += 1
                    alreadyfound=alreadyfound + letter1
    return n            
                
print(incommonstrict("beer", "pears")) # skips all previous letters               


#%% 6.3, Excercises
# Apprentice, Exercise 8.3, p. 115
    
import math

def pi(n):      # there are many variations
    pi_approx = 1
    for i in range(3, 2*n+1, 4):
        pi_approx -= 1/i 
    for i in range(5, 2*n+1, 4):
        pi_approx += 1/i 
    return 4 * pi_approx

print(pi(1))   
print(pi(10))   
print(pi(100))        
print(pi(1000))        
print(pi(10000))        
print("The 'real' pi = ", math.pi)

   
#%% 6.3, Exercises
#Think Python 7.9, exercise 7.2

def eval_loop():
    while True:
        expression = input("Expression (type 'done' to stop): ")
        if expression == "done":
            break
        print(eval(expression))
        
eval_loop()


#%% 7.3 Run-time errors, Exception handling
# Errors01.py 

#error trapping

try:
    number = int(input("How many? ")) #mind that a ) was missing as well!
except:
    print ("This was not a valid integer number, 0 is assumed")
    number=0
print("The program continues")


def isnum(s):
    try:
        n = float(s) # n is never used, just created to test if s is numerical
        return True
    except:
        return False
    
print(isnum("3.14"))

#%%8.1 What are sequences,strings
# Strings01.py

name="John Doe"

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index # also breaks the loop
        index += 1
    return -1

# at least, test the extremes
print(find(name, "J"))
print(find(name, "e"))
print(find(name, "x"))

# alternative:
def find1(word, letter):
    index = 0
    while True: # basically: never stop
        if word[index] == letter:
            return index # also breaks the loop
        index += 1
        if index == len(word): # the last character has been passed
            return -1 # also breaks the loop

# at least, test the extremes
print(find1(name, "J"))
print(find1(name, "e"))
print(find1(name, "x"))

# using a for loop
def find2(word, letter):
    index = 0
    for char in word:
        if char == letter:
            return index # also breaks the loop
        index += 1
    return -1

# at least, test the extremes
print(find2(name, "J"))
print(find2(name, "e"))
print(find2(name, "x"))

# alternative, using a for loop
def find3(word, letter):
    for index in range(len(word)):
         if word[index] == letter:
            return index # also breaks the loop
    return -1

# at least, test the extremes
print(find3(name, "J"))
print(find3(name, "e"))
print(find3(name, "x"))

# alternative: similar, but not what was requested
def find4(word, letter):
    for char in word:
         if char == letter:
            return char # also breaks the loop
    return -1

# at least, test the extremes
print(find4(name, "J"))
print(find4(name, "e"))
print(find4(name, "x"))
        
    
#%% 
# Think Python, p. 75

def findStartAt(word, letter, start=0):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index # also breaks the loop
        index += 1
    return -1

print(findStartAt('banana', 'b'))
print(findStartAt('banana', 'b', 1))
print(findStartAt('banana', 'x'))
print(findStartAt('banana', 'x', 10))

def count(word, letter):
    nr = 0
    for char in word:
        if char == letter:
            nr = nr + 1
    return nr

word = 'banana'
print(count(word,'b'))
print(count(word,'a'))
print(count(word,'x'))

# alternative, using findStartAt
def count2(word, letter):
    nr = 0
    index = findStartAt(word, letter, 0)
    while index != -1:
        nr += 1
        index = findStartAt(word, letter, index+1)
    return nr

word = 'banana'
print(count2(word,'b'))
print(count2(word,'a'))
print(count2(word,'x'))

#%% 8.2 Common features, Length
names = ("John", "Joe", "Jane", "Joan")
print (len(names))
print (len(names[1]))

#%% 8.2 Common features, Concatenation

elem = [1, 2, 3]
various1 = ["John", 42, True] +  elem
various2 = ["John", 42, True] +  [elem]
various3 = ["John", 42, True] +  [1, 2, 3]
various4 = ["John", 42, True] +  [[1, 2, 3]]

print(elem + "John")
print(elem + ["John"])

#%% 8.2 Common features, Repeating

zerolist = [0] * 10

#%% 8.2 Common features, Slices

diverse = ("John", 42, True, (1, 2, 3))
print(diverse[1:2])

# alternative:
print(("John", 42, True, (1, 2, 3))[1:2])

name = "John Doe"
new_name = name[0:2] + "a" + name[3:99] # [3:8] is more neat, but 99 works as well
name = name[0:2] + "a" + name[3:99] # overriding name works fine


# Sequences01.py
various = ["John", 42, True, [1, 2, 3]]
last_part1 = various[2:]
last_part2 = various[2:-1]
only_one1 = various[2]
only_one2 = various[2:3] # only the third element
completecopy = various[:] # a copy of all elements

various = ("John", 42, True, [1, 2, 3])
last_part1 = various[2:]
last_part2 = various[2:-1]
only_one1 = various[2]
only_one2 = various[2:3] # only the third element
print(only_one2)
completecopy = various[:] # a copy of all elements

#%% 8.2 Common features, Membership

isTupleMember = (2, 3) in (1, 2, 3)
areBothMembers = 2 in (1, 2, 3) and 3 in (1, 2, 3)

#%% 8.2 Common features, Traversing (for)

name = "John"
teststring = "on"

allfound=True

for char in teststring:
    isfound=False
    
    for letter in name:
        if char == letter:
            isfound = True
            break  # optional: after finding it once, you might stop this loop
    if not isfound:
        allfound = False
        break # if one is missing, then continuing is useless

print(allfound)

# or, in a function:

def allCharactersPresent(text, lookfor):
    allfound=True
    
    for char in lookfor:
        isfound=False
        
        for letter in text:
            if char == letter:
                isfound = True
                break  # optional: after finding it once, you might stop this loop
        if not isfound:
            allfound = False
            break # if one is missing, then continuing is useless
    return allfound
 
print(allCharactersPresent("John", "on"))

#%% 8.3 Strings, String comparison
# Strings02.py

# corrected version:

while True:
    number = input("Number: ")
    print(float(number) ** 2)
    if input("Square another number? Y/N: ") != "Y":  # or == "N"; difference?
        break

# case insensitive:

while True:
    number = input("Number: ")
    print(float(number) ** 2)
    answer = input("Square another number? Y/N: ")
    if answer.upper() != "Y":
        break

# or even:

while True:
    print(float(input("Number: ")) ** 2)
    if input("Square another number? Y/N: ").upper() != "Y":
        break


# only first character:

while True:
    number = input("Number: ")
    print(float(number) ** 2)
    answer = input("Square another number? Y/N: ")
    if answer.upper()[0] != "Y":  # or: answer[0].upper()
        break

#%% 8.3 Strings, String comparison
# Think Python, Exercise 8.4 (p.80)
        
# islower is a string method: only True if the entire string is lowercase
        
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1("john")) 
print(any_lowercase1("John")) 
print(any_lowercase1("JOHN doe")) 
print(any_lowercase1("J. DOE")) 
print(any_lowercase1("john DOE")) 
# WRONG, because this function stops after the first character  

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print(any_lowercase2("john")) 
print(any_lowercase2("John")) 
print(any_lowercase2("JOHN doe")) 
print(any_lowercase2("J. DOE")) 
print(any_lowercase2("john DOE")) 
# WRONG, checks the literal string "c", not the variable c
        
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

print(any_lowercase3("john")) 
print(any_lowercase3("John")) 
print(any_lowercase3("JOHN doe")) 
print(any_lowercase3("J. DOE")) 
print(any_lowercase3("john DOE")) 
# WRONG, because it returns only whether the last character is lowercase

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag

print(any_lowercase4("john")) 
print(any_lowercase4("John")) 
print(any_lowercase4("JOHN doe")) 
print(any_lowercase4("J. DOE")) 
print(any_lowercase4("john DOE")) 
# WRONG: return will leave the loop after the first c

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True

print(any_lowercase5("john")) 
print(any_lowercase5("John")) 
print(any_lowercase5("JOHN doe")) 
print(any_lowercase5("J. DOE")) 
print(any_lowercase5("john DOE")) 
# WRONG, because this function stops after the first character       

# Correct example; many possible alternatives:     
def any_lowercase6(s):
    for c in s:
        if c.islower():
            return True
    return False    

print(any_lowercase6("john")) 
print(any_lowercase6("John")) 
print(any_lowercase6("JOHN doe")) 
print(any_lowercase6("J. DOE")) 
print(any_lowercase6("john DOE")) 


#%% 8.3 Strings, String comparison
# Think Python, Exercise 8.5 (p.80)

def basic_rotate_word(word, nr):
    newword = ""
    for letter in word:
        newword = newword + chr(ord(letter)+nr)
    return newword

print(basic_rotate_word("IBM", -1))
print(basic_rotate_word("HAL", 1))
print(basic_rotate_word("cheer", 7))

# this version does not wrap around at beginning or end of the alphabet
# This one does:
# http: // thinkpython2. com/ code/ rotate. py .

#%% 8.3 Strings, String formatting
# Strings03.py

gimmick=150
gadget=1.75
widgets_3_pack=100
print("PRODUCT     PRICE")
print("{0:>11s} {1:6.2f}".format("Gimmick:", gimmick))
print("{0:>11s} {1:6.2f}".format("Gadget:", gadget))
print("{0:>11s} {1:6.2f}".format("Widget:", widgets_3_pack/3))

# Alternative:
print(("PRODUCT     PRICE\n{0:>11s} {1:6.2f}\n{2:>11s} {3:6.2f}\n{4:>11s} " +
      "{5:6.2f}").format("Gimmick:", gimmick, "Gadget:", gadget,"Widget:", 
       widgets_3_pack/3))
# Mind the parentheses around the (split) formatting string! Try without.


#%% 8.4  Lists, Exercise

def allupp(wordlist): # a list is always called by reference!
    for i in range(len(wordlist)):
        wordlist[i]=wordlist[i].upper() # original list itself is modified
        
# alternative:
def allupp2(wordlist):
    for i in range(len(wordlist)):
        wordlist[i]=wordlist[i].upper()
    return wordlist

# This might seem easier, but does not work:
def allupp3(wordlist):
    for word in wordlist:   # word is a local variable
        word = word.upper() 
    # words is not returned nor modified anywhere
        
words = ["John", "was", "here"]
print(id(words))
allupp(words) # call by reference: modify words in-place
print(words)
print(id(words)) # same memory location

words = ["John", "was", "here"]
print(id(words))
words = allupp2(words)
print(words)
print(id(words))

words = ["John", "was", "here"]
print(id(words))
words2 = allupp2(words) # words2 becomes an alias to words
print(id(words2))

words = ["John", "was", "here"]
print(id(words))
allupp3(words)
print(words)
print(id(words))

#%% 8.6 Conversion, List or tuple to string

def circle_info(r):
    """returns (circumference, area) of a circle of radius r 
    """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return ("circumference=" + str(c), "area="+ str(a))
# the returned value is a tuple containing strings
# the outer parentheses are not needed
    
print("{:>25s}\n{:>25s}".format(*circle_info(10)))
# As "circumference=<value>" is returned as a fixed string, 
# this format is hard to change; it must be split first,
# or the function should return the texts and the values separately
# We will not do this now

#%% 8.6 Conversion, Tuple or string to list

print("Red, Green, Light Blue".split(",")) 	#["Red", " Green", " Light Blue"]
print("Red, Green, Light Blue".split(", ")) 	#["Red", "Green", "Light Blue"]

# 8.6 Strings05.py
sentence = """John asked: 
\"How many      words are there in this sentence\"?"""

def split_into_words(text):
    temp = text.replace(":", " ")
    temp = temp.replace("\n", " ")
    temp = temp.replace("\"", " ")
    temp = temp.replace("\'", " ")
    temp = temp.replace(",", " ")
    temp = temp.replace(";", " ")
    temp = temp.replace(".", " ")
    temp = temp.replace("\\", " ")
    temp = temp.replace("\t", " ")
    temp = temp.replace("?", " ")
    temp = temp.replace("!", " ")
    return temp.split()

print(split_into_words(sentence))

#Alternative:
def split_into_words(text):
    specialchars = ":\n\"\',;,\\\t?!"
    for letter in specialchars:
        text = text.replace(letter, " ")
    return text.split()

print(split_into_words(sentence))
print(len(split_into_words(sentence)))

#%% 8.6 Exercises (Conversion )
# Sequences07.py

myList = ["I", "was a", "List"]
myTuple = ("I", "was a", "Tuple")
myString = "I was a string"

#Tuple and List swap
tupleFromList=tuple(myList)
listFromTuple=list(myTuple)

#Into strings
stringFromTuple = " ".join(myTuple)
stringFromList = " ".join(myList)

#From strings into separate characters
tupleFromString = tuple(myString)
listFromString  = list(myString)

#From strings into separate words
listFromString  = myString.split(" ")
#tupleFromString: There is no easy code for this. Just convert string to list and list to Tuple
tupleFromString = tuple(myString.split(" "))

# Sequences08.py
myVariantList = ["I","was", 1, "List", True]
#convert it all to a list of strings
myStringList = [str(item) for item in myVariantList]
myStringList2 = list(map(str, myVariantList))
myStringFromVariantList1 = ' '.join([str(item) for item in myVariantList])
myStringFromVariantList2 = ' '.join(list(map(str, myVariantList)))

#%% 9.1 Creating and accessing a dictionary

product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}
dict_UK_NL = {"house":"huis", "dog":"hond", "cat":"kat", "bird":"vogel"}

print(type(product_prices["bananas"])) # WRONG: case-sensitive
print(product_prices)
print(type(product_prices["Bananas"]))

dict_UK_NL["cat"] = "poes"

testdict = {"item1":"John", "item2":4} # OK
testdict = {"item1":"John", 2:4} # Strange, but possible
print(testdict["item1"]) # OK: "John"
print(testdict[2]) # OK: 4; NB: not testdict[1]!
# so you can use integers as keys
print(testdict["2"]) # WRONG: key is an integer in this case
testdict = {"item1":"John", 2.1:4} # Strange, but possible
print(testdict[2.1]) # OK: 4; NB: not testdict[1]!
# so you can use floats as keys as well

#%% 9.2 Adding and deleting

product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}
dict_UK_NL = {"house":"huis", "dog":"hond", "cat":"kat", "bird":"vogel"}
dict_UK_NL["horse"] = "paard"
product_prices["Potatoes"] = 0.99
del product_prices["Tomatoes"]
del product_prices["Tomatoes"]

#%% 9.3 Methods

dict_UK_NL = {"house":"huis", "dog":"hond", "cat":"kat", "bird":"vogel"}

dictnew = dict_UK_NL.copy() # OK

# availability of methods an be asked:
help(dict)

# or simply tried:
dictsmall = {"window":"raam"}
dict_UK_NL.append(dictsmall) # Not available
dict_UK_NL.insert("dog", dictsmall) # Not available
dict_UK_NL.sort() # Not available
dict_UK_NL.reverse() # Not available
print(dict_UK_NL.index("hond"))  # Not available
print("dog" in dict_UK_NL) # OK
print("hond" in dict_UK_NL) # Finds keys only, no values

# print a sorted list of keys:
product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}
allkeys = list(product_prices.keys())
allkeys.sort()
print(allkeys)

#%% 9.4 Traversing all keys

# print an ordered series of keys and their values
# two option, either:
product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}
allkeys = list(product_prices.keys())
allkeys.sort()
for item in allkeys:
    print(item, product_prices[item])

# or, mind the differences:
product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}
for item in sorted(product_prices.keys()):
    print(item, product_prices[item])

#%% 9.5 Complex dictionaries, Accessing
# Dictionaries02.py
    
courses = {"CIT101": 
    {"type":"PYT", "name":"Introduction into programming using Python",
     "lang":"EN", "semester":1, "room":253},
     "CIT102":
    {"type":"THS", "name":"Writing a thesis using Word",
     "lang":"EN", "semester":2, "room":153},
     "CIT103":
    {"type":"RIN", "name":"Introduction into R",
     "lang":"EN", "semester":1, "room":253},
     "CIT104":
    {"type":"EXL", "name":"Excel gevorderd",
     "lang":"NL", "semester":1, "room":153},
     "CIT106":
    {"type":"EXL", "name":"Excel gevorderd",
     "lang":"NL", "semester":1, "room":253},
     "CIT105":
    {"type":"PPT", "name":"Slimmer werken met Powerpoint",
     "lang":"NL", "semester":1, "room":253}
    }
  

coursecode = input("Course code? ")   
print(courses[coursecode])

coursetype = input("Course type? ")
# assuming there is only one course of each type:
for course in courses:
    if courses[course]["type"].upper() == coursetype.upper():
        print(courses[course])
        break
else:
    print(coursetype, "not found")
    
# assuming there may be more courses of each type:
isfound = False
for course in courses:
    if courses[course]["type"].upper() == coursetype.upper():
        print(courses[course])
        isfound = True
if not isfound:
    print(coursetype, "not found")
    
# formatted output:
isfound = False
for course in courses:
    if courses[course]["type"].upper() == coursetype.upper():
        print (course)
        for field in courses[course]:
            print("  {0:10s}:{1}".format(field, courses[course][field]))
        isfound = True
if not isfound:
    print(coursetype, "not found")
    
#%% 9.6: List or dictionary?
# Dictionaries03.py

def translate(french):
    dict_FR_EN = {"le":"the", 
                  "cheval":"horse",
                  "est":"is",
                  "dans":"in",
                  "pré":"meadow"
                  }
    words = french.split()
    translation=""
    for word in words:
        translation = translation + dict_FR_EN[word] + " "
    return translation.strip() # strip to remove trailing space

# Alternative
def translate2(french): 
    dict_FR_EN = {"le":"the", 
                  "cheval":"horse",
                  "est":"is",
                  "dans":"in",
                  "pré":"meadow"
                  }
    words = french.split()
    # translate the list items in place
    for i in range(len(words)):
        words[i] = dict_FR_EN[words[i]]
    return " ".join(words)

text = "le cheval est dans le pré"
print(translate(text))
print(translate2(text))

# Extended version
def translate3(french):
    dict_FR_EN = {"le":"the", 
                  "cheval":"horse",
                  "est":"is",
                  "dans":"in",
                  "pré":"meadow"
                  }
    words = french.split()
    translation=""
    for word in words:
        translation = translation + dict_FR_EN.get(word, "(" + word + ")") + " "
    return translation.strip() # strip to remove trailing space

def translate4(french): 
    dict_FR_EN = {"le":"the", 
                  "cheval":"horse",
                  "est":"is",
                  "dans":"in",
                  "pré":"meadow"
                  }
    words = french.split()
    # translate the list items in place
    for i in range(len(words)):
        words[i] = dict_FR_EN.get(words[i], "(" + words[i] + ")")
    return " ".join(words)

def translate5(french):
    dict_FR_EN = {"le":"the", 
                  "cheval":"horse",
                  "est":"is",
                  "dans":"in",
                  "pré":"meadow"
                  }
    words = french.split()
    translation=""
    for word in words:
        english = dict_FR_EN.get(word) # returns None if not found
        if english:   # None = False!
            translation = translation + english + " "
        else:
            translation = translation + "(" + word + ") "
    return translation.strip() # strip to remove trailing space

supertext = "le chat est aussi dans le pré"
print(translate(supertext))
print(translate2(supertext))
print(translate3(supertext))
print(translate4(supertext))
print(translate5(supertext))

#%% 10.3 Reading, Reading an entire file
# Files-reading.py    

with open("t:/Basics01.py") as fin: # adapt the path
    contents = fin.read()
print(contents) 

# alternative:
with open("t:/Basics01.py") as fin: # adapt the path
    print(fin.read()) 
    
   
    
# ReadBigFile.py
# or, if the file is big:
with open("t:/ENwords.txt") as fin: # adapt the path
    for i in range(5):
        print(fin.readline())
    
# dropping the extra line break
with open("t:/ENwords.txt") as fin: # adapt the path
    for i in range(5):
        print(fin.readline().strip())
 
    
# counting the lines
nr = 0        
with open("t:/ENwords.txt") as fin: # adapt the path
    for line in fin:
        nr +=1
print(nr)    
 
# alternative: print the length of the list of lines  
with open("t:/ENwords.txt") as fin: # adapt the path
    print(len(fin.readlines()))
# the risk of reading the entire file with readlines
# is that it will not fit in memory


#Find the longest word in a file
fin = open("t:/ENwords.txt")
longest = ""
max = 0
for line in fin:
    word = line.strip() 	# why not: word = fin.readline().strip?
    if len(word) > max:
        max = len(word)
        longest = word
print(longest, max)
fin.close()

# Find all longest word in a file
# Step 1: find greatest length
fin = open("t:/ENwords.txt")
max = 0
for line in fin:
    word = line.strip()
    if len(word) > max:
        max = len(word)
# Step 2: find all words of this length
# reopen the file, to "rewind" it:
fin = open("t:/ENwords.txt") # try to comment this line out
longest = []
for line in fin:
    word = line.strip()
    if len(word) == max:
        longest.append(word)
print(max, longest)
fin.close()

#Find all longest word in a file, in one loop
fin = open("t:/ENwords.txt")
max = 0
for line in fin:
    word = line.strip()
    if len(word) > max:
        max = len(word)
        #this word is longer than the previous series: start all over
        longest = [word]
    elif len(word) == max: # same length
        longest.append(word)
print(max, longest)
fin.close()


#Find all palindromes in a file
with open("t:/ENwords.txt") as fin:
    palindromes = []
    n = 0
    for line in fin:
        word = line.strip()
        if word.upper() == word[::-1].upper():
            palindromes.append(word)
            n += 1
print(n, palindromes)

#%% 10.4: Writing, Writing a string
# Files01.py

header = "Price list\n"  # \n: make sure that next item will be on a new line
product_prices = {"Tomatoes":1.75, "Bananas":2.25, "Oranges":3}

fout = open("pricelist.txt", "w")
print(fout.write(header))
fout.write(str(product_prices)) # write can only handle strings
# output of write is "lost"
fout.close()

# alternative:
with open("pricelist.txt", "w") as fout:
    print(fout.write(header))
    fout.write(str(product_prices))

with open(input("Path and file name: "), "w") as fout:
    fout.write(header)
    for item in product_prices:
        fout.write("{0:10s} : {1:s}\n".format(item, 
                   str(product_prices[item])))
    
#%% 10.5: Interaction with the operating system
# Files03.py

import os
     
filename = input("File (including path): ")

if os.path.isfile(filename):
    fin = open(filename)
    n = 0
    for line in fin:
        n += 1
    print("File", filename, "contains", n, "lines")        
elif os.path.isdir(filename):
    print(filename, "is not a file but a directory!")
else:
    print(filename, "is not a file!")


# Alternative, simple general check
filename = input("File (including path): ")

try:
    fin = open(filename)
    n = 0
    for line in fin:
        n += 1
    print("File", filename, "contains", n, "lines")        
except:
    print("Something wrong with", filename)
    
#%% 11.2 Defining classes, Adding methods
# Objects02.py

class Point:
    """Point in a two-dimensional space"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
start_point = Point()
end_point = Point()
#What are the coordinates of start_point? Print them. 
print("x =", start_point.x, "y=", start_point.y)
#Modify and print  end_point 
end_point = Point(4, 3)
print("x =", end_point.x, "y=", end_point.y)

#The ‘quadrant’ method 
class Point:
    """Point in a two-dimensional space"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def quadrant(self):
        if self.x >0 and self.y < 0:
            return "Upper left"
        elif self.x >0 and self.y > 0:
            return "Upper right"
        elif self.x <0 and self.y < 0:
            return "lower left"
        elif self.x <0 and self.y > 0:
            return "lower right"
end_point = Point(4, 3) #load the class and reload end_point to make it an object of the newly loaded class
end_point.quadrant()

#The ‘horizontal_distance’ method 
class Point:
    """Point in a two-dimensional space"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def horizontal_distance(self, point2):
        if self.y > point2.y:
            return (self.y - point2.y)
        else:
            return (point2.y-self.y)
start_point = Point()
end_point = Point(4, 3) #load the class and reload start_point and end_point to make it an object of the newly loaded class
end_point.horizontal_distance(start_point)

#basic solution to calculate the distance:
class Point:
    """Point in a two-dimensional space"""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def dist(self, x2, y2):
        return ((x2-self.x)**2 + (y2-self.y)**2)**0.5

start_point = Point()
end_point = Point(4, 3)

print(start_point.dist(end_point.x, end_point.y))


# alternative, making better use of the object concept
class Point:
    """Point in a two-dimensional space"""

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def dist(self, other): # other must be a Point as well
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5

start_point = Point()
end_point = Point(4, 3)

print(start_point.dist(end_point))

#%% 11.2 Defining classes, Displaying objects
# Objects03.py

class Point:
    """Point in a two-dimensional space"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def dist(self, other): # other must be a Point as well
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5

    def __repr__(self):
        return "x: {0:3.1f}; y: {1:3.1f}".format(self.x, self.y)
    
end_point = Point(3,4)
print(end_point)

#%% 11.3 Operator overloading, Comparisons
# Objects04.py

class Point:
    """Point in a two-dimensional space"""
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def dist(self, other): # other must be a Point as well
        return ((other.x-self.x)**2 + (other.y-self.y)**2)**0.5

    def __repr__(self):
        return "x: {0:3.1f}; y: {1:3.1f}".format(self.x, self.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
        
start_point = Point(3, 4)
end_point = Point(3, 4)
other_point = Point()

print(start_point == end_point)
print(start_point == other_point)

#%% 12.2 Prime numbers

# Algorithm 0: checking all integers

from datetime import datetime
# n = int(input("Find all primes up to: ")) # try 100000
n = 1000000 # temporarily, after testing, use line above
primes = []

def isprime(y):
    for x in range(2, y): # why not range(y)?
        if y % x == 0:
            return False
    return True

start = datetime.now()
for i in range(2, n):
    if isprime(i):
        primes += [i]
end = datetime.now()
print( "Algorithm 0, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))

# Algorithm 1: checking all previous primes

from datetime import datetime
# n = int(input("Find all primes up to: ")) # try 100000
n = 100000 # temporarily, after testing, use line above
primes = []

def isprime(y):
    for x in primes:
        if y % x == 0:
            return False
    return True

start = datetime.now()
for i in range(2, n):
    if isprime(i):
        primes += [i]
end = datetime.now()
print( "Algorithm 1, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))


# Algorithm 2: stopping at the square root
from datetime import datetime
import math
# n = int(input("Find all primes up to: ")) # try 100000
n = 100000 # temporarily, after testing, use line above
primes = []

def isprime(y):
    for x in primes:
        if x > math.sqrt(y): # stop at squareroot(y)
            return True
        if y % x == 0:
            return False
    return True
start = datetime.now()
for i in range(2, n):
    if isprime(i):
        primes += [i]
end = datetime.now()
print( "Algorithm 2, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))


# Algorithm 3: Stopping at the squareroot, and skipping even numbers

from datetime import datetime
import math
# n = int(input("Find all primes up to: ")) # try 100000
n = 100000 # temporarily, after testing, use line above
primes = [2]

def isprime(y):
    for x in primes:
        if x > math.sqrt(y): # stop at squareroot(y)
            return True
        if y % x == 0:
            return False
    return True
start = datetime.now()
for i in range(3, n, 2): # do NOT start at 2!
    if isprime(i):
        primes += [i]
end = datetime.now()
print( "Algorithm 3, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))



# Algorithm 4: Removing all multiples of the primes found

from datetime import datetime
# n = int(input("Find all primes up to: ")) # try 100000
n = 100000 # temporarily, after testing, use line above
primes = []
# create a list for all candidates that indicates if they have been checked
# we will simply neglect the existence of checked[0]
start = datetime.now()
checked = [] 
for i in range(n+1):
    checked += [False]
for i in range(2, n+1): # 1 is not a prime, so we start at 2
    if not checked[i]: # as long as not marked, it must be a prime!
        primes += [i] # add it to the list of found primes
        for j in range(i, n+1, i): # find all multiples of this prime
            checked[j] = True # and mark them as checked

end = datetime.now()
print( "Algorithm 4, found {} primes up to  {}: {}.{:06d} seconds".format(
        len(primes), n, (end -start).seconds, 
        (end -start).microseconds))


#%% 13.1: Algorithms, Magic squares

def magic_square(n):
    """
    generates and prints a magic square of size n * n
    n must be a positive odd integer
    a grid (list of lists) with the square is returned
    """
    # The magic square will be stored in a list.
    # As the elements of the list count from 0,
    # you have to to correct for that.
    row = [] 
    grid = []
    for i in range(n):  	# create a row with n items
        row.append(None)
    for i in range(n):  	# built a table/grid of n rows
        grid.append(row.copy()) 	# grid.append(row) would just add an alias to row!
    r = (n+1)//2 -1	# the row number-1, because of indexing from 0
    c = n -1 	# the column number
    maxnr = n**2
    nr = 1 # the starting integer
    while nr <= maxnr: 	# continue as long as not all cells are filled
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
            nr += 1  	# next number
        else: 	# if the destination was not empty
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
            print("{:4d}".format(grid[i][j]), end="") 	# no line breaks
        print() # to get a line break
    return grid 	# grid is not only printed, but also returned

def check_list(series):
    """checks the sum of one series (row, column, or diagonal) """
    n = len(series)
    required = int(n * (n*n + 1)/2) 	# int is essential for later comparison
    sum = 0
    for cell in series:
        sum += int(cell)
    return sum, required	# return a tuple

def check_magic_square(grid):
    """ check sum of all rows, columsn and diagonals """
    n= len(grid)
    msg = ""	# collect all messages in a string
    # check rows
    for row in grid:
        sum, required = check_list(row)
        if sum != required:
            msg = msg + "Row {} has sum {} instead of {}\n".format(
                  row, sum, required)
        else:
            msg = msg + "Row {} has sum {}: OK\n".format(row, sum) 

    # check columns, must be composed first
    for j in range(n): # columns
        series = []
        for i in range(n): 	# rows
            series += [grid[i][j]]  	#column j of row i, remember the outer []
        sum, required = check_list(series)
        if sum != required:
            msg = msg + "Column {} has sum {} instead of {}\n".format(
                  series, sum, required)
        else:
            msg = msg + "Column {} has sum {}: OK\n".format(series, sum) 

    # check diagonal1	# must be composed
    series = []
    for i in range(n): 
        series += [grid[i][i]]  #column i of row i
    sum, required = check_list(series)
    if sum != required:
        msg = msg + "Diagonal {} has sum {} instead of {}\n".format(
              series, sum, required)
    else:
        msg = msg + "Diagonal {} has sum {}: OK\n".format(series, sum) 

    # check diagonal2	# must be composed
    series = []
    for i in range(n): 
        series += [grid[i][n-i-1]]  #column n-1 of row i
    sum, required = check_list(series)
    if sum != required:
       msg = msg + "Diagonal {} has sum {} instead of {}\n".format(
             series, sum, required)
    else:
        msg = msg + "Diagonal {} has sum {}: OK".format(series, sum) 
    return msg	# all collected messages

n=5 
# After testing, remove the previous line and uncomment the following 
# n = input("Size of the square (odd positive integer):")
# It ought to be checked whether the value is an odd positive integer
#print(check_magic_square(magic_square (5)))
# while debugging, it is easier to see intermediate results
# after that, the next three lines might be removed
# and the previous one 'uncommented'
grid = magic_square (n)
result = check_magic_square(grid)
print(result) 
