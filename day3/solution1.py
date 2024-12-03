import re

with open("day3/input.txt", "r") as file:
    content = file.read()


#iscemo mul(x,y) kjer sta x in y med 1-3 stevke 
pattern = r'\b(?:mul|add|sub)\((\d{1,3}),\s*(\d{1,3})\)'


#commands = re.findall(pattern, content)
matches = re.findall(pattern, content)

arrX = []
arrY = []

for match in matches:
    x, y = match
    arrX.append(int(x))  
    arrY.append(int(y))

sum=0

for i in range (len(arrX)): 
    sum+=arrX[i]*arrY[i]

print(sum)