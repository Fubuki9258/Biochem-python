import pandas
import numpy
import matplotlib

persons = pandas.DataFrame(
    {'age': [26, 23, 45, 33, 56, 43, 22, 38, 34, 43],
     'fitness': [6, 7, 6, 8, 5, 6, 8, 7, 7, 6]})

x = persons['age']
y = persons['fitness']
matplotlib.pyplot.scatter(x, y)
m, b = numpy.polyfit(x, y, 1)
matplotlib.pyplot.plot(x, m*x+b)
matplotlib.pyplot.show()

