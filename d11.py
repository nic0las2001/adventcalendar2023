import numpy as np

input = open("d11.txt","r")

space = []
for line in input:
    data = list(line)
    if "\n" in data:
        data.remove("\n")
    space.append(data)

space = np.array(space)
exp_space = space
# print(space)

i_idx = []
for i in range(len(space)):
    if "#" not in space[i][:]:
        i_idx.append(i)

j_idx = []
for j in range(len(space[0])):
    if "#" not in space[:, j]:
        j_idx.append(j)

galaxies = np.argwhere(space == "#")

shortest_paths = {}

for g in range(len(galaxies)):
    if g < len(galaxies):
        for h in range(g+1, len(galaxies)):
            dist = abs(galaxies[h][1]-galaxies[g][1])+abs(galaxies[h][0]-galaxies[g][0])
            shortest_paths[(tuple(galaxies[g]),tuple(galaxies[h]))] = dist

factor = 1000000-1 #NB: additional columns so -1 everytime

for key in shortest_paths.keys():
    for i in i_idx:
        if i < max(key[0][0],key[1][0]) and i>min(key[0][0],key[1][0]):
            shortest_paths[key] += factor
        
    for j in j_idx:
        if j < max(key[0][1],key[1][1]) and j>min(key[0][1],key[1][1]):
            shortest_paths[key] += factor

print(sum(shortest_paths.values()))