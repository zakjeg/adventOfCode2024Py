sum=0
part1=[]
part2=[]
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
pravila=[]
for n in temparr1:
    ent=[]
    ent.append(n[0:2])
    ent.append(n[3:5])
    for i in range(len(ent)):
        ent[i]=int(ent[i])
    pravila.append(ent)

pravila=sorted(pravila, key=lambda x: x[1])   

temparr2=part2.splitlines()
navodila=[]
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

    if velja:
        sredinski_index = len(navodila[i]) // 2
        #print(navodila[i][sredinski_index], "je veljavno!")
        sum += navodila[i][sredinski_index]

print("resitev > ", sum)
