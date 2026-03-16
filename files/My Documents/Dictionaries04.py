#List comprehension for Dictionaries

#A step by step walkthrough

#create a simple dictionary
a_movie = {'title':'A boy and His Dog', 'year':1975, 'rating':6.6}

#as a reminder. In a dictionary you can use the key to select the value 
print(a_movie["title"])
#the text of that key can also be stored in a variable
key = "title"
print(a_movie[key])
#Of course we can choose how we call that variable. We just called it 'key' which is a logical name, but any name would do.
asdf = "title"
print(a_movie[asdf])


#Using list comprehension we can build a quick for loop to get all the keys
print([key for key in a_movie]) #key is a logical name
#or
print([asdf for asdf in a_movie]) #but really any name will work
#However, this next line won't work.
print([key for asdf in a_movie])  #here we get the variable 'asdf' with the loop
                        #but we try to print the variable key' that doesn't exist


#We can print all the keys
print([key for key in a_movie])
#Or directly use those keys to select the corresponding values in the dictionary
print([a_movie[key] for key in a_movie])

#We can also print both
print([(key, a_movie[key]) for key in a_movie])

#By now we have a lot of brackets, each with a different meaning.
#We'll identify each
print([(key, a_movie[key]) for key in a_movie])
#    123            4   43                   21
#1 ( ) of the print statement
#2 [ ] of the list comprehension
#3 ( ) creating a tuple
#4 [ ] making a selection in the dictionary a_movie

#Instead of printing the list of tuples, we can also store it as a list of tuples 
MyTupleList = [(asdf, a_movie[asdf]) for asdf in a_movie]
#Or store it as a list of lists 
MyListList = [[asdf, a_movie[asdf]] for asdf in a_movie]
#Open MyTupleList and MyListList by double-clicking them in the Variable explorer to see they indeed contain lists or tuples

#a dictionary can contain dictionaries itself
movie_dicts = {
    "1":{'title':'A boy and His Dog','year':1975,'rating':6.6},
    "2":{'title':'Ran','year':1985,'rating':8.3},
    "3":{'title':'True Grit','year':2010,'rating':8.0},
    "4":{'title':'Scanners','year':1981,'rating':6.7}
    }

movie_dicts = { #we can put dictionaries in dictionaries
    "1":{'title':'A','year':1},
    "2":{'title':'B','year':2}}
    
type(movie_dicts) #movie_dicts is a dictionary itself
#list comprehension also works with dictionaries inside dictionaries
#to get the titles you go through all dicts and per dict you ask the title
print([movie_dicts[each_dict]["title"] for each_dict in movie_dicts ]) 
#to clarify, if we don't specify we want the title, we get all dicts whole
print([movie_dicts[each_dict] for each_dict in movie_dicts ]) 

#you can also gather dictionaries in a list
movie_dicts = [
    {'title':'A boy and His Dog','year':1975,'rating':6.6},
    {'title':'Ran','year':1985,'rating':8.3},
    {'title':'True Grit','year':2010,'rating':8.0},
    {'title':'Scanners','year':1981,'rating':6.7}
    ] 
    #note we don't have to add the numbers now like "1":
    #these numbers were the keys of movie_dicts to find the subdicts
    #however, a list is ordered, which means each item we add automatically 
    #gets a followup number. See it like a row number of a table.
type(movie_dicts) #movie_dicts is now a list

#list comprehension also works with dictionaries inside a list
print([dict['title']  for dict in movie_dicts]) #dict is a logical name, although perhaps confusing, since it is a class object on it's own. Hence the coloring
help(dict)

print([each_dict['title']  for each_dict in movie_dicts ]) #some might find this more clear

print([qwer['title']  for qwer in movie_dicts ]) #but again, any name will do


#Thank you for your extra attention!