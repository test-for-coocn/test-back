import matplotlib.pyplot as mpt

import math

 

def sqr(x):

    return x * x

 

data = [66, 59, 62, 64, 63,

        68, 65, 59, 68, 64,

        65, 51, 67, 64, 83,

        59, 61, 62, 57, 72,

        65, 64, 54, 60, 53,

        65, 67, 60, 53, 79,

        74, 53, 61, 68, 75,

        50, 57, 55, 66, 56,

        55, 61, 70, 71, 49,

        69, 70, 80, 73, 72]

 

n = len(data)           #  The number of scores

print("n =%d"%n)

 

print("Data...")

i = 1

for x in data:

    print("%5d:"%i + "  %f"%x)

    i+=1

 

mpt.title("Histogram")      #   The title of the histogram

mpt.xlabel("Score")        #   The label of the x-axis

mpt.ylabel("Frequency")   #   The label of the y-axis

mpt.hist(data, bins = 10)   #   Making the histogram

mpt.show()                  #   Show the histogram