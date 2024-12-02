import numpy as np
import os
print(os.getcwd())


with open("day1\input.txt", "r") as file: 
    data=[line.split() for line in file]

array1 = np.array([int(row[0]) for row in data], dtype=int)
array2 = np.array([int(row[1]) for row in data], dtype=int)

unique_array = list(set(array1))

sum=0

for i in range (len(unique_array)):
    sum+= unique_array[i]*np.count_nonzero(array2 == unique_array[i])

print("rezultat je ",  sum)