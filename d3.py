import numpy as np
input = open("d3.txt","r")

data = input.readlines()
map = np.array(data)

def neighbour_func(map,i,j):
    output = False
    charlist = []
    for ki in range(-1,2):
        for kj in range(-1,2):
            if i+ki > -1 and j+kj > -1 and i+ki < len(map) and j+kj < len(map[i])-1:
                    if (map[i+ki][j+kj].isnumeric() == False) and (map[i+ki][j+kj] not in "\\.n ") and map[i+ki][j+kj] != "":
                        output = True
                    if map[i+ki][j+kj] == "*":
                        char_dat = [i+ki,j+kj]
                        if char_dat not in charlist:
                            charlist.append(char_dat)
    return output, charlist


elligible_num = []
stars = []

for i in range(0,len(map)):
    j = 0
    while j < len(map[i]):
        num = ""
        status = False
        starlist = []
        while map[i][j].isnumeric():
            num += map[i][j]
            elligible, charlist = neighbour_func(map,i,j)
            if elligible == True:
                status = True
            for char_dat in charlist:
                if char_dat != [] and char_dat not in starlist:
                    starlist.append(char_dat)
            
            if j<len(map[i]):
                j += 1
            else:
                break
        j+=1
        if num.isnumeric() and status:
            elligible_num.append(int(num))
            for item in starlist:
                pt = item
                pt.insert(0, int(num))
                stars.append(pt)


print("Part 1: ", sum(elligible_num))

stardata = np.array(stars)
stardict = {}

for line in stardata: 
    key = str(line[1])+"x"+str(line[2])
    if key not in stardict: 
        stardict[key] = [line[0]]
    else:
        stardict[key].append(line[0])

sum2 = 0
for key,val in stardict.items():
    if len(stardict[key]) == 2:
        prod = stardict[key][0] * stardict[key][1]
        sum2 += prod

print("Part 2:", sum2)