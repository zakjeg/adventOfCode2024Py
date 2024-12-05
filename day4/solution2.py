from collections import Counter

part1=[]
part2=[]
is2ndPart=False
with open("day4/input.txt", "r") as file:
    for line in file:
        if line.strip() == "" and not is2ndPart:
            is2ndPart = True
            continue

        if is2ndPart:
            part2.append(line)
        else:
            part1.append(line)
    
part1 = ''.join(part1)
part2 = ''.join(part2)
print(part1)
print(part2)

sum=0
#matrix = [list(string) for string in input_string.splitlines()]


iscemo = ["MAS", "SAM"]
rows = len(matrix)
cols = len(matrix[0])

pojaveA = []
for r in range(rows):
    for c in range(cols):        
        if r + 2 < rows and c + 2 < cols:
            word = matrix[r][c] + matrix[r+1][c+1] + matrix[r+2][c+2]
            if word in iscemo:
                pojaveA.append((r+1, c+1))  # kordinate črke a za => dol/desno
        
        if r + 2 < rows and c - 2 >= 0:
            word = matrix[r][c] + matrix[r+1][c-1] + matrix[r+2][c-2]
            if word in iscemo:
                pojaveA.append((r+1, c-1))  # kordinate črke a za => dol/levo

steviloPojav = Counter(pojaveA)

ponovljenePojaveA = {pojava: count for pojava, count in steviloPojav.items() if count > 1}

print("stevilo ponovljenih kordinat ", len(ponovljenePojaveA))

