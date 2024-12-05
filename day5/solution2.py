import time

start_time = time.time()
sum=0
part1=[]
part2=[]
pravila=[]
navodila=[]
slabaNavodila=[]
is2ndPart=False

with open("day5/input.txt", "r") as file:
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
temparr1=part1.splitlines()
temparr2=part2.splitlines()



for n in temparr1:
    ent=[]
    ent.append(n[0:2])
    ent.append(n[3:5])
    for i in range(len(ent)):
        ent[i]=int(ent[i])
    pravila.append(ent)

pravila=sorted(pravila, key=lambda x: x[1])   

for n in temparr2:
    ent=n.split(",")
    for i in range(len(ent)):
        ent[i]=int(ent[i])
    navodila.append(ent)

for i in range(len(navodila)):
    velja = True
    for n in range(len(navodila[i])):
        for m in range(n + 1, len(navodila[i])):
            for rule in pravila:
                if rule[0] == navodila[i][m] and rule[1] == navodila[i][n]:
                    velja = False  
                    break
            if not velja:
                break
        if not velja:
            break

    if not velja:
        slabaNavodila.append(navodila[i])


for faulty_update in slabaNavodila:
    update = faulty_update  
    sorted_update = sorted(update)
    #z mal pomoci gpt-ja ;)
    changed = True
    while changed:
        changed = False
        for rule in pravila:
            if rule[0] in sorted_update and rule[1] in sorted_update:
                index1 = sorted_update.index(rule[0])
                index2 = sorted_update.index(rule[1])
                if index1 > index2: 
                    sorted_update[index1], sorted_update[index2] = sorted_update[index2], sorted_update[index1]
                    changed = True 
                    break  
    
    middle_page = sorted_update[len(sorted_update) // 2]
    sum += middle_page 

end_time = time.time()
print("resitev > ", sum)
print("program laufal : " , (end_time - start_time),"s")
