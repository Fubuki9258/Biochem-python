def line(char, length):
    double_length = 2 * int(length)
    print(char * double_length)

x = "="
line(x, 5 * 10)

def star_line():
    print("*" * 100)

star_line()

def optional_line(char, length = 50): 
    print(char * length)

optional_line("=", 10)
optional_line("*")