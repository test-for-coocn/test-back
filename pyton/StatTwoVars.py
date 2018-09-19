import math

 

def sqr(x):

    return x * x

 

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

 

n = len(pairs)

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

 

var_x = ssum_x / n

var_y = ssum_y / n

print("Var_x = %f"%var_x)

print("Var_y = %f"%var_y)

sd_x = math.sqrt(var_x)

sd_y = math.sqrt(var_y)

print("sd_x = %f"%sd_x)

print("sd_y = %f"%sd_y)

cor = sum_xy / math.sqrt(ssum_x * ssum_y)

print("r = %f"%cor)