import numpy as np

input = open("d5.txt","r")
data = input.readlines()

seeds = data[0]
seeds = seeds[6:-1].split()
print(seeds)

part = 1
if part == 2:
    new_seeds = []
    for i in range(0,len(seeds),2):
        seedvals = np.linspace(int(seeds[i]),int(seeds[i])+int(seeds[i+1])-1,int(seeds[i+1]))
        print(seedvals)
        new_seeds += list(seedvals)

    seeds = new_seeds


def pos_update(step_list,seeds):
    new_seeds = []
    for seed in seeds: 
        nseed = int(seed)
        sflag = True
        for s_match in step_list:
            match = s_match.split()
            [d, s, l] = [int(match[0]),int(match[1]),int(match[2])]
            if (nseed >= s) and (nseed < s+l):
                new_seeds.append(str(nseed+d-s))
                sflag = False
                break
        if sflag:
            new_seeds.append(seed)
    return new_seeds

# s2s = {}; s2f = {}; f2w = {}; w2l = {}; l2t = {}; t2h = {}; h2l = {}
# matches = {0:s2s, 1:s2f, 2:f2w, 3:w2l, 4:l2t, 5:t2h, 6:h2l}
matches = {}

step_list = []
i_dict = 0
flag = True
for i in  range(1,len(data)):
    if data[i][0].isnumeric():
        end = 0
        if data[i][-1].isnumeric():
            end = len(data[i])+1
        step_list.append(data[i][0:-1+end])
    elif (data[i] != "\n" and flag == False):
        seeds = pos_update(step_list, seeds) 
        matches[i_dict] = step_list
        i_dict += 1
        step_list = []
    elif data[i] != "\n" and flag == True:
        flag = False
seeds = pos_update(step_list, seeds) 
matches[i_dict] = step_list
seeds = map(int, seeds)
print(min(seeds))

# Part 2
# Create a reverse mapping
print(matches)
reverse_mapping = {}
for category in matches:
    reverse_mapping[category] = {}

# Iterate over all the mappings in reverse order
for category in reversed(list(matches.keys())):
    for s_match in matches[category]:
        match = s_match.split()
        [d, s, l] = [int(match[0]),int(match[1]),int(match[2])]
        for seed in range(s, s+l):
            if seed not in reverse_mapping[category]:
                reverse_mapping[category][seed] = d

# print(reverse_mapping)

# Find the extremums
# extremums = []
# for seed in seeds:
#     if seed in reverse_mapping['location']:
#         extremums.append(seed)

# # Print the extremums
# print(min(extremums))
