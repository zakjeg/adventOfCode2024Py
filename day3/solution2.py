import re

with open("day3/input.txt", "r") as file:
    content = file.read()

#iscemo mul(x,y) kjer sta x in y med 1-3 stevke 
math_pattern = r'\b(?:mul)\((\d{1,3}),\s*(\d{1,3})\)'  
#iscemo do() / don't()
state_change_pattern = r"\b(?:do|don't)\(\)" 


matches = re.finditer((rf'{state_change_pattern}|{math_pattern}'), content)

store = True
validComands = []
sum=0

for match in matches:
    command = match.group(0)
    
    if re.match(state_change_pattern, command):  
        if command == "do()":
            store = True
        elif command == "don't()":
            store = False
    elif re.match(math_pattern, command):
        if store:
            x, y = map(int, match.groups())
            validComands.append((x,y))
            sum+= (x*y)



print(sum)
