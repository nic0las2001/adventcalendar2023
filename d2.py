import math

input = open("d2.txt","r")

targets = {'red':12, 'green':13, 'blue':14}

sumtot = 0
sumtot2 = 0
i = 0
for line in input: 
    i += 1
    sumi = i
    gm = line.split(":")
    gm[1] = gm[1].replace(';', '')
    gm[1] = gm[1].replace(',', '')
    line_list = gm[1].split()
    
    mincount = {}
    for count in range(0,len(line_list)-1,2):
        if targets[line_list[count+1]] >= int(line_list[count]):
            pass
        else:
            sumi = 0
        
        if line_list[count+1] not in mincount:
            mincount[line_list[count+1]] = int(line_list[count])
        elif int(line_list[count]) > mincount[line_list[count+1]]:
            mincount[line_list[count+1]] = int(line_list[count])

    power = math.prod(list(mincount.values()))

    sumtot2 += power
    sumtot += sumi

print("Part 1: ",sumtot)
print("Part 2: ",sumtot2)
