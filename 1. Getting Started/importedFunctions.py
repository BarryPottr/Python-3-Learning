import fileinput # You can also give libraries as aliases. Ex: import fileinput as fi
import time
import numpy # install with "pip install numpy" in terminal


# Notice how this input() function has the module name and period before it. 
# This tells Python to use fileinput's input() function instead of the standard input() function
lines = fileinput.input() 

print(time.localtime())

numpyArray = numpy.array([9,5,7,11])