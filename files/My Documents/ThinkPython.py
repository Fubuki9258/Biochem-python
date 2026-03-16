#%%

n=2;y=3
x=3
x=4;
60 * (24.95*.6)+.75*59+3
print(6 + (52 + 8.25 + 3*7.2 + 8.25) // 60,  (52 + 8.25 + 3*7.2 + 8.25) % 60)
16.5 + 21 + 36/60
def right_justify(text):
    print(" " * (70-len(text)) + text)
   
right_justify("Jan")
right_justify("Hemel")

def draw_grid():
    print(("+" + "-"*5)*2 + "+")
    print(("|" + " "*5)*2 + "|")
    print(("|" + " "*5)*2 + "|")
    print(("|" + " "*5)*2 + "|")
    print(("|" + " "*5)*2 + "|")
    print(("+" + "-"*5)*2 + "+")
    print(("|" + " "*5)*2 + "|")
    print(("|" + " "*5)*2 + "|")
    print(("|" + " "*5)*2 + "|")
    print(("|" + " "*5)*2 + "|")
    print(("+" + "-"*5)*2 + "+")

draw_grid()
#%%
import turtle
bob = turtle.Turtle()
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
#turtle.mainloop()
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)
#%%        
import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)
#%%
#5.1    
import time
print(time.time())
print(time.gmtime(0))
print(time.gmtime())
print(time.localtime())
print(time.strftime("%a %d %B %Y, %H.%M"), time.time()/24/60/60)
#%%
#5.2
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
#%%
#5.3
def is_triangle(a, b, c):
    if a>b+c or b>a+c or c>a+b:
        print("No, not a triangle")
    else:
        print("Yes, a triangle!")
        
def triangle()        :
    a = int(input("First length:"))
    b = int(input("Second length:"))
    c = int(input("Third length:"))
    is_triangle(a, b, c)
    
triangle()
#%%
#6.4
def is_power(a, b):
    if a // b == 1:
        return a % b == 0
    else:
        if abs(a % b) == 0:
            return is_power(a/b, b)
        else:
            return False
    
print(is_power(1024, 2))
print(is_power(3, 2))
print(is_power(1, 1))

# does this work?:
print(is_power(6.25, 2.5))   # only for integers!
print(is_power(0.25, 0.5))  # only for integers!

#%%
#6.5
def gcd(a, b):
    if b == 0:
        return a
    else:
        r= a % b
        return gcd(b, r)

print(gcd(96,54))
#%%
#7.1
import math

def mysqrt(a):
    if a >= 0:
        x = a/2
        while True:
  #          print(x)
            y = (x + a/x) / 2
            if y == x:
                return y
            x = y
    else:
        print("only postive values supported")
        
def test_square_root():
    print("a", "mysqrt(a)", "math.sqrt(a)", "diff", sep ="\t")
    print("-", "---------", "------------", "----", sep ="\t")    
    for a in range(1, 10):
        print(a, mysqrt(a), math.sqrt(a), abs(mysqrt(a)- math.sqrt(a)), 
              sep="\t")
 
def test_square_root_formatted():
    print("{:>5s}    {:15s} {:15s} {:15s}".format("a", "mysqrt(a)", 
          "math.sqrt(a)", "diff"))
    print("{:>5s}    {:15s} {:15s} {:15s}".format("-", "---------", 
          "------------", "----"))    
    for a in range(1, 10):
        print("{:5d} {:15.10f} {:15.10f} {:14g}".format(a, mysqrt(a), math.sqrt(a),
              abs(mysqrt(a)- math.sqrt(a))))
 
test_square_root()
test_square_root_formatted()
    
#%%
x = 5
def test():
    x = 7
    print(x)

test()	

print (x)
#%%
various = ["John", 42, True] + [1, 2, 3]
print (various)
extra = [various] + [1]
much = "test" + extra
rij = list(range(11))
print(rij[::2])
#%%
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
for x, y in zip(x, y):
    print(x, y)
#%%
printproduct = lambda x, y: print (x * y)
printproduct (2, 3)
mylist = [1, 2, 3, 4, 5]
mylist_squared = map(lambda x: x**2, mylist)
print(list(mylist_squared))
#%%
famous = set(('A', 'B', 'C'))
print (famous)
#%%
grades = [7.4, 2.8, 8.2, 4.0, 5.5, 6.5, 6.5]
persons = ['Giri', 'Hidayatullah', 'Husain', 'Prasad', 'Radhakrishnan',
           'Venkataraman', 'Singh']
info = zip(persons, grades)
print(info)
info = list(info)
info.sort()
print(info)
#%%
morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
         'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....', 'I': '..',
         'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---',
         'P': '.--.', 'Q': '--.-', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-',
         'V': '...-', 'W': '.--', 'X': '-..-',
         'Y': '-.--', 'Z': '--..',
         '0': '-----', '1': '.----', '2': '..---',
         '3': '...--', '4': '....-', '5': '.....',
         '6': '-....', '7': '--...', '8': '---..',
         '9': '----.'
         }
bericht = input("Geef bericht: ")
for teken in bericht:
    if teken == ' ':
        print()
    else:
        print(morse[teken.upper()], end=' ')#%%
#%%
def myfirstfunction(temp, mode):
    if mode == 'K':
        temp += 273
    elif mode == 'F':
        temp = (temp-32.0)*(5/9)
    if temp > 15:
        condition = 'good'
    else:
        condition = 'bad'
    return condition, temp

#demo = myfirstfunction(90, 'F')
#print("A temperature of {:.1f} is {:s}".format(demo[1], demo[0]))

condition, degrees = myfirstfunction(90, 'F')
print("A temperature of {:.1f} is {:s}".format(degrees, condition))
#%%
def sphere(r):
    return 4/3*3.1415*r*r*r, 4*3.1415*r*r

isOk = False
while not isOk:
    straal = input("Straal? ")
    try:
        straal = float(straal)
        isOk = True
    except:
        print('incorrect radius!')

volume, opp = sphere(straal)
print("volume={}, opp={}".format(volume, opp))
#%%
def square(L):
    for i in range(len(L)):
        L[i] **=2
    
Lijst = [1,2,3,4,5]
square(Lijst)
print(Lijst)

L2 = [x**4 for x in Lijst]
L3 =[x for x in Lijst if x %2 ==0]
#%%
def netto(bedrag):
    if bedrag < 50000:
        return bedrag * 0.9
    else:
        return bedrag * .5
    
salaries = [21000, 35000, 28000, 60000, 32000, 112000, 5500]
netsal = list(map(netto, salaries))
print(netsal)
#%%
zero = 0
five = 5
print(zero or five)
print(five or zero)