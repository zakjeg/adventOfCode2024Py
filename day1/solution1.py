import numpy as np
import os

with open("day1\input.txt", "r") as file: 
    data=[line.split() for line in file]

array1 = np.array([int(row[0]) for row in data], dtype=int)
array2 = np.array([int(row[1]) for row in data], dtype=int)
array1.sort()
array2.sort()

sum=0

for i in range (len(array1)):
    sum+=abs(array1[i]-array2[i])

print("rezultat je ",  sum)