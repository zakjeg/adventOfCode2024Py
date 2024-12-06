def findGuard(arr):
    for i in range (len(arr)):
        for n in range (len(arr[0])):
            if arr[i][n]==1:
                cords=[i,n]
                return cords
            
matrix=[]

with open("day6/input.txt", "r") as file:
    for line in file:
        ent=[]
        for i in line:
            if i==".":
                ent.append(0)
            elif i=="#":
                ent.append(7)
            elif i=="^":
                ent.append(1)
        matrix.append(ent)

cords = findGuard(matrix)

cords = findGuard(matrix)
visited_positions = set()
smer = 1  

smer=1
print(cords)
print((len(matrix)), " " , (len(matrix[0])))
while cords[0]<(len(matrix)) and cords[1]<(len(matrix[0])) and cords[0]>0 and cords[1]>0 :
    visited_positions.add(tuple(cords))  
    
    if smer==1:
        if cords[0]-1<0:
            break
        elif matrix[cords[0]-1][cords[1]]==7:
            smer+=1
            continue
        else:
            cords[0]-=1
        print("1")
    elif smer==2:
        if cords[1] == len(matrix[0])-1:
            break
        elif matrix[cords[0]][cords[1]+1]==7:
            smer+=1
            continue
        else:
            cords[1]+=1
        print("2")
    elif smer==3:
        if cords[0] == (len(matrix))-1:
            break
        elif matrix[cords[0]+1][cords[1]]==7:
            smer+=1
            continue
        else:
            cords[0]+=1
        print("3")
    elif smer==4:
        if cords[1] < 0:
            break
        elif matrix[cords[0]][cords[1]-1]==7:
            smer=1
            continue
        else:
            cords[1]-=1
        print("4")
    print(cords)

print("Distinct positions visited:", len(visited_positions))
