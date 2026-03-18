#%% Convert from, and to, Tuple, List and string
myList = ["I","was a", "List"]
myTuple = ("I","was a", "Tuple")
myString = "I was a string"

#Tuple and List swap
tupleFromList= 
listFromTuple= 

#Into strings
stringFromTuple =  
stringFromList =  

#From strings into separate characters
tupleFromString =  
listFromString  =  

#From strings into separate words
listFromString  =  
tupleFromString = #HINT ---> ---------------------------------------------------------------------------------------------------------> There is no easy code for this. Just convert string to list and list to Tuple

#%%
#Advanced String from list with various types of values
myVariantList = ["I","was", 1, "List", True]
#convert it all to a list of strings
myStringList =             #HINT ---> ---------------------------------------------------------------------------------------------------------> Use the map function and convert that result into a list. list(map(function,items)))
#Join words to a string as before
myStringFromVariantList1 = 
#or in one go
myStringFromVariantList2 = " ".join(map(str, myVariantList))

#%% (Optional) potential of map function

#The map() function applies a function to al items in a sequence (like a list).
#Build a simple function that squares numbers.
#Use the map() function to apply that function to all MyNumbers

def square(num):
    return num**2

squared=square(3) #Tip: test your work halfway

myNumbers=[1,2,3]
mySquaredNumbers = list(map(square, myNumbers))


#%% ANSWERS Convert from, and to, Tuple, List and string
myList = ["I","was a", "List"]
myTuple = ("I","was a", "Tuple")
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
tupleFromString = tuple(myString.split(" "))

#%%
#Advanced String from list with various types of values
myVariantList = ["I","was", 1, "List", True]
myStringList = list(map(str, myVariantList))
myStringFromVariantList1 = " ".join(myStringList)
#or in one go
myStringFromVariantList2 = " ".join(map(str, myVariantList))

#%% (Optional) potential of map function

#The map() function applies a function to al items in a sequence (like a list).
#Build a simple function that squares numbers.
#Use the map() function to apply that function to all MyNumbers

def square(num):
    return num**2

squared=square(3) #Tip: test your work halfway

myNumbers=[1,2,3]
mySquaredNumbers = list(map(square, myNumbers))
