import math

import matplotlib.pyplot as mpt

 

def sqr(x):

    return x * x

 

#

#       Prepare the input data file

#

s_in = input("Input data file = ")

f_in = open(s_in, "r")

#

#       Set the contents of the input data file in the object data

#

data_f = f_in.readlines()

f_in.close()

#

#       Prepare the output file

#

s_out = input("Output data file = ")

f_out = open(s_out, "w")

f_out.write("Input data file = " + s_in + "\n\n")

 

pos = 0

while True:

    if data_f[pos].find("/", 0) == 0: break

    pos += 1

n = 0

data = []

while True:

    pos += 1

    if data_f[pos].find("/", 0) == 0: break

    data.append(float(data_f[pos]))

    n += 1

   

print("Data...")

i = 1

for x in data:

    f_out.write("%5d:"%i + "  %f\n"%x)

    i+=1

 

f_out.write("\n")

sum = 0.0

for x in data:

    sum += x

mean = sum / n

print("Mean = %f"%mean)

f_out.write("Mean = %f\n"%mean)

ssum = 0.0

for x in data:

    ssum += sqr(x - mean)

var = ssum / n

sd = math.sqrt(var)

print("Variance = %f"%var + "     sd = %f"%sd)

f_out.write("Variance = %f"%var + "     sd = %f\n"%sd)

uvar = ssum / (n - 1.0)

sd_uvar = math.sqrt(uvar)

print("Unbiased Var. = %f"%uvar + "     sd(uvar) = %f"%sd_uvar)

f_out.write("Unbiased Var. = %f"%uvar + "     sd(uvar) = %f\n"%sd_uvar)

 

 

f_out.close()

print(s_out + " was saved.")

 

 

vmin = data[0]

n_max = n

vmax=data[0]

for x in data:

    if vmin > x: vmin = x

    if vmax < x: vmax = x

print("min = %f"%vmin + "   max = %f"%vmax)

n_bin = 10

while(True):

    mpt.title("Histogram")

    mpt.xlabel("Scores")

    mpt.ylabel("Frequencies")

    mpt.axis([vmin,vmax,0,n_max])

    mpt.hist(data, bins = n_bin)

    mpt.show()

 

    n_bin = int(input("n_bin/%d = "%n_bin))

    if (n_bin < 2): break

    n_max = int(input("n_max/%d = "%n_max))

    vmin = float(input("x_min/%f = "%vmin))

    vmax = float(input("x_max/%f = "%vmax))