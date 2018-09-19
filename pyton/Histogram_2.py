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

 

n = len(data)           #   The number of scores

print("n =%d"%n)

 

print("Data...")

i = 1

for x in data:

    print("%5d:"%i + "  %f"%x)

    i+=1

 

sum = 0.0

for x in data:

    sum += x

mean = sum / len(data)

print("Mean = %f"%mean)

ssum = 0.0

for x in data:

    ssum += sqr(x - mean)

var = ssum / len(data)

sd = math.sqrt(var)

print("Variance = %f"%var + "     sd = %f"%sd)

uvar = ssum / (len(data) - 1.0)

sd_uvar = math.sqrt(uvar)

print("Unbiased Var. = %f"%uvar + "     sd(uvar) = %f"%sd_uvar)

 

#

#       Check the minimum and maximum values

#

vmin = data[0]

n_max = n

vmax=data[0]

for x in data:

    if vmin > x: vmin = x

    if vmax < x: vmax = x

print("min = %f"%vmin + "   max = %f"%vmax)

n_bin = 10

while(True):

    mpt.title("Histogram")          #   The title of the histogram

    mpt.xlabel("Score")            #   The label of the x-axis

    mpt.ylabel("Frequency")       #   The label of the y-axis

    mpt.axis([vmin,vmax,0,n_max])   #   Set the boundaries of the axes

    mpt.hist(data, bins = n_bin)    #   Make the histogram

    mpt.show()                      #   Show the histogram

 

    n_bin = int(input("n_bin/%d = "%n_bin))     #   Set the number of

    if (n_bin < 2): break                       #   The program ended

    n_max = int(input("n_max/%d = "%n_max))     #   The upper boundary of the y-axis

    vmin = float(input("x_min/%f = "%vmin))     #   The left boundary of the x-axis

    vmax = float(input("x_max/%f = "%vmax))     #   The right boundary of the x-axis