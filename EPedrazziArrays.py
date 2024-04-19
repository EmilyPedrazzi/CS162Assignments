#Emily Pedrazzi
#Python Arrays
#4-19-24
#CS 162

import numpy as ny

#1 Generate a random 5x5 2D numpy array
randArray = ny.random.randint(0,100,size=(5,5))

#2 Print the array
print("Your Array")
print(randArray)

#3 Print the 2nd row, 3rd column value
print("R2 C3 Value:",randArray[1,2])

#4 Print the sum of all values
print("Array Sum:",ny.sum(randArray))

#5 Print the mean of each row
print("Mean Value by Row:",ny.mean(randArray,axis=0))

#6 Print the max value in each column
print("Max Value by Column:",ny.max(randArray,axis=1))