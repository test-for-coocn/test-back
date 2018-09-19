import math

import matplotlib.pyplot as plt

 

def sqr(x):

    return x * x

 

#

#       Data

#

pairs = [[70, 168], [68, 165], [62, 159], [56, 156], [70, 170],

         [64, 162], [59, 162], [70, 169], [68, 168], [69, 170],

         [67, 168], [63, 166], [58, 163], [74, 170], [65, 168],

         [60, 160], [65, 165], [72, 175], [61, 164], [77, 174],

         [68, 164], [64, 161], [70, 166], [47, 147], [66, 165],

         [68, 170], [73, 174], [74, 172], [63, 164], [83, 182],

         [58, 159], [64, 166], [67, 167], [75, 174], [67, 163],

         [68, 166], [68, 167], [66, 165], [63, 165], [55, 154],

         [61, 163], [60, 160], [62, 164], [62, 160], [59, 160],

         [51, 155], [59, 163], [68, 170], [56, 157], [79, 180]]

 

n = len(pairs)      #       The number of pairs (xi, yi)

print("n = %d"%n)

 

sum_x = 0.0

sum_y = 0.0

for i in range(0, n):

    sum_x += pairs[i][0]

    sum_y += pairs[i][1]

mean_x = sum_x / n

mean_y = sum_y / n

print("Mean_x = %f"%mean_x)

print("Mean_y = %f"%mean_y)

ssum_x = 0.0

ssum_y = 0.0

sum_xy = 0.0

for i in range(0, n):

    ssum_x += sqr(pairs[i][0] - mean_x)

    ssum_y += sqr(pairs[i][1] - mean_y)

    sum_xy += (pairs[i][0] - mean_x) * (pairs[i][1] - mean_y)

   

var_x = ssum_x / n                  #   Variance of X

var_y = ssum_y / n                  #   Variance of Y

print("Var_x = %f"%var_x)

print("Var_y = %f"%var_y)

sd_x = math.sqrt(var_x)             #   Standard deviation of X

sd_y = math.sqrt(var_y)             #   Standard deviation of Y

print("sd_x = %f"%sd_x)

print("sd_y = %f"%sd_y)

 

cor = sum_xy / math.sqrt(ssum_x * ssum_y)       #   The correlation coefficient

print("r = %f"%cor)

 

data_x = []     #   Values of the coordinate Xs of the pairs

data_y = []     #   Values of the coordinate Ys of the pairs

for i in range(0, n):

    data_x.append(pairs[i][0])

    data_y.append(pairs[i][1])

print(data_x)

print(data_y)

 

plt.title("Scattergram...r = %6.3f"%cor)            #   The title of the scattergram

plt.xlabel("Weight")                #   The label of the x-axis

plt.ylabel("Height")                #   The label of the y-axis

plt.plot(data_x, data_y, 'bo')      #   Make the scattergram.   'bo' -> blue circle

plt.show()                          #   Show the scattergram