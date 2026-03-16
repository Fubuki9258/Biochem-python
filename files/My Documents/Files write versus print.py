#write versus print
#you can write to a file with file.write(txt) or print(txt, file=file)
#write requires text, so if you want to write numbers, you first have to convert them 
#write will by default stay on the same line, unless you add "\n"
#print can deal with numbers as well
#print adds "\n" to the end of the line by default, unless you add 'end=""'
#print is easier to test, since you can jump to printing to console and printing to file quickly. (although opening the file is not very hard either)

#if you want numbers from a list, all on a seperate line. print() is easier
#using write
MyList=[1,2,3]
with open("A_write_test.txt","w") as file:
    for nr in MyList:
        file.write(str(nr) + "\n")

MyList=[1,2,3]
with open("A_print_test.txt","w") as file:
    for nr in MyList:
        print(nr, file=file) #to test, type )# before file=file

#if you want to write texts to the same line, write() is easier
MyList=["a","b","c"]
with open("A_write_test.txt","w") as file:
    for word in MyList:
        file.write(word)

#even easier with writelines()      
MyList=["a","b","c"]
with open("A_writelines_test.txt","w") as file:
    file.writelines(MyList)

MyList=["a","b","c"]
with open("A_print_test.txt","w") as file:
    for word in MyList:
        print(word, end="",file=file)#to test, type )# before file=file    