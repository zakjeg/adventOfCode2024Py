import numpy as np
import sys

with open("day4/input.txt", "r") as file:
    input_string = file.read()

sum=0
arr = input_string.splitlines()

for row in arr:
    sum+=row.count("XMAS")+row.count("SAMX")

for i in range (len(arr)):
    stolpec = ""
    for row in arr:
        stolpec+=row[i]
    sum+=stolpec.count("XMAS")+stolpec.count("SAMX")

matrix = [list(string) for string in arr]

matrix = np.array(matrix)
diags = [matrix[::-1,:].diagonal(i) for i in range(-matrix.shape[0]+1,matrix.shape[1])]
diags.extend(matrix.diagonal(i) for i in range(matrix.shape[1]-1,-matrix.shape[0],-1))


for n in diags:
    diag=''.join(n.tolist())
    sum+=diag.count("XMAS")+diag.count("SAMX")

print("koncni rezultat = ", sum)